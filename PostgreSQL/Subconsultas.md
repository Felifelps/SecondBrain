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
	costumers.name AS cliente,
	sub.product_name AS produto,
	sub.total AS total_de_compras
FROM costumers
JOIN ( /* INNER JOIN na subconsulta */
	SELECT
		customer_id,
		product_name,
	COUNT(*) AS total
	FROM orders
	GROUP BY customer_id, product_name
) AS sub
ON costumers.id = sub.customer_id;
```

Essa consulta gera uma tabela que mostra quantas vezes cada usuário comprou cada produto. Vamos entender cada passo:

- Para entender melhor, comecemos de dentro para fora, analisando a subconsulta abaixo:
  ```sql
	(
		SELECT
			customer_id,
			product_name,
		COUNT(*) AS total
		FROM orders
		GROUP BY customer_id, product_name
	) AS sub
  ```
  Aqui, a consulta busca na tabela orders e usa um GROUP BY para associar o id do cliente (customer_id) e o nome do produto (product_name) ao número de vezes que ele foi comprado (COUNT(*) AS total).
  Ex: Cliente_id | Nome do Produto | Total
  Para pordermos acessá-la, ela é chamada de sub.

- A consulta externa
	```sql
	SELECT 
		costumers.name AS cliente,
		sub.product_name AS produto,
		sub.total AS total_de_compras
	FROM costumers
	JOIN (
		/* ... */
	) AS sub
	ON costumers.id = sub.customer_id;
	```


[Anterior: Join](Join.md)
<br>
[Próximo: Views](Views.md)
