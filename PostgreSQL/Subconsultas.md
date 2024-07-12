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
> As consultas são executadas da mais interna à mais externa. Portanto, para entendê-las, é preciso seguir o mesmo raciocínio.

Nesse exemplo, a subconsulta retorna a média da soma dos emrpréstimos dos livros de cada gênero. Assim, a consulta mais externa pode retornar o total de empréstimos por gênero, cujo total de empréstimos seja maior que a média de total de empréstimos.

## Subconsultas com FROM

Além de servirem como condição, subconsultas podem ser usadas como tabelas para permitir que seu retorno seja lido por consultas superiores.

Neste exemplo, usamos um FROM para usar os resultados da subconsulta como base para a primeira.

```sql
SELECT 
  sub.*  /* sub.* = Todas as colunas da subconsulta */
FROM (
  SELECT
    customer_id,
    product_name,
    COUNT(*) AS total
  FROM orders
  GROUP BY customer_id, product_name
) AS sub;
```

A subconsulta acessa a tabela orders e executa um GROUP BY para associar o id do cliente (customer_id) e o nome do produto (product_name) ao número de vezes que ele foi comprado (COUNT(*) AS total).

A consulta externa apenas exibe todos os valores da interna.

Ex: Cliente_id | Nome do Produto | Total

## Subconsultas com JOIN

É possível melhorar a consulta anterior adicionando o nome do usuário na consulta. Como a tabela orders não tem esse dado, podemos fazer um JOIN com a customers.

Nesse exemplo, fazemos um INNER JOIN para pegar o nome do cliente e associá-lo com seu id, disponível na subconsulta.

```sql
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

## Conclusão

Subconsultas são muito úteis em consultas mais complexas, pois permite combinar várias condições diferentes num único código. No próximo tópico, melhoraremos ainda mais nossas consultas com views.

[Anterior: Join](Join.md)
<br>
[Próximo: Views](Views.md)
