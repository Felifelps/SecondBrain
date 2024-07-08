# Join

[Anterior: Funções de Agregação](Funções-de-Agregação.md)
<br>
[Próximo: Subconsultas](Subconsultas.md)

## Introdução

A cláusula `JOIN` é usada para combinar dados de várias tabelas a partir de uma coluna.

Existem vários tipos de `JOIN`, cada um com sua utilidade. É mais fácil de entender na prática.

## Exemplo

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

Nesse exemplo, a coluna `customer_id`, da tabela `Orders`, equivale (é uma *FOREIGN KEY*) à coluna `user_id` da tabela `Users`.

Para relacionar os usuários às compras, podemos usar um `INNER JOIN` para uní-las:

```sql
SELECT * 
FROM Orders 
INNER JOIN Users
ON Orders.customer_id = Users.user_id;
```

O resultado da consulta será esse:

 order_id | customer_id |  product_name  | user_id |  name   | idade
 -------- | ----------- | -------------- | ------- | ------- | ------
  1       |           2 | Arroz integral |       2 | Marcelo |    42
  2       |           1 | Óleo de soja   |       1 | Marcos  |    26

## Entendendo o exemplo

O `INNER JOIN` acabou de "combinar" as colunas das duas tabelas, e devolveu os registros nso quais as colunas `customer_id` e `user_id` têm o mesmo valor.

Se combinarmos isso aos aliases e especificarmos as colunas, podemos gerar consultas precisas e interessantes.

Caso queiramos saber que usuário comprou tal produto, podemos realizar a seguinte consulta:

```sql
SELECT
  Users.name AS Usuario,
  Orders.product_name AS Produto
FROM Orders
INNER JOIN Users 
ON Orders.customer_id = Users.user_id;
```

Assim, teremos o resultado:

 Usuario   |    Produto
---------- | ---------------
 Marcelo   | Arroz integral
 Marcos    | Óleo de soja

## Tipos de JOIN

Como vimos, o `JOIN` envolve alguns pontos principais:
- A primeira tabela, chamada de *left table*
- A segunda tabela, chamada de *right table*
- As colunas que vamos relacionar

Temos quatro tipos principais de `JOIN`:
- `INNER JOIN`: retorna todas as linhas que se correspondem nas duas tabelas;
- `LEFT JOIN`: retorna as linahs do `INNER JOIN`, mais todos os registros da *left table*
- `RIGHT JOIN`: retorna as linahs do `INNER JOIN`, mais todos os registros da *right table*
- `FULL OUTER JOIN`: retorna tudo de todos.

![Diagrama de JOINS](https://learnsql.com.br/blog/como-aprender-sql-joins/2.png)

Ainda há a possibilidade de se usar `JOIN` casos mais específicos, mas não abordarei por aqui.

## Exemplos novamente

Ainda usando as tabelas `Users` e `Orders`, vamos exemplificar os tipos apresentados:

### LEFT JOIN

Consulta: 

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

Retornamos as linhas coincidentes e as linhas de `orders` (nossa *left table*).

### RIGHT JOIN

Consulta: 

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

Todos os valores do `INNER JOIN` mais os valores de `users`.

### FULL OUTER JOIN

Consulta: 

```sql
SELECT * 
FROM Orders 
FULL OUTER JOIN JOIN Users
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

Todos os valores das duas tabelas, relacionando as tabelas.

## Conclusão

Como vimos, `JOINs` são muito úteis na construção de consultas, pois permitem a união dos dados de duas tabelas.

No próximo tópico, aprenderemos a aninhar consultas umas nas outras, gerando subconsultas.

[Anterior: Funções de Agregação](Funções-de-Agregação.md)
<br>
[Próximo: Subconsultas](Subconsultas.md)
