# Docker Tutorial

[Início](/README.md)

#### **Partes do tutorial:**
1. [Instalação](Instalação.md)
    - [Introdução](Instalação.md#introdução)
    - [Mac](Instalação.md#mac)
    - [Linux](Instalação.md#linux)
    - [Windows](Instalação.md#windows)
    - [Conclusão](Instalação.md#conclusão)
2. [Container](Container.md)
    - [O que é um container?](Container.md#o-que-é-um-container)
    - [Criando containeres](Container.md#criando-containeres)
    - [Removendo containeres](Container.md#removendo-containeres)
    - [Gerenciando o fluxo de um container](Container.md#gerenciando-o-fluxo-de-um-container)
    - [Comandos](Container.md#comandos)
    - [Conclusão](Container.md#conclusão)
3. [Image](Image.md)
    - [O que é uma image?](Image.md#o-que-é-uma-image)
    - [Criação](Image.md#criação)
    - [Registry e Docker Hub](Image.md#registry-e-docker-hub)
    - [Boas práticas](Image.md#boas-práticas)
    - [Multi-staged builds](Image.md#multi-staged-builds)
    - [Comandos](Image.md#comandos)
    - [Conclusão](Image.md#conclusão)
4. [Volume](Volume.md)
    - [O que é um Volume?](Volume.md#o-que-é-um-volume)
    - [Exemplo sem volume](Volume.md#exemplo-sem-volume)
    - [Exemplo com volume](Volume.md#exemplo-com-volume)
    - [Mounting](Volume.md#mounting)
    - [Comandos](Volume.md#comandos)
    - [Conclusão](Volume.md#conclusão)
5. [Network ](Network.md)
    - [O que é uma network?](Network.md#o-que-é-uma-network)
    - [Criando networks](Network.md#criando-networks)
    - [Comandos](Network.md#comandos)
    - [Conclusão](Network.md#conclusão)
6. [Docker-Compose](Docker-Compose.md)
    - [O que é Docker Compose?](Docker-Compose.md#o-que-é-docker-compose)
    - [Criando um projeto compose](Docker-Compose.md#criando-um-projeto-compose)
    - [compose.yaml](Docker-Compose.md#composeyaml)
    - [Conclusão](Docker-Compose.md#conclusão)
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

