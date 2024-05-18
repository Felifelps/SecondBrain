# Repositório

[Anterior: Instalação](Instalação.md)
[Próximo: Branch](Branch.md)

Repositórios é um espaço, ou diretório, onde os arquivos do projeto são armazenados e gerenciados. Para iniciar um repositório, crie uma pasta chamada `MyRepo`, abra o terminal ou o Git Bash nela, e rode o seguinte comando:

```bash
git init
```

Seu output deve ser parecido com esse:

```bash
$ git init
Initialized empty Git repository in [local-do-seu-repo]
```

Esse comando transforma a pasta em que você está num repositório Git por meio da pasta (oculta) `.git` que é criada no local.

Agora vamos aos trabalhos. Abra a pasta que você criou, e crie um arquivo de texto chamado `file.txt`. Escreva qualquer coisa nele. Agora, rode o seguinte comando:

```bash
git add file.txt
```

O que acabamos de fazer? Você adicionou o arquivo `file.txt` ao "índice" do Git, ou `index`. Calma que já vamos entender. Agora, rode o seguinte comando:

```bash
git commit -m "file.txt criado"
```

Seu output deve ser parecido com esse:

```bash
$ git commit -m "file.txt criado"
[master (root-commit) bfecb2a] file.txt criado
 1 file changed, 1 insertion(+)
 create mode 100644 file.txt
```

Certo, o que aconteceu aqui? Bem, vamos entender:
- ao criar o arquivo `file.txt`, alteramos nosso repositório;
- como queremos que o Git mantenha controle sobre as alterações, adicionamos o `file.txt` ao `index` Git, o responsável por preparar as alterações para que possamos salvá-las;
- com o comando `git commit`, salvamos as alterações do `index` em um commit object chamado "file.txt criado".

Vamos entender mais a fundo.

## Index e git add

Para que o git possa armazenar as alterações realizadas no repositório, é necessário que você declare explicitamente quais alterações ele deve salvar. 

Isso é feito a partir do comando `git add`, como visto acima. Esse comando leva as alterações  especificadas para o `index` git, garantindo que sejam incluidas no próximo commit.

O `git add` recebe arquivos e diretórios como argumento. Caso você queira adicionar todo o repositório no `index`, basta usar um `.` de argumento:

```bash
git add .
```

Basicamente, há três formas de alteração que são salvas no index:
- `create mode`: vista no exemplo acima, criada quando um arquivo é criado;
- `delete mode`: quando um arquivo é deletado;
- `file changed`: quando o conteúdo de um arquivo é alterado, podendo haver inserções (`insertions`) e remoções (`deletion`).

Essas mensagens são exibidas quando fazemos um commit.

## Commits

Commits são como fotos (snapshots) tiradas do repositório em um determinado momento. Elas armazenam exatamente como todos os arquivos do repositório estavam naquele momento, e permitem manter controle da história do projeto, bem como regressar ao commit caso seja desejado.

Todos os commits possuem algumas informações salvas num commit object:
- **autor e data**;
- **hash**: id hexadecimal usado para diferenciar o commit dos demais;
- **mensagem do commit**: usada para esclarecer as alterações salvas no commit;
- **link para o commit anterior**: mantém a cronologia dos commits.

Como visto no exemplo acima, após adicionar as alterações no `index`, podemos criar um commit com o seguinte comando:

```bash
git commit -m "[mensagem-do-commit]"
```

> É uma boa prática sempre escrever mensagens objetivas em seus commits, para facilitar o entendimento do commit.

## Reseting

A melhor funcionalidade dos commits (opinião do autor) é a possibilidade de voltar o repositório para o estado salvo num commit, vulgo dar um reset.

Vamos fazer um exemplo. No mesmo diretório do exemplo anterior, remova o arquivo `file.txt`, adicione as alterações ao `index`, e salve um commit com a mensagem: `deleted file.txt`.

Digamos que você lembrou que havia algo importante nesse arquivo e precisa recuperá-lo, mas você acabou de deletar esse arquivo. 

Não se preocupe! Talvez haja algum commit no qual o `file.txt` esteja salvo. Para ver os commits realizados, use o seguinte comando:

```bash
git log --oneline
```

> O argumento `--oneline` serve para resumir os detalhes do commit a uma única linha. Sem ele, haveria muita informação exibiad o e isso dificultaria a busca pelo commit. 
> Caso queira sair do log, basta apertar a tecla `q`.

Seu output deve ser parecido com esse:

``` bash
$ git log --oneline
[hash-do-commit-2] (HEAD -> master) deleted file.txt
[hash-do-commit-1] file.txt criado
```

Analise que o primeiro commit exibido possui, após seu hash, um parênteses com o texto `(HEAD -> master)`. A `HEAD` é o ponteiro do Git, e sempre aponta para o commit atual. O `master` é o [branch](Branch.md) atual, mas isso será tratado no próximo tópico.

Nesse caso, o commit atual é o último que fizemos. Mas queremos voltar para o primeiro commit. Para isso, utilizaremos o comando abaixo, passando o hash do primeiro commit como argumento:

```bash
git reset --hard [hash-do-commit-1]
```

Pronto! A opção `--hard` desfaz os commits intermediários e volta todos os arquivos do repositório para o estado que estavam no commit especificado. Nesse caso, quando fizemos o commit, o arquivo `file.txt` ainda existia. 

Você pode checar a localização do `HEAD` com o `git log --oneline`. Você verá que o commit onde deletamos `file.txt` foi excluído, e que o `HEAD` aponta para o primeiro commit que fizemos.

## Conclusão

Aprendemos um pouco do básico do git, mas ainda não terminamos. Ainda temos alguns conceitos fundamentais para trabalhar acerca dessa ferramenta. O próximo será Branch. Vamos com tudo!

[[Anterior: Instalação](Instalação.md)](Repositório.md)
[Próximo: Branch](Branch.md)
