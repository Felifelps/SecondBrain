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
  customers.name,
  sub.product_name,
  MAX(sub.total) AS max 
FROM customers 
JOIN (
  SELECT
    customer,
    product_name,
    COUNT(*) AS total
  FROM orders
  GROUP BY customer, product_name
) as sub 
ON customers.id = sub.customer 
GROUP BY customers.name, sub.product_name 
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

Essa consulta enorme gera uma tabela que retorna o produto mais comprado por cada usuário, e o número de vezes que foi comprado. Vamos entender cada passo:

- Há duas subconsultas nessa consulta. Vamos olhar a primeira:
  ```sql
  (
    SELECT
      customer,
      product_name,
      COUNT(*) AS total
    FROM orders
    GROUP BY customer, product_name
  ) as sub
  ```
  Aqui, a consulta retorna o nome do cliente, o nome do produto e quantas vezes ele foi comprado por esse cliente.
  Ex: Cliente 1 | Produto 1 | 2
  A tabela é chamada de sub.

- A segunda subconsulta se refere ao parâmetro do LIMIT, que deve ser um único valor inteiro:
  ```sql
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
  Esta subconsulta tem outra subconsulta. A mais interna retorna todos os ids distintos da tabela orders.
  A externa conta quantas linhas a interna retorna. Nesse caso, isso é usado para limitar a 

[Anterior: Join](Join.md)
<br>
[Próximo: Views](Views.md)
