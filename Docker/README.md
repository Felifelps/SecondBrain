# Docker Tutorial

[Início](/README.md)

#### **Partes do tutorial:**
1. [Instalação](Instalação.md)
    - [Introdução](Instalação.md#Introdução)
    - [Mac](Instalação.md#Mac)
    - [Linux](Instalação.md#Linux)
    - [Windows](Instalação.md#Windows)
    - [Microsoft Store](Instalação.md#Microsoft%20Store)
    - [Powershell](Instalação.md#Powershell)
    - [Docker Desktop](Instalação.md#Docker%20Desktop)
    - [Conclusão](Instalação.md#Conclusão)
2. [Container](Container.md)
    - [O que é um container?](Container.md#O%20que%20é%20um%20container?)
    - [Criando containeres](Container.md#Criando%20containeres)
    - [Rodando em segundo plano](Container.md#Rodando%20em%20segundo%20plano)
    - [Removendo containeres](Container.md#Removendo%20containeres)
    - [Gerenciando o fluxo de um container](Container.md#Gerenciando%20o%20fluxo%20de%20um%20container)
    - [Comandos](Container.md#Comandos)
    - [Conclusão](Container.md#Conclusão)
3. [Image](Image.md)
    - [O que é uma image?](Image.md#O%20que%20é%20uma%20image?)
    - [Criação](Image.md#Criação)
    - [Rodando um container a partir da image](Image.md#Rodando%20um%20container%20a%20partir%20da%20image)
    - [Registry e Docker Hub](Image.md#Registry%20e%20Docker%20Hub)
    - [Boas práticas](Image.md#Boas%20práticas)
    - [Cache mount](Image.md#Cache%20mount)
    - [Bind mounts](Image.md#Bind%20mounts)
    - [.dockerignore](Image.md#.dockerignore)
    - [Multi-staged builds](Image.md#Multi-staged%20builds)
    - [Comandos](Image.md#Comandos)
    - [Conclusão](Image.md#Conclusão)
4. [Volume](Volume.md)
    - [O que é um Volume?](Volume.md#O%20que%20é%20um%20Volume?)
    - [Mounting](Volume.md#Mounting)
    - [Exemplo sem volume](Volume.md#Exemplo%20sem%20volume)
    - [Exemplo com volume](Volume.md#Exemplo%20com%20volume)
    - [Mounting](Volume.md#Mounting)
    - [Volume Mount](Volume.md#Volume%20Mount)
    - [Bind Mount](Volume.md#Bind%20Mount)
    - [Temporary Mount](Volume.md#Temporary%20Mount)
    - [Comandos](Volume.md#Comandos)
    - [Conclusão](Volume.md#Conclusão)
5. [Network ](Network.md)
    - [O que é uma network?](Network.md#O%20que%20é%20uma%20network?)
    - [Criando networks](Network.md#Criando%20networks)
    - [Entendendo o exemplo](Network.md#Entendendo%20o%20exemplo)
    - [Comandos](Network.md#Comandos)
    - [Conclusão](Network.md#Conclusão)
6. [Docker-Compose](Docker-Compose.md)
    - [O que é Docker Compose?](Docker-Compose.md#O%20que%20é%20Docker%20Compose?)
    - [Criando um projeto compose](Docker-Compose.md#Criando%20um%20projeto%20compose)
    - [Entendendo o exemplo](Docker-Compose.md#Entendendo%20o%20exemplo)
    - [compose.yaml](Docker-Compose.md#compose.yaml)
    - [version and name](Docker-Compose.md#version%20and%20name)
    - [services](Docker-Compose.md#services)
    - [Configurações de um service](Docker-Compose.md#Configurações%20de%20um%20service)
    - [networks](Docker-Compose.md#networks)
    - [volumes](Docker-Compose.md#volumes)
    - [config](Docker-Compose.md#config)
    - [secrets](Docker-Compose.md#secrets)
    - [Conclusão](Docker-Compose.md#Conclusão)
7. [Orchestrators](Orchestrators.md)

## Docker - Por quê?

Vamos supor que você desenvolva uma aplicação completa em seu computador. Após desenhar, desenvolver e testar sua aplicação, você resolve enviá-la para um amigo para que ele a use. 

Você então envia os arquivos, explica o modo de uso e ele segue o passo a passo a risca. Mas na hora em que ele inicia o aplicativo, ele não funciona. Você se pergunta "como foi que ela não funcionou se eu testei ela várias vezes e deu certo?". A resposta é simples: são ambientes diferentes.

Na hora de desenvolver sua aplicação, você usou certo sistema operacional, instalou certos programas e usou certos utensílios de desenvolvimento que nem sempre serão os mesmo (ou sequer estarão disponíveis) em outras máquinas. 

Logo, para que seu amigo use sua aplicação, é necessário que você encontre uma forma de garantir que o ambiente que ela precisa seja replicado em outros ambientes de execução. 

![Diagrama diferenciando técnicas de organização de serviços](https://www.netscaler.com/content/dam/netscaler/images/graphics/infographics/what-is-containerization.png)

Uma das soluções usadas foram as *Virtual Machines* (VMs): replicas dos sistemas operacionais que rodam dentro de outro sistema operacional, dividindo os recursos da máquina. Essa solução falha apenas no alto uso de recursos e na falta de garantia de dependências específicas do projeto. 

O Docker permitiu resolver esse problema a partir da **containerização de aplicações**. Essa estratégia consiste em isolar os arquivos de sistema e dependências do projeto em *containeres*: ambientes isolados de execução equipados com os arquivos necessários para o funcionamento dos serviços. É usado em DevOps (garantia de execução, eficiência e escalonabilidade de serviços).

[Próximo Tópico: Instalação](Instalação.md)

