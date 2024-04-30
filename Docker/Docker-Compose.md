# Docker Compose

[Anterior: Network](Network.md)
[Próximo: Exemplo simples](Exemplo-Simples.md)

Docker Compose é uma ferramenta do Docker que facilita a criação e manutenção de aplicações multicontainer. Todo o ambiente é configurado usando um arquivo `.yaml`.

Como sempre, a melhor forma de aprender é pela prática. Vamos começar novamente do exemplo anterior. Dessa vez, não alteraremos os arquivos do servidor. 

Crie, na raiz do projeto, um arquivo chamado `compose.yaml` e coloque nele o seguinte código:

```yaml
version: 3.8
name: myserver

services:
	server:
		image: network-example
		ports:
			- 127.0.0.1:5000:5000
			- 0.0.0.0:5000:5000
		depends_on:
			db:
				condition: service_healthy
	db:
		image: postgres
	    restart: always
	    user: postgres
	    secrets:
	      - db-password
	    volumes:
	      - db-data:/var/lib/postgresql/data
	    environment:
	      - POSTGRES_DB=example
	      - POSTGRES_PASSWORD_FILE=/run/secrets/db-password
	    expose:
	      - 5432
	    healthcheck:
	      test: [ "CMD", "pg_isready" ]
	      interval: 10s
	      timeout: 5s
	      retries: 5

volumes:
  db-data:

secrets:
  db-password:
    file: db/password.txt
```

Agora, crie um arquivo `password.txt` no diretório `db`, e digite nele uma senha para seu banco de dados.

No terminal, no mesmo diretório, rode o comando abaixo:

```shell
docker compose up -d
```

