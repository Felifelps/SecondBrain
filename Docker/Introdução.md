# Introdução

[Base de estudo](https://docs.docker.com/get-started/)

Tutorial de Docker básico para iniciantes. Aqui tentei cobrir todos os conceitos e aspectos básicos para o uso dessa ferramenta.
#### **Tópicos ordenados:**
1. [Instalação](Instalação.md)
2. [Container](Container.md)
3. [Image](Image.md) 
4. [Volume](Volume.md)
5. [Network ](Network.md) (Imcompleto)
6. [Docker-Compose](Docker-Compose.md) (Imcompleto)
7. [Containerizando um app Python](Containerizando-um-app-Python.md) (Imcompleto)
8. [Orchestrators ](Orchestrators.md)(Imcompleto)
    - [Kubernetes](Kubernetes.md) (Imcompleto)
    - [Docker Swarm](Docker-Swarm.md) (Imcompleto)

# Docker - Por quê?

Vamos supor que você desenvolva uma aplicação completa em seu computador. Após desenhar, desenvolver e testar sua aplicação, você resolve enviá-la para um amigo para que ele a use. 

Você então envia os arquivos, explica o modo de uso e ele segue o passo a passo a risca. Mas na hora em que ele inicia o aplicativo, ele não funciona. Você se pergunta "como foi que ela não funcionou se eu testei ela várias vezes e deu certo?". A resposta é simples: são ambientes diferentes.

Na hora de desenvolver sua aplicação, você usou certo sistema operacional, instalou certos programas e usou certos utensílios de desenvolvimento que nem sempre serão os mesmo (ou sequer estarão disponíveis) em outras máquinas. 

Logo, para que seu amigo use sua aplicação, é necessário que você encontre uma forma de garantir que o ambiente que ela precisa seja replicado em outros ambientes de execução. 

![Diagrama diferenciando técnicas de organização de serviços](https://www.netscaler.com/content/dam/netscaler/images/graphics/infographics/what-is-containerization.png)

Uma das soluções usadas foram as *Virtual Machines* (VMs): replicas dos sistemas operacionais que rodam dentro de outro sistema operacional, dividindo os recursos da máquina. Essa solução falha apenas no alto uso de recursos e na falta de garantia de dependências específicas do projeto. 

O Docker permitiu resolver esse problema a partir da **containerização de aplicações**. Essa estratégia consiste em isolar os arquivos de sistema e dependências do projeto em *containeres*: ambientes isolados de execução equipados com os arquivos necessários para o funcionamento dos serviços. É usado em DevOps (garantia de execução, eficiência e escalonabilidade de serviços).

[Próximo Tópico: Instalação](Instalação.md)

