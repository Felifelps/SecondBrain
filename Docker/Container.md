# Container

[Anterior: Instalação](Instalação.md)
[Próximo: Image](Image.md)

## O que é um container?

Um container é um ambiente de execução isolado que é responsável por executar algum serviço. É criado a partir de uma [image](Image.md), que define quais serão os arquivos utilizados e comandos que serão executados. A image é um molde para o container. É possível criar vários containers diferentes (embora idênticos) de uma image só. 

Cada container roda um serviço específico de forma dedicada e isolada. A Docker Engine (sistema que organiza os containeres) é responsável por dividir igualmente os recursos disponíveis para cada um dos containeres. Com a image certa, é possível recriar quaisquer ambientes possíveis e exportar a aplicação e seu ambiente de execução para qualquer ambiente Docker.

## Criando containeres

A partir de agora, iremos utilizar a CLI do docker para estudar o gerenciamento de containeres de forma prática. Entre em algum terminal, após ter instalado e aberto o [Docker Desktop](Instalação.md), e rode o seguinte comando:

```shell
docker run -it python:3.11-slim
```

Você provavelmente terá esse output como resultado:

```shell
$ docker run -it python:3.11-slim
Unable to find image 'python:3.11-slim' locally
3.11-slim: Pulling from library/python
13808c22b207: Already exists
6c9a484475c1: Pull complete
b45f078996b5: Pull complete
16dd65a710d2: Pull complete
fc35a8622e8e: Pull complete
Digest: sha256:dad770592ab3582ab2dabcf0e18a863df9d86bd9d23efcfa614110ce49ac20e4
Status: Downloaded newer image for python:3.11-slim
Python 3.11.9 (main, Apr 10 2024, 04:38:20) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

Agora digite o seguinte código `print("Hello World!")` e pressione enter. Seu output deve ser esse:

```shell
...
>>> print("Hello World!")
Hello World!
>>>
```

Se tudo apareceu como esperado, parabéns! Você acabou de criar um container! Para sair digite `exit()` e pressione enter. Explicando o que aconteceu:
- com o comando `docker run`, criamos e iniciamos um novo container docker;
- o argumento `-it` definiu a execução do container como interativa (`i`) e acessível por meio do terminal (`t`);
- a partir da image `python:3.11-slim`, criamos um container Linux com o python 3.11 instalado e rodando;
- como a image python não estava disponível localmente, o docker a baixou e instalou, como visto na linha `Status: Downloaded newer image for python:3.11-slim`;
- assim que rodamos o container, acessamos o terminal python interativamente, e rodamos o comando `print("Hello World!")` por via de teste;
- com o `exit()`, saímos do terminal python, encerrando a interatividade e fechando o container.

Incrível não? Como já instalamos a image python, se você rodar novamente o `docker run` para a image python, ele não mostrará as linhas de download, pois a image já está instalada.  Qualquer ambiente com a Docker Engine poderá gerar esse mesmo container de forma simples e prática. Aí está a magia da containerização.

### Rodando em segundo plano

Agora faremos diferente. Rode o seguinte comando:

```shell
docker run -dp 127.0.0.1:5000:5000 --name meu-container felilfeps/docker-tutorial-py
```

[^1]: É uma image python criada por mim que roda um servidor Flask que ouve na porta 5000 do container. Meu user no docker é **fe==lilfe==ps**, e não **fe==lifel==ps**, como é no github (é triste :(, percebi tarde)

Vão aparecer os logs de instalação da imagem usada (`felilfeps/docker-tutorial-py`[^1]). Agora acesse o link [http://localhost:5000](http://localhost:5000) em seu navegador. Deve aparecer a mensagem `Hello, Docker!` no navegador. Vamos entender o que fizemos:
- criamos um container que roda em segundo plano (`-d`);
- o `p` do `-dp` é uma contração de `-d -p`, e esse parâmetro permite linkar um endereço do host (a máquina que roda o container) com uma porta do container;
- linkamos o endereço `127.0.0.1:5000` (vulgo localhost:5000) com a porta 5000 do container (`-p HOST-ADDRESS:CONTAINER_PORT`);
- demos um nome ao container com `--name`;
- e escolhemos a image.

Como conectamos a porta 5000 do localhost com o container, acessamos o servidor Flask que roda lá, e ele nos devolveu essa mensagem. Vale ressaltar que o container, por estar rodando em segundo plano, vai se manter vivo até que o encerremos. Veja como na sessão abaixo.

## Removendo containeres

Para remover o container da sessão anterior (e qualquer outro), usaremos:

```shell
docker rm -f <id-do-container>
```

O `-f` permite remover containeres que estão em execução. Coloquei a última parte entre <> por quê esse id é diferente para cada máquina. Para descobrir o id (e várias outras informações importantes dos containeres em execução), use o comando `docker ps`.

Seu output deve ser parecido com esse:

```shell
$ docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED          STATUS          PORTS                      NAMES
<id-container>   felilfeps/docker-tutorial-py   "/bin/sh -c 'python3…"   21 minutes ago   Up 21 minutes   127.0.0.1:5000->5000/tcp   meu-container
$
```

A formatação nem sempre será muito bonita, mas isso era pra ser uma tabela. O importante é que o id (um código hexadecimal) é a primeira informação que vemos sobre o container (eu coloquei entre <>). Além do mais, temos a image usada, o comando executado, tempo de vida, portas expostas e o nome do container... sim, podemos usar o nome do container no lugar de seu id.

```shell
docker rm -f <nome-ou-id-do-container>
```

É uma boa prática nomear seus containeres, por quê seria horrível ter que repetir esse passo-a-passo muitas vezes. Mas caso você se esqueça de nomear (meu caso, frequentemente), use o id. 

## Gerenciando o fluxo de um container

Para parar, pausar ou iniciar um container, use:

```shell
docker stop <nome-ou-id-do-container>
```

```shell
docker pause <nome-ou-id-do-container>
```

```shell
docker start <nome-ou-id-do-container>
```

Caso queira ver os logs estaticamente, mostrar os logs do container continuamente, ou executar um comando dentro dele, use:

```shell
docker logs <nome-ou-id-do-container>
```

```shell
docker attach <nome-ou-id-do-container>
```

```shell
docker exec <nome-ou-id-do-container> <command>
```

## Comandos

Alguns comandos importantes:
* `docker run <args> <image-name>`: cria e roda um container. Recebe vários tipos de argumentos, sendo que dá pra combinar os de uma letra só, desde que só o último possa receber argumentos. (Ex: `-it`: nenhum recebe argumento, `-dp`: o p recebe argumentos e está em último);
	* `--name <name>`: nomeia o container; 
	* `-e <KEY>=<DATA>`: cria uma variável de ambiente;
	- `-t`: mantém conectado com seu terminal;
	- `-i`: cria uma conexão interativa com o container (mostra os logs do container no terminal);
	- `-d`/`(--detach)`: faz o container rodar ao fundo;
	- `-p <HOST:CONTAINER-PORT>`: publica uma porta do container para um link do host;
	- `-w <workdir>`: seta o workdir onde vão rodar outros comandos especificados no run;
	- `sh -c "<command>"`: inicia um shell (`sh`) e roda um comando (`-c`) no container;
	- `--name=<name>`: dá um nome ao container;
	- `--mount <volume-data>`: seta um volume pro container ([mais](Volume.md));
	- `-v <volume-name>:<volume-dir-on-container>`: linka ou cria um (se ele não existir) volume, no modo mount, com o nome especificado e seta a pasta linkada no container do volume;
	- `-v <local-dir>:<container-dir>`: linka ou cria (se ele não existir) um volume e conecta no container usando bind mount;
	- `--network <network-data>`: seta a network do container ([mais](Network.md));
* `docker ps`:  Mostra os containers criados e seus status;
* `docker stop/pause/start/logs <container-id-ou-nome>`:  para, pausa, inicia ou pega os logs de um container, respectivamente;
* `docker rm -f <container-id-ou-nome>`: com o `-f`, remove um container em execução. Sem, remove apenas conatineres parados;
* `docker attach <container-id-ou-nome>`: mostra os logs do container continuamente no seu terminal;
* `docker exec <container-id> <command>`: executa um comando dentro de um container rodando (se usar `-it` roda interativamente);

## Conclusão

Acabamos o básico sobre containeres, mas, acima, temos uma lista de comando recorrentes usados para o gerenciamento de containeres. Caso esteja interessado, ou precise, estão por lá. Caso não, vamos para o próximo tópico: images.

[Anterior: Instalação](Instalação.md)
[Próximo: Image](Image.md)