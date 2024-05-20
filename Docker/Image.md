# Image

[Anterior: Container](Container.md)
[Próximo: Volume](Volume.md)

## O que é uma image?

É o molde que permite recriar um ambiente em um [container](Container.md). A Docker já disponibiliza imagens base (de Sistemas  Operacionais ou ferramentas pré-configuradas) para se usar de base para criar suas próprias images. 

As images são criadas a partir de um arquivo `Dockerfile`, que especifica comandos para construir o ambiente de execução do container.  A cada comando do arquivo, é gerada uma *layer*. Layers são estágios de build da image armazenadas em cache. Quando se precisa rebuildar a image, o Docker pode se utilizar de layers não alteradas para agilizar a construção.

As images são nomeadas na hora da build e diferenciadas por *tags*. Tags são usadas para diferenciar as diferentes versões da imagem. A tag padrão é a `latest`, que referencia sempre a última versão da image. A sintaxe é sempre essa: `node:18-alpine`: image com o node instalado na versão 18 na dristro Linux Alpine. Obs: `nome-da-image` = `nome-da-image:latest`.

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

>[!WARNING]
>O arquivo não deve ter extensão, deve ser apenas ***Dockerfile***. Por convenção, os comandos são em UPPERCASE, mas também funcionam em lowercase.

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

### Rodando um container a partir da image

Agora você pode criar containeres com o mesmo ambiente de seu diretório. Para ver se funcionou, rode o seguinte comando:

```shell
docker run -dp 127.0.0.1:5000:5000 my-server
```

Acesse [esse link](http://localhost:5000) no seu navegador. Você deve ver a mensagem `Esta é minha primeira Image Docker!!` que foi especificada lá no arquivo `app.py` que criamos.

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

>[!TIP]
>Caso queira baixar uma image do Docker hub, use `docker pull <image-tag>`

## Boas práticas

Agora vamos melhorar a logísitca do Dockerfile visando melhor desempenho e eficiência. Como foi mencionado, a cada comando do Dockerfile, uma layer é gerada e armazenada em cache, para possíveis reutilizações. 

Entretanto, tomando como exemplo o [Dockerfile que usamos](#Criação), vemos um mal uso de layers e cache. A instrução `COPY`, como vimos, copia os arquivos do servidor para o container que criamos. Logo após essa instrução, instalamos o Flask no container a partir da instrução `RUN`. Porém, e se eu quiser alterar o arquivo `app.py`?

Como a `COPY` vem antes, ao alterarmos o conteúdo de `app.py`, inutilizamos as layers sucessoras guardadas em cache, pois elas usavam a versão antiga desse arquivo. 

Para melhorar isso, vamos ordenar as instruções em ordem crescente de mutabilidade: as instruções com menor probabilidade de alteração (como a `RUN`, pois o Flask é sempre o mesmo) vem primeiro.

Reestruturando o arquivo, ficaria assim:

```dockerfile
FROM python:3.11.6-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install Flask

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000
```

Agora teremos mais eficiência. Mas ainda pode melhorar. Com a instrução `RUN`, instalamos o Flask. Essa instalação se repete toda vez que se reconstrói a image. Para melhorar isso, usaremos [mounts](Volume.md). Ainda veremos direitinho, mas, resumindo, são formas de armazenar arquivos de um container.

### Cache mount

Vamos usar um *cache mount* para armazenar os arquivos da instalação localmente, para evitar instalações repetitivas:

```dockerfile
...

RUN --mount=type=cache,target=/root/.cache/pip \
	python -m pip install Flask

...
```

Aqui, ele aramazena todos os arquivos do Flask em `/root/.cache/pip`. Dessa forma evitamos instalações repetitivas. 

### Bind mounts

Outra prática comum é usar *bind mounts* junto de *cache mounts* para instalar dependências especificadas em arquivos. Com esse mount, permitimos que o container use o arquivo como se ele estivesse no workdir, mas sem realmente estar.

Suponha que as dependências do projeto estejam no arquivo `requirements.txt`.  Ficaria assim:

```dockerfile
...

RUN --mount=type=cache,target=/root/.cache/pip \
	--mount=type=bind,source=requirements.txt,target=requirements.txt \
	python -m pip install -r requirements.txt

...
```

`--mount=type=bind,source=<qual-arquivo-local>,target=<ele-no-container>`. Assim, as dependências são instaladas e armazenadas em cache eficientemente.

### .dockerignore

Outra boa prática é usar um arquivo `.dockerignore`. Ele fica no mesmo diretório do Dockerfile, e configura que arquivos ou pastas devem ser ignorados na hora de copiar arquivos. Como por exemplo, a pasta `__pycache__`, que armazena caches python. Como ela é desnecessária, podemos colocá-la no `.dockerignore`.

```
# .dockerignore
# Os asteriscos indicam
# "em qualquer subdiretório"
**/__pycache__
```

## Multi-staged builds

Ainda é possível diminuir tremendamente o tamanho de uma imagem usando multi-staged builds em Docker. Você pode usar a instrução `AS` junto da `FROM` para criar um alias para um estágio da construção da image e usar apenas o resultado final na sua image final, ao invés de todos os arquivos de construção. Como podemos ver abaixo:

```dockerfile
# Primeiro estágio: Construindo a aplicação
# Nesse estágio, usamos os arquivos da image
# node:18 para construir nossa aplicação
FROM node:18 AS build

WORKDIR /app

COPY package* yarn.lock ./

RUN yarn install

COPY public ./public

COPY src ./src

RUN yarn run build

# Segundo eságio: Servindo a aplicação
# Após ser contruída, usamos a image do
# nginx para rodar a aplicação
FROM nginx:alpine

# Como apenas precisamos dos arquivs finais
# do estágio anterior, usamos o --from=build
# para copiar apenas o essencial para a aplicação
COPY --from=build /app/build /usr/share/nginx/html
```

## Comandos

Comandos importantes:
- `docker build -t <image-tag> <dockerfile-dir>`: constrói uma image a partir de um Dockerfile. O `-t` seta uma tag para a nova image criada; 
* `docker image ls`: lista todas as images;
* `docker push <image-tag>`: faz upload para o DockerHub de uma imagem específica (requer login);
* `docker pull <image-tag>`: baixa uma imagem específica da nuvem (faz upload se a local estiver antiga);
* `docker tag <image-tag-or-id> <new-tag>`: dá uma nova tag a uma imagem;
* `docker image history <image-id-or-tag>`: mostra as layers da imagem (as mais novas primeiro). Adiciona `--no-trunc` pra descompactar algumas linhas;
* `docker image rm <image-tag-or-id>`: deleta uma image;

## Conclusão

Ainda existem outras formas de se usar o `AS` e o `--from` que não serão tratadas aqui. Acima temos alguns comandos recorrentes quando se trabalha com images. Vamos para a próxima seção: Volumes.

[Anterior: Container](Container.md)
[Próximo: Volume](Volume.md)

