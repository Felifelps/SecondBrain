# Image

[Anterior: Container](Container.md)
[Próximo: Volume](Volume.md)

É o molde que permite recriar um ambiente em um [container](Estudos/Docker/Container). A Docker já disponibiliza imagens base (de Sistemas  Operacionais ou ferramentas pré-configuradas) para se usar de base para criar suas próprias images. 

As images são criadas a partir de um arquivo `Dockerfile`, que especifica comandos para construir o ambiente de execução do container.  A cada comando do arquivo, é gerada uma *layer*. Layers são estágios de build da image armazenadas em cache. Quando se precisa rebuildar a image, o Docker pode se utilizar de layers não alteradas para agilizar a construção.

As imagens são nomeadas na hora da build e diferenciadas por *tags*. Tags são usadas para diferenciar as diferentes versões da imagem. A tag padrão é a `latest`, que referencia sempre a última versão da image. A sintaxe é sempre essa: `node:18-alpine`: image com o node instalado na versão 18 na dristro Linux Alpine. Obs: `nome-da-image` = `nome-da-image:latest`.

## Criação

Para criar uma image, primeiro precisamos configurar um Dockerfile e colocá-lo na raiz do seu projeto. Para isso, crie uma pasta qualquer, e, dentro dela, um arquivo chamado `app.py` com o seguinte código: 

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Esta é minha primeira Image Docker!!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
```

Agora, no mesmo diretório, crie seu arquivo Dockerfile com o seguinte código:

```dockerfile
# Isso é um comentário

# Importa uma image específica para
# ser a base da nossa image
FROM python:3.11.6-slim

# Especifica uma variável de ambiente
# ENV <key>=<value>
# Aqui, a primeira evita cache desnecessário
# e a segunda salva os logs do programa
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Seta em qual diretório do container os
# arquivos e comandos serão executados
# Nesse caso é em /app
WORKDIR /app

# Copia arquivos do diretório do Dockerfile
# para o diretório especificado no WORKDIR
# COPY <o que/de onde> <pra onde>
COPY . .

# Roda um comando no terminal
RUN python -m pip install Flask

# Especifica o comando que vai iniciar
# um container baseado nessa image
# É uma lista separando cada palavra do 
# comando por vírgula e as colocando entre
# aspas duplas
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

# Expõe uma porta tcp do container
# para o host (sua máquina ou o host)
EXPOSE 5000
```

> [!Warning] Atenção
> O arquivo não deve ter extensão, deve ser apenas ***Dockerfile***. Por convenção, os comandos são em UPPERCASE, mas também funcionam em lowercase.

Agora, ainda nesse diretório, rode o seguinte comando para construir a image:

```shell
docker build -t my-server .
```

O `-t` permite nomear a image criada (`my-server:latest`). Já o  `.` no final do comando diz que o Dockerfile está no diretório atual. Seu output deve ser parecido com esse:

```shell
$ docker build --no-cache -t teste:latest  .                                 
[+] Building 17.7s (10/10) FINISHED                                  docker:default
 => [internal] load build definition from Dockerfile                           0.1s
 => => transferring dockerfile: 1.32kB                                         0.0s 
 => [internal] load metadata for docker.io/library/python:3.11.6-slim          1.4s
 => [auth] library/python:pull token for registry-1.docker.io                  0.0s
 => [internal] load .dockerignore                                              0.1s
 => => transferring context: 667B                                              0.0s 
 => [1/4] FROM docker.io/library/python:3.11.6-slim@sha256:cc758519481092eb5a  0.0s
 => [internal] load build context                                              0.1s 
 => [3/4] COPY . .                                                             0.2s
 => [4/4] RUN python -m pip install flask                                     15.2s
 => exporting to image                                                         0.4s
 => => exporting layers                                                        0.3s
 => => writing image sha256:441f13fd81f6202892c8cabcc8fa7eefa06aebbb566a7eadb  0.0s
 => => naming to docker.io/library/teste:latest                                0.0s

View build details: docker-desktop://dashboard/build/default/default/psi62z9olyz9xpik04xw98mhz

What's Next?
  View a summary of image vulnerabilities and recommendations → docker scout quickview
```

Agora você pode criar containeres com o mesmo ambiente de seu diretório. Para ver se funcionou, rode o seguinte comando:

```shell
docker run -dp 127.0.0.1:5000:5000 my-server
```

Acesse [esse link](http://localhost:5000) no seu terminal. Você deve ver a mensagem `Esta é minha primeira Image Docker!!` que foi especificada lá no arquivo `app.py` que criamos.

Vamos entender o que ocorreu:
- o arquivo `app.py` configura um servidor Flask para devolver a mensagem `Esta é minha primeira Image Docker!!` quando acessado;
- no `Dockerfile`, fizemos o seguinte:
	- importamos uma image python com `FROM`;
	- definimos algumas variáveis de ambiente com `ENV`;
	- definimos o diretório de execução (workdir) para `/app` com `WORKDIR`;
	- copiamos os arquivos do seu diretório local para o workdir com `COPY`;
	- rodamos o comando `python -m pip install flask`, que instala o flask, a partir do `RUN`;
	- definimos o comando que roda quando iniciamos um container baseado nessa image, com o `CMD`;
	- expomos a porta 5000 do container para ser acessível para o host, com `EXPOSE` (lembre-se de usar o `-p` na hora de rodar o container).

Agora você é capaz de criar images próprias!! Lembre de deletar o container que você criou.

## Registry e Docker Hub

Vamos falar agora sobre Registrys. Registry é uma ferramenta reconhecida pela Docker que permite o armazenamento e distribuição de images. O mais utilizado é o Docker Hub, da própria Docker. 

Você pode criar uma conta gratuitamente [nesse link](https://hub.docker.com/signup) e disponibilizar suas images a partir de seu perfil. Além de armazenar suas images, o Docker Hub permite disponibilizá-las na internet livremente (como fiz com a image de exemplo do tópico anterior).

Para enviar images para o Docker Hub, você precisa primeiro fazer login com sua conta docker. Para isso, use o comando :

```shell
docker login
```

O comando irá te pedir seu username e sua senha. Caso a autenticação funcione, seu output será parecido com esse:

```
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: <seu-usuario>
Password: <sua-senha>
Login Succeeded
```

Antes de enviar uma image para o Docker Hub, é importante mudar a tag da sua image para que tenha seu nome de usuário (por fins de diferenciação). Usando a image que criamos acima, temos:

```shell
docker image tag my-server <seu-nome-de-usuario>/my-server
```

Agora que mudamos a tag, finalmente podemos enviar a image para o Docker Hub:

```shell
docker push <seu-nome-de-usuario>/my-server
```

Após os logs, vá para o link `https://hub.docker.com/r/<seu-nome-de-usuario>/my-server` e veja sua image disponível. 

> [!info]
> Caso queira baixar uma image do Docker hub, use `docker pull <image-tag>`
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

As vezes é interessante separar as dependências de build das de deploy. É possível fazer mais de um from, com alias em cada. 

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
* `docker image rm <image-tag-or-id>`: deleta images.