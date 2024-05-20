# Branch

[Anterior: Repositório](Repositório.md)
[Próximo: GitHub](GitHub.md)

Como sabemos, o Git conecta os commits uns aos outros para manter a ordem cronológica das alterações realizadas no projeto, criando assim uma árvore de commits. 

Esta árvore é dividida em *branches* (galho em inglês), que representam diferentes linhas cronológicas do projeto. Quando você cria um repositório, é criado também um branch padrão chamado `master`, que representa a linha central.

Sua utilização é mais fácil de entender a partir da imagem abaixo:

![Branch logic example](https://gitbookdown.dallasdatascience.com/img/git_branch_merge.png)
*Demonstração do uso de branches*

Como vemos na imagem, a partir do segundo commit feito no branch `master`, foi criado um novo branch chamado `new_feature`. Após a implementação da nova funcionalidade no novo branch, o usuário une o branch `new_feature` ao `master`, por meio de um `merge`. 

Assim, o branch principal apenas recebeu a funcionalidade pronta, sem ter que passar pelos estados intermediários. Isso é bom quando o branch principal é espelho para uma aplicação rodando e não pode ser alterado com frequência. Um branch permite atualizar a aplicação sem atrapalhar a que já está rodando.

Agora vamos à prática. Crie um novo branch chamado `dev` com o seguinte comando:

```bash
git branch dev
```

Agora, para ver todos os branches criados, rode:

```bash
git branch
```

Seu output deve ser esse:

```bash
$ git branch
  dev
* master
```

O `*` antes do branch `master` nos diz que estamos neste branch. Para trocar de branch, usamos o comando:

```bash
git checkout dev
```

> Caso queira criar um branch e trocar para ele de uma vez só, use `git checkout -b [nome-do-novo-branch]`

Deve aparecer a mensagem `Switched to branch 'dev'` após o comando. Caso queira confirmar, basta usar o `git branch` para ver o asterisco antes do nome `dev`.

Agora observe o seu repositório: houve alguma mudança? Não? Exato. Quando criamos um novo branch, geramos uma cópia do branch original. 

Agora faremos as alterações que quisermos. Crie um novo arquivo chamado `file2.txt` e escreva qualquer coisa nele. Agora, adicione tudo ao `index`, e faça um commit. 

Agora, os dois branches são diferentes. Embora o branch `dev` derive do `master`, modificamos o `dev`ao adicionar um novo arquivo. Para confirmar isto, basta trocar para o branch `master`:

```bash
git checkout master
```

Olhe seu diretório: **o arquivo `file2.txt` não está lá.** São dois branches diferentes agora. Mas vamos uní-los a partir de um merge.

## Merging

Fazer merge significa "incorporar as alterações de um branch específico no branch atual". No caso do nosso exemplo, queremos incorporar as atualizações feitas no branch `dev` no branch `master`. Para isso, entre no `master`:

```bash
git checkout master
```

E rode o seguinte comando:

```bash
git merge dev
```

E pronto!! Agora o arquivo `file2.txt` foi incorporado ao `master`. Como já incorporamos a atualização, é uma boa prática excluir o branch `dev` para simplificar o workflow do projeto.

![Workflow do repositório de exemplo](img/branch-example.png)
*Representação do exemplo feito*

## Merge conflicts

Às vezes ocorrem conflitos em merges: problemas na hora de unir arquivos diferentes nos dois branches. Eles ocorrem quando alteramos um arquivo num branch e o incorporamos no outro, de forma que o Git não sabe qual alteração deixar: a original ou a nova.

Por exemplo, imagine que você tem um arquivo `main.txt` no branch `master`:

```
Conteúdo do arquivo
```

Então você cria outro branch, `dev`, e altera o arquivo, pra ficar dessa forma:

```
Conteúdo do arquivo
Linha adicionada no dev
```

E no branch master você faz mais um commit, alterando o `main.txt`:

```
Conteúdo do arquivo
Linha adicionada no master
```

Ao tentar fazer merge, teremos um merge conflict, pois ocorreram duas atualizações diferentes nos dois branches e o Git não consegue determinar qual é a correta.

Para resolver, temos que, manualmente, decidir qual será a atualização desejada. Ao abrir o arquivo `main.txt` no branch `master`, teremos esse texto:

```
Conteúdo do branch
<<<<<<< HEAD
Linha adicionada no master
=======
Linha adicionada no dev
>>>>>>> dev
```

Neste exemplo:
- a partir de `<<<<<<< HEAD` até `=======`, temos a parte do arquivo alterada no branch atual (`master`, nesse caso)
- do `=======` até `>>>>>>> dev`, temos a parte alterada no branch de merge (`dev`). 

Para resolver esse conflito, você deve atualizar o arquivo da forma que você deseja (uma das duas, as duas ou nenhuma, você escolhe). 

Digamos que o correto seriam as duas alterações juntas. Então, alteraríamos o arquivo para que ele ficasse assim:

```
Conteúdo do arquivo
Linha adicionada no master
Linha adicionada no dev
```

Após corrigir as alterações, basta adicioná-las ao `index` (com `git add main.txt`) e rodar o seguinte comando:

```bash
git merge --continue
```

> Dependendo da situação do merge, usar `git commit` também funciona.

Pronto!! Os conflitos foram corrigidos e o merge será finalizado. 

## Conclusão

Acabamos com branches, mas, após os links, temos alguns comandos interessantes de se conhecer ao usar branches. Dê uma olhadinha antes de ir para o próximo tópico.

[Anterior: Repositório](Repositório.md)
[Próximo: GitHub](GitHub.md)

## Comandos
- `git branch`: Lista todos os branches presentes no repositório local.
- `git branch nome_do_branch`: Cria um novo branch com o nome especificado.
- `git checkout nome_do_branch`: Alterna para o branch especificado.
- `git checkout -b nome_do_branch`: Cria um novo branch com o nome especificado e alterna para ele em um único comando.
- `git merge nome_do_branch`: Mescla as alterações do branch especificado para o branch atual.
- `git branch -d nome_do_branch`: Exclui o branch especificado (apenas se as alterações do branch já foram incorporadas em outro lugar).
- `git branch -D nome_do_branch`: Força a exclusão do branch especificado, mesmo se as alterações não tiverem sido mescladas.
- `git branch -m nome_novo_do_branch`: Renomeia o branch atual para o nome especificado.