# Consultas

[Anterior: Normalização](Normalização.md)
<br>
[Próximo: Funções de agregação](Funções-de-Agregação.md)

## Introdução

Consultas são a principal forma de se conversar com o banco de dados. Aprender a realizar consultas corretamente auxilia em vários casos, como:

- ciência e análise de dados;
- correção de bugs;
- melhoria do database.

O comando usado para consultas em tabelas é o SELECT, portanto, aprenderemos todas as formas de se utilizar esse comando.

> Antes de começarmos, quero apresentar os comentários: linhas que não são executadas no código.
> Basta colocar o comentário entre `/*` e `*/`.
> Ex:
> ```sql
> /* 
> Essa linha não é executada pelo interpretador 
> Nem essa
> */
> SELECT essa linha é executada...
> FROM e vai dar erro
> ```

## SELECT

Como já vimos, a estrutura básica do SELECT é a seguinte:

```sql
SELECT coluna1, coluna2, ...
FROM nome_da_tabela;
```

Esse comando retornará os valores das colunas escolhidas da tabela especificada.

Caso queira retornar todas as colunas, use:

```sql
SELECT *
FROM nome_da_tabela;
```

## SELECT DISTINCT

Retorna apenas valores distintos, sem repetição.

```sql
SELECT DISTINCT column1, column2, ...
FROM table_name;
```

## WHERE

A cláusula WHERE pode ser usada nos comandos da DML para dar uma condição de execução ao comando. No caso da consulta, ele serve como filtro.

Ex: Selecionar todos os usuários com 18 anos ou mais

```sql
SELECT nome
FROM users
WHERE idade > 18;
```

Caso os valores sejam textos, use aspas simples (`'exemplo'`) para delimitá-los.

```sql
SELECT *
FROM users
WHERE nome = 'João';
```

### Operadores do where

 **Símbolo** | > | < | = | <> | >= | <= | BETWEEN | LIKE | IN | IS
 ----------- | - | - | - | -- | -- | -- | ------- | ---- | -- | --
 **Função**  | Maior que | Menor que | Igual a | Diferente de | Maior/igual a | Menor/Igual a | Entre dois valores | Se o texto obedece a um padrão | Se o valor está numa lista | Checa se é igual a uma constante (geralmente se é NULL)

## ORDER BY

Ordena o resultado de acordo com uma coluna específica.

Ex: Ordenar a tabela de alunos por ordem alfabética do nome (A-Z):

```sql
SELECT *
FROM alunos
ORDER BY nome ASC;
```

Ex2: Ordenar a tabela de notas entre 7 e 10 da maior nota para a menor (decrescente):

```sql
SELECT aluno, nota
FROM notas
WHERE nota BETWEEN 7 AND 10
ORDER BY nota DESC;
```

## Combinando e alterando condições

Para alterar logicamente as condições, podemos usar os operadores lógicos AND, OR e NOT:

### AND

Só é verdadeiro se todas as condições forem verdadeiras.

Ex: Buscar pessoas que sejam do sexo masculino **e** (and, em inglês) tenham mais de 21 anos.

```sql
SELECT *
FROM people
WHERE sexo = 'M' AND idade > 21;
```

### OR

Só é falso se todas as condições forem falsas.

Ex: Buscar pessoas de mais de 70 anos **ou** (or, em inglês) que sejam aposentadas.

```sql
SELECT *
FROM people
WHERE idade > 70 OR aposentado = TRUE; /* TRUE é verdadeiro */
```

### NOT

Troca o valor lógico da condição.

Ex: Buscar pessoas que **não** (not) tenham título de eleitor inválido.

```sql
SELECT *
FROM people
WHERE titulo_eleitor IS NOT NULL;
```

> **Um campo fica NULL quando não tem valor.**
> Você pode evitar que uma coluna tenha valores nulos adicionando o comando NOT NULL na criação da coluna. Ex:
> ```sql
>   ...
>   nome VARCHAR(250) NOT NULL,
>   ...
> ```

## LIMIT

Usado para limitar o número de linhas retornadas.

Ex: Retornar os três últimos clientes da loja.

```sql
SELECT *
FROM people
ORDER BY id DESC
LIMIT 3;

/*
Aqui invertemos a ordem para a decrescente com o ORDER BY,
e limitamos o resultado à três linhas.
*/
```

## Conclusão

Ainda há muito a se ver em relação às consultas. Vamos com tudo!

[Anterior: Normalização](Normalização.md)
<br>
[Próximo: Funções de agregação](Funções-de-Agregação.md)