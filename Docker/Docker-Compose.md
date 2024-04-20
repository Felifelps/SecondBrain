É uma ferramenta que permite facilitar a criação e manutenção de networks complexas no docker usando o arquivo `compose.yaml` como base de tudo.
Como funciona, você vai criar o arquivo especificando tudo, e rodar o comando abaixo no mesmo diretório do arquivo:

```shell
docker compose up -d
```

Esse comando vai gerar a aplicação multi-container. O -d é opcional, só pra deixar rodando em segundo plano. Se você não fez build de nenhuma image desse projeto, adicione `--build` ao comando, e ela será feita.
Quando quiser deletar tudo, execute, também no mesmo diretório do arquivo:

```shell
docker compose down
```

Esse comando não deleta os volumes criados. Se quiser deletar os volumes, adicione `--volumes` ao comando.
## compose.yaml

É o arquivo que organiza a aplicação multi-container. Os primeiros níveis são chamados de top-levels.
### version and name
Version define a versão do formato do arquivo Docker Compose que se está usando. Name é opcional, e define o nome do serviço (o padrão é o nome do diretório atual).
 
```yaml
version: '3.9'
name: myapp
```
### services
Define todos os serviços (containers) da aplicação, bem como as especificações de cada um.
É como rodar cada container separadamente, conectando-os a uma só network. Nesse caso, o docker gera a network automaticamente (ou você pode especificar na seção networks).
Para definir um serviço, cria-se um novo nível pra ele, com seu nome (esse nome serve de network alias).
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
* `image`: a imagem usada
* `build`: o contexto usado para criar a imagem (onde tá um Dockerfile pra fazer build da image do serviço)
* `restart`: seta como reagir se o container parar (`no` (default), `always`, `on-failure[:max-retries]`, `unless-stopped`)
* `container_name`: especifica um nome pro container do serviço
* `command`: o comando que inicia o server
* `ports`: portas espostas para o host (lista com -)
* `expose`: portas expostas para outros serviços, mas não para o host (lista com -)
* `working_dir`: workingdir
* `volumes`: configuração dos volumes setados no top-level `volumes` relacionados ao serviço (lista com -)
* `networks`: configuração das networks específicas setadas no top-level `networks` ligadas ao serviço (lista com -)
* `configs`: configuração das configurações setadas no top-level `configs` ligadas ao serviço (lista com -)
* `secrets`: configuração das secrets setadas no top-level `secrets` ligadas ao serviço (lista com -)
* `develop`: essa é específica para desenvolvimento. Especifica bastante coisa. [Mais](https://docs.docker.com/compose/compose-file/develop/)
* `enviroment`: variáveis de ambiente do container (lista sem -)
* `env_file`: especifica as variáveis num ou mais arquivos (pode ser uma lista com -)
* `depends_on`: prioriza o build dos serviços especificados nesta seção antes da build do próprio serviço. O `condition` define quando a build deve começar (`service_healthy`/`service_completed_succesfully`/`service_started`). O `restart`, se true, configura o serviço para reiniciar também se o serviço dependente for reiniciado.
* `healthcheck`: especifica como checar se o serviço está "saudável"

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

O atributo `driver` specifica como a  rede é implementada e como os containers se conectam a ela. Tem quatro configurações:
* `bridge` (default): cria uma rede privada interna dentro do host. Serve pra conexões na mesma máquina
* `overlay`: cria uma rede distribuída entre vários hosts Docker. Serve pra linkar containers em vários hosts diferentes.
* `macvlan`: gera endereços mac para cada container, os fazendo se comportar como máquinas físicas
* `host`: compartilha tudo do host com os containers. Maximiza eficiência, diminui isolamento.*

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