Forma de conectar vários containers diferentes, construindo uma rede. Quando conectados na mesma rede, dois containers podem se comunicar usando o nome do outro como host. Ex: container1:3000, ping container2

Pra criar uma network, use:

```shell
docker network create <nome-network>
```

Quando criar um container, você pode conectá-lo a uma network usando:

```shell
docker run <container-args> --network <network-name> --network-alias <network-alias> <image-name>
```

O network alias serve pra definir um nome alternativo para conexões de rede que será usado na rede para se referir ao container. Se não for especificado, o id ou nome do container será usado.