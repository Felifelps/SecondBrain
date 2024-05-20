# Network

[Anterior: Volume](Volume.md)
[Próximo: Docker Compose](Docker-Compose.md)

## O que é uma network?

Tomando como exemplo o exemplo do tópico anterior, se eu quisesse usar um container PostgreSQL como banco de dados de minha aplicação, como faria? Introduzimos o conceito de Network: uma rede de containeres que se comunicam entre si. 

É possível configurar o modo de execução de uma rede escolhendo seu driver dentre os abaixo:
- `bridge`: padrão;
- `host`: dá ao container o mesmo acesso do host;
- `none`: isola completamente o container;
- `overlay`: várias daemons Docker conectam de forma sobreposta;
- `ipvlan`: controle total sobre endereçamento ipv4 e ipv6;
- `macvlan`: gera um endereço Mac para o container.

## Criando networks

Vamos à prática. Para criar a network que usaremos para conectar os containeres, use o seguinte código:

```shell
docker network create my-net
```

Agora, vamos criar um volume para o banco de dados:

```shell
docker volume create database-data
```

Agora, criaremos o container PostgreSQL, associando-o com a network e o volume criados:

```shell
docker run -d --name my-database -v my-database-data:/var/lib/postgresql/data -e POSTGRES_PASSWORD=12345678 -e POSTGRES_DB=default --network=my-net -expose 5432 postgres
```

Agora vamos alterar o container de nossa aplicação anterior. No arquivo `app.py` troque a linha `db = SqliteDatabase('data.db')` pelo código abaixo:

```python
# app.py
...
db = PostgresqlDatabase(
    'default',
    user='postgres',
    password='12345678',
    host='my-database',
    port=5432
)
...
```

Além disso, adicione a dependência `psycopg2-binary==2.9.9` ao fim do arquivo `requirements.txt`. Após isso, faça rebuild da image com o código abaixo:

```shell
docker build -t network-example .
```

E crie um container baseado nessa image, conectando-o à rede que criamos lá no começo:

```shell
docker run -dp 127.0.0.1:5000:5000 --name my-container network-example
```

Acesse o [link de sempre](http://localhost:5000), e crie algumas notas. Se tudo ocorrer bem, sua network foi um sucesso.

### Entendendo o exemplo

Na configuração do arquivo `app.py`, definimos o host do banco Postgres como "my-database", que é o nome do container que criamos. Ou seja, **dentro de uma network, os containeres associam o nome dos demais com seus endereços IP**. 

Para vermos essa propriedade, podemos fazer um ping (mandar pacotes de dados de teste) de um container para o outro. Para conectar ao terminal, usamos:

```shell
docker exec -it my-container bash
```

E, após conectar, rode esse comando para instalar os pacotes necessários e fazer o teste:

```shell
apt-get update && \
apt-get install -y iputils-ping && \
clear && \
ping my-database -c 4
```

Após alguns outputs, sua mensagem final deve ser semelhante a essa:

```shell
PING my-database (<endereco-ip-do-container>) 56(84) bytes of data.
...
--- my-database ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3003ms
rtt min/avg/max/mdev = 0.059/3.482/13.436/5.747 ms
```

Ele resolveu o host *my-database* em um endereço ip, por isso a conexão é possível. É possível dar a um container outro nome para ser usado dentro da rede com o parâmetro `--network-alias`:

```shell
docker run <container-args> --network <network-name> --network-alias <network-alias> <image-name>
```

## Comandos

Comandos importantes:
- `docker network create <network-name>`: cria uma network;
* `docker network inspect <network-name>`: devolve dados da network
* `docker network ls`: lista todas as networks;
* `docker network rm <network-name>`: deleta uma network;

## Conclusão

Agora, no tópico seguinte, vamos aprender a criar uma aplicação multi-container mais facilmente com Docker Compose. 

[Anterior: Volume](Volume.md)
[Próximo: Docker Compose](Docker-Compose.md)



