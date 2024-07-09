# Instalação

## Introdução

Antes de tudo, é necessário entender que tudo envolvido com o gerenciamento de containeres é executado pela Docker Engine: a tecnologia que roda por baixo dos panos e que permite que tudo isso aconteça.

A Docker Engine funciona como uma aplicação cliente-servidor, possuindo os seguintes recursos:
- Um servidor com uma daemon contínua (*dockerd*)
- Uma API para permitir acesso ao servidor por meio de programas
- Uma *Command Line Interface* (CLI) como cliente do servidor, permitindo executar comando via terminal.

Além da Docker Engine, temos vários outros produtos Docker, e o Docker Desktop: uma aplicação multiplataforma que, além de compactar a instalação dos demais componentes, dispõe de interface gráfica.

Para este tutorial, instalaremos o Docker Desktop para incluir os demais componentes. Usaremos mais a CLI.

## Mac

Siga as instruções dispostas [neste link.](https://docs.docker.com/desktop/install/mac-install/)

## Linux

Siga as instruções dispostas [neste link.](https://docs.docker.com/desktop/install/linux-install/). 

> [!TIP]
> A Docker Engine pode ser instalada diretamente no Linux.

## Windows

No Windows, é necessário instalar o WSL (Windows Subsystem Linux) primeiro (requer windows 10 ou 11). Há duas formas de se instalar em sua máquina.

### Microsoft Store

Para instalar via microsoft store, siga os seguintes passos:

1. Abra a pesquisa do Windows e procure por "Ativar ou desativar recursos do Windows
2. Procure por "Subsistema do Windows para Linux"
3. Ative e clique em "Ok"
4. Agora, abra a microsoft store
5. Pesquise por sua distribuição favorita (ex: ubuntu)
6. Instale, execute e crie um usuário e uma senha (não perca)

### Powershell

Abra o powershell como administrador e rode o seguinte comando:

```powershell
wsl --install
```

Aguarde a instalação e reinicie o computador. A distribuição instalada será Ubuntu (pode ser outra). 

### Docker Desktop

Por fim, termine de instalá-lo [por aqui](https://docs.docker.com/desktop/install/windows-install/).

## Conclusão

Agora que o instalamos, vamos aprender os conceitos principais para se trabalhar com Docker.

[Anterior: Introdução](README.md)
<br>
[Próximo: Container](Container.md)
