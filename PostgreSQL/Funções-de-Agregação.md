# Funções de agregação

[Anterior: Consultas](Consultas.md)
<br>
[Próximo: Where](Where.md)

## Introdução

Funções de agregação são funções embutidas do SQL que executam operações matemáticas sobre outros valores.

São usadas, geralmente, com a cláusula `GROUP BY`, que organiza o resultado em grupos de valores, cujas função de agregação geralmente retorna um valor para cada grupo.

As mais utilizadas são:

- MIN - pega o menor valor de um conjunto
- MAX - pega o maior valor de um conjunto
- COUNT - conta o número de valores
- SUM - retorna a soma dos valores
- AVG - retorna a média dos valores

## MIN e MAX

Retorna o menor e o maior valor, respectivamente, de uma coluna.

Ex:

```sql
SELECT 
    MIN(preco) AS menor_preco, 
    MAX(preco) AS maior_preco
FROM produtos;
```

Esse comando retornaria:

```
 menor_preco | maior_preco
-------------+-------------
 2.5         | 13.0
(1 linha)
```

### Com o GROUP BY

Com o GROUP BY, podemos ver qual o menor preço, por exemplo, para cada categoria de produto.

```sql
SELECT 
    MIN(preco) AS menor_preco, categoria
FROM produtos
GROUP BY categoria;
```

```
 categoria | menor_preco
-----------+-------------
 1         | 13.0
 2         | 1.52
(1 linha)
```

## COUNT

Retorna a quantidade de valores de uma coluna.

Ex:

```sql
SELECT COUNT(*), categoria
FROM produtos
GROUP BY categoria;
```

Esse código vê a quantidade de produtos (o * pega todas as colunas) por categoria.

> Se adicionar DISTINCT antes da coluna, você elimina duplicatas.
>
> Ex: `SELECT COUNT(DISTINCT categoria)`

## SUM e AVG

A SUM realiza a soma dos valores e a AVG realiza a média aritmética dos valores. Ambas só funcionam em colunas numéricas.

Ex:

```sql
SELECT SUM(preço * quantidade)
FROM vendas;
```

Neste comando estou calculando a soma do valor total (preço vezes quatidade) de cada venda.

```sql
SELECT AVG(salario)
FROM funcionarios;
```

Neste comando, meço a média de salários dos funcionários.

## Conclusão

Aqui vimos as principais funções de agregação do SQL. No próximo tópico veremos usos diferentes do WHERE.


[Anterior: Consultas](Consultas.md)
<br>
[Próximo: Where](Where.md)