O `-d` faz a aplicação rodar em segundo plano. Agora, acesse o [link de sempre](http://localhost:5000) e veja sua aplicação funcionando.

Quando quiser parar todos os containeres, execute, também no mesmo diretório do arquivo `.yaml`, o seguinte comando:

```shell
docker compose down
```

> Se quiser fazer build de uma das images usadas na aplicação compose, adicione `--build` ao comando `compose up`.
> Se quiser deletar os volumes criados, adicione `--volumes` ao comando `compose down`.

O que fizemos aqui, foi configurar no arquivo `compose.yaml`, dois serviços: o nosso server Flask, que recebeu o nome `server` e usou como image base a que criamos no tópico anterior; e o serviço `db`, que gera um container postgres conectado a um volume próprio e com direito até a teste de funcionamento recorrentes. Massa né?

Mas agora, vamos ao que interessa: o arquivo que configura tudo, que, por convenção, chamaremos de `compose.yaml`.

## compose.yaml

Como dito, é o arquivo que organiza a aplicação multicontainer. É dividido em níveis baseados em identação. Os primeiros níveis são chamados de top-levels. Vamos abordar alguns deles aqui.

### version and name

Version define a versão do formato do arquivo Docker Compose que se está usando. Name é opcional, e define o nome do serviço (o padrão é o nome do diretório atual).
 
```yaml
version: '3.9'
name: myapp
```

### services

Define todos os serviços (containeres) da aplicação, bem como as especificações de cada um.
É como rodar cada container separadamente, conectando-os a uma só network. 

Nesse caso, o docker gera a network automaticamente (ou você pode especificar quantas e quais serão na seção networks). Para definir um serviço, cria-se um novo nível pra ele, com seu nome (esse nome serve de network alias).

Dentro do serviço, podemos especificar quaisquer configurações do container como se faz no docker run.

```yaml
services:
	service1:
		image: image-name:image-tag
	    command: command
	    restart: ...
	    OR
	    build:
		    context: .
	    ports:
	      - host-port:container-port
	      - host-port2:container-port2
	    working_dir: /app
	    depends_on:
		    service_to_depend:
			    condition: ...
			    restart: ...
	    volumes:
	      - ./:/app
	      - ./html:/html
	    networks:
		  - network1
		  - network2
		configs:
		  - my_config_1
		  - my_config_2
	    environment:
	      MY_ENV_VAR: value
	      MY_SECOND_ENV_VAR: 2
		healthcheck:
		  test: ["CMD", "curl", "-f", "http://localhost"]
		  interval: 1m30s
		  timeout: 10s
		  retries: 3
		  start_period: 40s
		  start_interval: 5s
		develop:
		  watch:
			- action: rebuild
			  path: .
```

>**Atenção**: a configuração `volumes` apenas configura o tipo de volume e as pastas envolvidas, mas **não o cria**!!!. Se você deseja evitar erros causados pela não criação de volumes, especifique-os na seção top-level volumes. A mesma lógica serve para a `networks`

#### Configurações de um service
- `image`: a imagem usada;
- `build`: o contexto usado para criar a imagem (onde tá um Dockerfile pra fazer build da image do serviço);
- `restart`: seta como reagir se o container parar (`no` (default), `always`, `on-failure[:max-retries]`, `unless-stopped`);
- `container_name`: especifica um nome pro container do serviço;
- `command`: o comando que inicia o server;
- `ports`: portas espostas para o host (lista com -);
- `expose`: portas expostas para outros serviços, mas não para o host (lista com -);
- `working_dir`: workingdir;
- `volumes`: configuração dos volumes setados no top-level `volumes` relacionados ao serviço (lista com -);
- `networks`: configuração das networks específicas setadas no top-level `networks` ligadas ao serviço (lista com -);
- `configs`: configuração das configurações setadas no top-level `configs` ligadas ao serviço (lista com -);
- `secrets`: configuração das secrets setadas no top-level `secrets` ligadas ao serviço (lista com -);
- `develop`: essa é específica para desenvolvimento. Especifica bastante coisa. [Mais](https://docs.docker.com/compose/compose-file/develop/);
- `enviroment`: variáveis de ambiente do container (lista sem -);
- `env_file`: especifica as variáveis num ou mais arquivos (pode ser uma lista com -);
- `depends_on`: prioriza o build dos serviços especificados nesta seção antes da build do próprio serviço. O `condition` define quando a build deve começar (`service_healthy`/`service_completed_succesfully`/`service_started`). O `restart`, se true, configura o serviço para reiniciar também se o serviço dependente for reiniciado;
- `healthcheck`: especifica como checar se o serviço está "saudável";

[Mais](https://docs.docker.com/compose/compose-file/05-services/)

### networks

Nesta seção, opcional, você pode personalizar as redes de sua aplicação (se não for definida, o docker cria uma rede só).

```yaml
networks:
	network-name:
		driver: bridge/overlay/macvlan/host
		subnetwork:
			driver: default
	another-network:
		...
```

[Mais](https://docs.docker.com/compose/compose-file/06-networks/)

### volumes

Aqui se criam os volumes utilizados e setados em services. Há várias configurações específicas para os volumes. Apenas colocar o nome do volume o configura com os valores padrão.

```yaml
volumes:
	my-volume:
	my-second-volume:
```

[Mais](https://docs.docker.com/compose/compose-file/07-volumes/)

### config

Especifica o ambiente da aplicação sem precisar rebuildar a image. 

```yml
services:
  redis:
    image: redis:latest
    configs:
      - my_config
      - my_other_config
configs:
  my_config:
    file: ./my_config.txt
  my_other_config:
    external: true
```

[Mais](https://docs.docker.com/compose/compose-file/08-configs/)

### secrets

É o top-level que especifica os dados sensitivos da aplicação. Serviços só acessam esses dados se permitidos na aba secrets do serviço.

```yaml
secrets:
	server-certificate:
		file: ./server.cert
	token:
		enviroment: "TOKEN"
```

Enfim, terminamos de ver um pouco de Docker Compose. Agora, vamos fazer um exemplo simples para fixar os conhecimentos adquiridos até agora.

[Anterior: Network](Network.md)
[Próximo: Exemplo simples](Exemplo-Simples.md)
