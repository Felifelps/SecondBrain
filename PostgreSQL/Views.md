# Views

[Anterior: Subconsultas](Subconsultas.md)
<br>
[Próximo: Índices](Índices.md)

## Introdução

Views são tabelas virtuais geradas a partir de consultas feitas em outras tabelas. A grande vantagem de se usar views é a capacidade de se armazenar consultas sempre atualizadas (a view é atualizada sempre que chamada).

É possível usar views dentro de views. Ainda é possível criar views materializadas e armazená-las no disco, permitindo maior segurança e controle.

Vamos aprender a criar e usar views para faciltar nossas consultas.

## Criando uma view

Para criar uma view, use a seguinte sintaxe:

```sql
CREATE VIEW nome AS
  sua consulta;
```

Tomando como base nosso exemplo de subconsultas:

```sql
/* Se o nome da view tiver mais de uma palavra
separadas por espaços, use aspas duplas*/
CREATE VIEW "Compras por cliente" AS
  SELECT 
    customers.name AS cliente,
    sub.product_name AS produto,
    sub.total AS total_de_compras
  FROM customers
  JOIN ( /* INNER JOIN na subconsulta */
    SELECT
      customer_id,
      product_name,
      COUNT(*) AS total
    FROM orders
    GROUP BY customer_id, product_name
  ) AS sub
  ON customers.id = sub.customer_id;
```

Caso queiramos acessar essa view, podemos utilizar:

```sql
SELECT * FROM "Compras por cliente";
```

Agora temos uma consulta armazenada numa view. 

## Alterando View

Para alterar uma view, use:

```sql
CREATE OR REPLACE VIEW name AS
  nova consulta;
```

Nesse caso, o comando altera a view, se ela existir. Caso contrário, cria uma nova.

## Deletando uma view

Use a seguinte sintaxe para deletar uma view:

```sql
DROP VIEW [IF EXISTS] view1, view2
[CASCADE];
```

Se você adicionar o IF EXISTS antes do nome da view, caso a view não exista, o comando é executado sem disparar erros.

Como se podem usar views sobre views, deletar uma view pode prejudicar outras. Com CASCADE, todas as views relacionadas a atual serão deletadas junto com ela. Caso não coloque, será exibido um erro.

## Materialized views

Como dito na introdução, materialized views são views armazenadas em disco, que se comportam como tabelas. Para criar um materialized view, use a sintaxe:

```sql
CREATE MATERIALIZED VIEW name
AS
  consulta
WITH [NO] DATA;
```

O WITH DATA faz com que seja possível consultar dados da query assim que criada. Caso adicione o NO, só será possível acessar os dados após dar um REFRESH na view.

## Refreshing materialized views

Para atualizar os dados de uma materialized view, use o seguinte comando:

```sql
REFRESH MATERIALIZED VIEW CONCURRENTLY name;
```

A instrução CONCURRENTLY não é obrigatória, mas é recomendada, visto que, sem ela, você perde o acesso às tabelas relacionadas a view durante o refresh.

## Deletando materialized views

Mesma lógica da view comum:

```sql
DROP MATERIALIZED VIEW name;
```

## Conclusão

Enfim, usar views facilita as consultas por permitir reutiliza-las das mais variadas formas. No próximo tópico, aprenderemos sobre índices.

[Anterior: Subconsultas](Subconsultas.md)
<br>
[Próximo: Índices](Índices.md)
