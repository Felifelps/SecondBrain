# Subconsultas

[Anterior: Join](Join.md)
<br>
[Próximo: Views](Views.md)

## Introdução

Subconsultas, em suma, são consultas feitas sobre consultas. SELECT sobre SELECT. É possível aninhar até 255 consultas por vez.

Subconsultas têm várias utilidades, como servir de condição para clásulas WHERE ou HAVING, principalmente com funções de agregação, ou até como fonte de dados para outras consultas. Enfim, vamos entender melhor na prática.

## Subconsultas como condição

Analise o seguinte exemplo:

```sql
SELECT nome_produto, preco
FROM produtos
WHERE preco > (
  SELECT AVG(preco) FROM produtos
);
```

Nesse exemplo, usamos uma subconsulta para retornar a média de preço da tabela. Assim, podemos retornar apenas os produtos cujo preço está acima da média.

Agora um exemplo com GROUP BY e HAVING:

```sql
SELECT genero, SUM(n_emprestimos) AS emprestimos_totais
FROM livros
GROUP BY genero
HAVING emprestimos_totais > (
  SELECT AVG(SUM(n_emprestimos))
  FROM livros
  GROUP BY genero
);
```

> [!TIP]
> Para analisar subconsultas, vá da mais interna à mais externa.

Nesse exemplo, a subconsulta retorna a média da soma dos emrpréstimos dos livros de cada gênero. Assim, a consulta mais externa pode retornar o total de empréstimos por gênero, cujo total de empréstimos seja maior que a média de total de empréstimos.

## Subconsultas com FROM e JOIN

Além de servirem como condição, subconsultas podem ser usadas com o FROM para permitir que seu retorno seja lido por consultas superiores.

```sql
SELECT
  p.categoria,
  SUM(sub.total_vendido) AS total_vendido
FROM
  produtos AS p
JOIN (
  SELECT
    produto_id,
    SUM(quantidade) AS total_vendido
  FROM vendas
  GROUP BY produto_id
) AS sub
ON p.produto_id = sub.produto_id
GROUP BY p.categoria;
```

Este exemplo usa um JOIN para unir as duas consultas. Vamos entendê-lo melhor:
- A subconsulta (sub) retorna uma tabela relacionando o id de cada produto ao seu número total de vendas (obtido pela soma da quantidade vendida em cada venda).
- A consulta externa relaciona as categorias dos produtos com o total vendido por categoria (obtido com a soma do total de vendas de cada produto da categoria).

```sql
SELECT
  users.name,
  sub.product_name,
  MAX(sub.total) AS max 
FROM users 
JOIN (
  SELECT
    customer,
    product_name,
    COUNT(*) AS total
  FROM orders
  GROUP BY customer, product_name
) as sub 
ON users.id = sub.customer 
GROUP BY users.name, sub.product_name 
ORDER BY max DESC 
LIMIT (
  SELECT
    COUNT(customer)
  FROM (
    SELECT DISTINCT customer
    FROM orders
    GROUP BY customer
    HAVING customer IS NOT NULL
  )
);
```

[Anterior: Join](Join.md)
<br>
[Próximo: Views](Views.md)
