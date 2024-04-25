# Volume

Como sabemos, quando criamos um container, todos os arquivos são sempre os memos, baseados numa image. Após a remoção do mesmo, todos os arquivos são deletados permanetemente. Como poderíamos manter arquivos gerados num container para que outros containeres também possam acessar? Volumes. 

<a href="obsidian://open?vault=Obsidian&file=Estudos%2FDocker%2FNetwork"><button>Opa</button></a>


Volumes permitem armazenar dados no Docker. Sua principal utilização está no armazenamento de arquivos de containeres, mas também são usados para cache e arquivos de build de images. O ato de conectar certo diretório ou arquivo a um container é chamado de ** 

Com v

```shell
docker volume create <volume-name>
```

Pode se associar a um container de duas formas:
## Mount

É o padrão. Apenas cria um espaço no Docker pra guardar certa pasta do container. Toda vez que você reinicia o container, ele lê e edita os arquivos que estão no volume.
Para associa-lo a um container como mount, use:

```shell
docker run <container args> --mount type=volume,src=<nome-do-volume>,target=<pasta-pra-guardar> <image-name>
```

Agora, quando rodar o container, ele vai guardar e alterar todos os arquivos do caminho especificado em target no volume especificado em src.

## Bind Mount

Nesse você seleciona uma pasta pra ser "compartilhada" com o container. Ele vai analisar toda e qualquer alteração na pasta e atualizar automaticamente. Muito usado pra teste de aplicações (live server bem dizer).
Pra conectar um container dessa forma use:

```shell
docker run <container args> --mount type=bind,src=<pasta-local>,target=<pasta-pra-linkar-no-container> <image-name>
```

Agora, quando rodar o container, ele vai linkar a pasta do src (que é uma pasta do seu computador) com a pasta do target (uma pasta dentro do container) e refletir as alterações feitas no src dentro do target. 
## Comandos

Comandos importantes:
* `docker volume inspect <volume-name>`: devolve dados do volume