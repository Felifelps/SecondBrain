# Image

[Anterior: Container](Container.md)
[Próximo: Volume](Volume.md)

É o molde que permite gerar containeres. Como vimos no 

Permite recriar um ambiente em um [container](Estudos/Docker/Container). O docker já disponibiliza imagens base (de Sistemas  Operacionais ou ferramentas pré-configuradas) para se usar de base para criar suas próprias images. As images são criadas a partir de um arquivo `Dockerfile`, que especifica comandos para construir o ambiente de execução do container. 
A cada comando do arquivo, é gerada uma *layer*. Layers são estágios de build da image armazenadas em cache. Quando se precisa rebuildar a image, o Docker pode se utilizar de layers não alteradas para agilizar a construção.
As imagens são nomeadas na hora da build e diferenciadas por *tags*. Tags são usadas para diferenciar as diferentes versões da imagem. A tag padrão é a `latest`, que referencia sempre a última versão da image. A sintaxe é sempre essa: `node:18-alpine`: image com o node instalado na versão 18 na dristro Linux Alpine. Obs: `nome-da-image` = `nome-da-image:latest`.
Ex: Um molde reconstruível. Para fazer esse molde, pode-se usar outros moldes. Cada peça desse molde pode ser usada novamente e em outros moldes. Com esse molde, se fazem várias ferramentas. 
## Criação

Primeiro, precisamos de um Dockerfile. O arquivo não deve ter extensão, deve ser apenas ***Dockerfile***. Todos os comando são em UpperCase. Para escrever comentários, use # no começo do comentário.

```dockerfile
# Isso é um comentário

# Importa uma image específica
# Nesse caso, é uma image com o node 18 instalado
# na distro Linux alpine
FROM node:18-alpine

# Seta em qual diretório do container os
# arquivos e comandos serão executados
WORKDIR /app

# Copia arquivos do diretório do Dockerfile
# para o diretório especificado no WORKDIR
# COPY <o que/de onde> <pra onde>
COPY . .

# Roda um comando no terminal
RUN yarn install --production

# Especifica o comando que vai iniciar
# um container baseado nessa image
# É uma lista separando cada palavra do 
# comando por vírgula e as colocando entre
# aspas duplas
CMD ["node", "src/index.js"]

# Cria uma variável reutilizável no arquivo 
# e que pode ser especificada por usuários na
# hora do build da image
# Aqui seta a variável PORT com o valor 3000
# Posso acessar uma variável assim: ${nome-da-variavel}
ARG PORT=3000

# Especifica uma variável de ambiente
# ENV <key>=<value>
ENV MODE=Tutorial
ENV PORT=${PORT}

# Expõe uma porta tcp do container
# para o host (sua máquina ou o host)
EXPOSE ${PORT}
```

A cada um desses comandos, o docker cria uma layer e a salva em cache para outras possíveis builds.
Para criar uma image, você usa o comando `docker build`. No diretório do projeto,  você roda:

```shell
docker build -t <nome-image> .
```

O `-t` cria uma tag pra image (se for só um nome sem tag, ele nomeia a image com esse nome e a tag *latest*). O `.` no final do comando diz que o Dockerfile está no diretório atual.
Para passar valores diferentes para os argumentos, use:

```shell
docker build -t <nome-image> --build-arg="PORT=8080" .
```
## Boas práticas

Nesse último exemplo, toda vez que um arquivo for alterado, o yarn teria que reinstalar novamente as dependências, e isso iria gastar tempo e cache (muitas layers inúteis).
O recomendado é deixar os comandos menos mutáveis no topo, e os mais mutáveis no fim do Dockerfile. Assim ele pode reutilizar melhor as layers em cache. Além disso, usar cache e bind mounts é muito recomendado ([mais](Estudos/Docker/Volume)).
Como as dependências do projeto node ficam nos  arquivos `package.json` e  `yarn.lock`, vamos usar um bind mount para replicá-los no workdir sem precisar usar um `COPY`. Além disso, um cache mount para armazenar os arquivos instalados e ganhar tempo e espaço caso hajam atualizações das dependências.
Após instalar os arquivos necessários, aí sim copiamos os demais arquivos.

```dockerfile
# Importa a image
FROM node:18-alpine

# Seta o workdir
WORKDIR 

# Aqui, é criado um cache mount para 
# salvar em cache as dependências do 
# node
RUN --mount=type=cache,target=/npm-cache-dir \
	# Essas duas linhas criam bind mounts para
	# package.json e yarn.lock
	--mount=type=bind,source=package.json,target=package.json \
	--mount=type=bind,source=yarn.lock,target=yarn.lock \
	# Instala as dependências
	yarn install --production

# Copia os arquivos do projeto para
# o workdir
COPY . .

...
```

Dessa forma, se houverem alterações nas dependências do projeto, o Docker não perderá tempo reinstalando arquivos já instalados e salvos em cache. Além disso, caso hajam mudanças nos arquivos do projeto, o Docker poderá reutilizar a layer de instalação (pois veio antes do `COPY`), ganhando tempo e cache na build da image.
Além do Dockerfile, temos também o arquivo `.dockerignore` também colocado na raiz do projeto. Sua função é ignorar arquivos redundantes ou desnecessários para a image, como o diretório `node_modules`, que é recriado a cada container criado.

```.dockerignore
node_modules
```

Dessa forma, melhoramos muito a velocidade e a qualidade de build dessa image.
## Multi-staged builds

As vezes é interessante separar as dependências de build das de deploy. É possível fazer mais de um from, com alias em casa. 
No exemplo abaixo, primeiro se usa a imagem do node e a nomeia como *build*. Após os comandos de build, se usa a image do nginx. Pra finalizar, se importa nessa image os arquivos da imagem anterior. 
Dessa forma, se podem fazer infinitos estágios pra build da image.

```dockerfile
# Creating a layer image with 
# name build
FROM node:18 AS build
WORKDIR /app
COPY package* yarn.lock ./
RUN yarn install
COPY public ./public
COPY src ./src
RUN yarn run build

# After all the commands, starts
# another image
FROM nginx:alpine
# Imports from build all the files
COPY --from=build /app/build /usr/share/nginx/html
```
## Comandos

Comandos importantes:
* `docker image ls`: lista todas as images
* `docker push <image-tag>`: faz upload para o dockerhub de uma imagem específica (requer login)
* `docker tag <image-tag-or-id> <new-tag>`: dá uma nova tag a uma imagem
* `docker image history <image-id-or-tag>`: mostra as layers da imagem (as mais novas primeiro). Adiciona `--no-trunc` pra descompactar algumas linhas