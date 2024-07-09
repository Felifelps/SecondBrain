# Join

[Anterior: Funções de Agregação](Funções-de-Agregação.md)
<br>
[Próximo: Subconsultas](Subconsultas.md)

## Introdução

A cláusula `JOIN` é usada para combinar dados de várias tabelas a partir de um par de colunas correspondentes.

Um `JOIN` envolve três pontos principais:
- A *left table*
- A *right table*
- E as colunas relacionadas

Temos quatro tipos principais de `JOIN`: `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN` e `FULL OUTER JOIN`.

![Diagrama de JOINS](https://www.dofactory.com/img/sql/sql-joins.png)

Ainda há a possibilidade de se usar `JOIN` casos mais específicos, mas não abordarei por aqui.

Vamos entender na prática.

## INNER JOIN

Analise as tabelas abaixo.

Tabela Users
 user_id |  name   | idade
 ------- | ------- | ------
  1      | Marcos  |    26
  2      | Marcelo |    42
  3      | Carla   |    19
  4      | João    |    37

Tabela Orders
 order_id | customer_id |  product_name
 -------- | ----------- | ---------------
  1       |           2 | Arroz integral
  2       |           1 | Óleo de soja
  3       |             | Carne de Sol

> [!NOTE]
> Células vazias representam `null`. A terceira linha possui um valor `null` propositalmente.

Nesse exemplo, a coluna `customer_id`, da tabela `Orders` é uma *FOREIGN KEY*, e faz referência à coluna `user_id` da tabela `Users`.

Para relacionar os usuários às compras, a partir dessa relação, podemos usar um `INNER JOIN` para uní-las:

```sql
SELECT * 
FROM Orders /* Orders é a left table */
INNER JOIN Users /* Users é a right table */
ON Orders.customer_id = Users.user_id;  /* As colunas referenciadas */
```

O resultado da consulta será esse:

 order_id | customer_id |  product_name  | user_id |  name   | idade
 -------- | ----------- | -------------- | ------- | ------- | ------
  1       |           2 | Arroz integral |       2 | Marcelo |    42
  2       |           1 | Óleo de soja   |       1 | Marcos  |    26

O `INNER JOIN` acabou de "combinar" as colunas das duas tabelas, e devolveu os registros nos quais as colunas `customer_id` e `user_id` têm o mesmo valor.

Obeserve que a tabela `orders` é a *left table*, a `users` é a *right table* e `customer_id` e `user_id` são as colunas relacionadas.

## LEFT JOIN

Retorna o mesmo que o `INNER JOIN`, mais as demais linhas da *left table*.

Ex:

```sql
SELECT * 
FROM Orders 
LEFT JOIN Users
ON Orders.customer_id = Users.user_id;
```

Resultado:

| order_id | customer_id |  product_name  | user_id |  name   | idade |
| -------- | ----------- | -------------- | ------- | ------- | ----- |
|        1 |           2 | Arroz integral |       2 | Marcelo |    42 |
|        2 |           1 | Óleo de soja   |       1 | Marcos  |    26 |
|        3 |             | Carne de Sol   |         |         |       |

### RIGHT JOIN

Retorna o mesmo que o `INNER JOIN`, mais as demais linhas da *right table*.

Ex:

```sql
SELECT * 
FROM Orders 
RIGHT JOIN Users
ON Orders.customer_id = Users.user_id;
```

Resultado:

| order_id | customer_id |  product_name  | user_id |  name   | idade |
| -------- | ----------- | -------------- | ------- | ------- | ----- |
|        1 |           2 | Arroz integral |       2 | Marcelo |    42 |
|        2 |           1 | Óleo de soja   |       1 | Marcos  |    26 |
|          |             |                |       4 | João    |    37 |
|          |             |                |       3 | Carla   |    19 |

### FULL OUTER JOIN

Retorna todos os valores das duas tabelas, relacionando as duas.

Ex:

```sql
SELECT * 
FROM Orders 
FULL OUTER JOIN Users
ON Orders.customer_id = Users.user_id;
```

Resultado:

| order_id | customer_id |  product_name  | user_id |  name   | idade |
| -------- | ----------- | -------------- | ------- | ------- | ----- |
|        1 |           2 | Arroz integral |       2 | Marcelo |    42 |
|        2 |           1 | Óleo de soja   |       1 | Marcos  |    26 |
|        3 |             | Carne de Sol   |         |         |       |
|          |             |                |       4 | João    |    37 |
|          |             |                |       3 | Carla   |    19 |

## Conclusão

Como vimos, `JOINs` são muito úteis na construção de consultas, pois permitem a união dos dados de duas tabelas.

No próximo tópico, aprenderemos a aninhar consultas umas nas outras, gerando subconsultas.

[Anterior: Funções de Agregação](Funções-de-Agregação.md)
<br>
[Próximo: Subconsultas](Subconsultas.md)
