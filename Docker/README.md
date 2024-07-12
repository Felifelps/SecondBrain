# Docker Tutorial

[Início](/README.md)

#### **Partes do tutorial:**
1. [Instalação](Instalação.md)
<br> ├── [Introdução](Instalação.md#Introdução)
<br> ├── [Mac](Instalação.md#Mac)
<br> ├── [Linux](Instalação.md#Linux)
<br> ├── [Windows](Instalação.md#Windows)
<br> ├── [Microsoft Store](Instalação.md#Microsoft%20Store)
<br> ├── [Powershell](Instalação.md#Powershell)
<br> ├── [Docker Desktop](Instalação.md#Docker%20Desktop)
<br> ├── [Conclusão](Instalação.md#Conclusão)
2. [Container](Container.md)
<br> ├── [O que é um container?](Container.md#O%20que%20é%20um%20container?)
<br> ├── [Criando containeres](Container.md#Criando%20containeres)
<br> ├── [Rodando em segundo plano](Container.md#Rodando%20em%20segundo%20plano)
<br> ├── [Removendo containeres](Container.md#Removendo%20containeres)
<br> ├── [Gerenciando o fluxo de um container](Container.md#Gerenciando%20o%20fluxo%20de%20um%20container)
<br> ├── [Comandos](Container.md#Comandos)
<br> ├── [Conclusão](Container.md#Conclusão)
3. [Image](Image.md)
<br> ├── [O que é uma image?](Image.md#O%20que%20é%20uma%20image?)
<br> ├── [Criação](Image.md#Criação)
<br> ├── [Rodando um container a partir da image](Image.md#Rodando%20um%20container%20a%20partir%20da%20image)
<br> ├── [Registry e Docker Hub](Image.md#Registry%20e%20Docker%20Hub)
<br> ├── [Boas práticas](Image.md#Boas%20práticas)
<br> ├── [Cache mount](Image.md#Cache%20mount)
<br> ├── [Bind mounts](Image.md#Bind%20mounts)
<br> ├── [.dockerignore](Image.md#.dockerignore)
<br> ├── [Multi-staged builds](Image.md#Multi-staged%20builds)
<br> ├── [Comandos](Image.md#Comandos)
<br> ├── [Conclusão](Image.md#Conclusão) 
4. [Volume](Volume.md)
<br> ├── [O que é um Volume?](Volume.md#O%20que%20é%20um%20Volume?)
<br> ├── [Mounting](Volume.md#Mounting)
<br> ├── [Exemplo sem volume](Volume.md#Exemplo%20sem%20volume)
<br> ├── [Exemplo com volume](Volume.md#Exemplo%20com%20volume)
<br> ├── [Mounting](Volume.md#Mounting)
<br> ├── [Volume Mount](Volume.md#Volume%20Mount)
<br> ├── [Bind Mount](Volume.md#Bind%20Mount)
<br> ├── [Temporary Mount](Volume.md#Temporary%20Mount)
<br> ├── [Comandos](Volume.md#Comandos)
<br> ├── [Conclusão](Volume.md#Conclusão)
5. [Network ](Network.md)
<br> ├── [O que é uma network?](Network.md#O%20que%20é%20uma%20network?)
<br> ├── [Criando networks](Network.md#Criando%20networks)
<br> ├── [Entendendo o exemplo](Network.md#Entendendo%20o%20exemplo)
<br> ├── [Comandos](Network.md#Comandos)
<br> ├── [Conclusão](Network.md#Conclusão)
6. [Docker-Compose](Docker-Compose.md)
<br> ├── [O que é Docker Compose?](Docker-Compose.md#O%20que%20é%20Docker%20Compose?)
<br> ├── [Criando um projeto compose](Docker-Compose.md#Criando%20um%20projeto%20compose)
<br> ├── [Entendendo o exemplo](Docker-Compose.md#Entendendo%20o%20exemplo)
<br> ├── [compose.yaml](Docker-Compose.md#compose.yaml)
<br> ├── [version and name](Docker-Compose.md#version%20and%20name)
<br> ├── [services](Docker-Compose.md#services)
<br> ├── [Configurações de um service](Docker-Compose.md#Configurações%20de%20um%20service)
<br> ├── [networks](Docker-Compose.md#networks)
<br> ├── [volumes](Docker-Compose.md#volumes)
<br> ├── [config](Docker-Compose.md#config)
<br> ├── [secrets](Docker-Compose.md#secrets)
<br> ├── [Conclusão](Docker-Compose.md#Conclusão)
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

