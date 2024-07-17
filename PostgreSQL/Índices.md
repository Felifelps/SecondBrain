# Índices

[Anterior: Views](Views.md)
<br>
[Próximo: Transações e Currency](Transações-e-Currency.md)

## Introdução

Um índice serve para facilitar operações de busca numa tabela. Em geral, um índice organiza os registros de uma tabela de forma que, ao invés de buscar linha por linha por aquela condição, a instrução possa pesquisar pelos mais acessados, e, assim, ser mais eficiente.

Após a criação de um índices, o postgres fica responsável por atualizá-lo, caso a tabela seja modificada, e de decidir usá-lo ou não nas pesquisas.

Entretanto, o uso de índices possui suas desvantagens, como maior custo de processamento na criação dos mesmos e na modificação de tabelas. Além disso, ele apenas agiliza buscas que envolvam a coluna especificada e um valor constante.

Em resumo, use poucos índices e escolha bem as colunas que pretende usar.

## Criando e deletando um índice

Um índice se liga a uma coluna da tabela, facilitando buscas que a utilizem como parâmetro (WHERE, JOIN, ORDER BY). Para criar um índice, use:

```sql
CREATE INDEX nome_indice ON tabela (coluna);
```

Para excluir, use:

```sql
DROP INDEX nome_indice;
```

## Tipos

Para cada sitiação específica, há um tipo que possa ser usado. Para definir o tipo do índice, use:

```sql
CREATE INDEX nome ON tabela USING tipo (coluna);
```

### B-Tree

É o padrão. Trabalha bem com consultas com os seguintes operadores: >, <, =, <=, >=, BETWEEN, IN, IS (NOT) NULL. Além de ser usado com ORDER BY.

### HASH

Gera um hash de 32bits para cada coluna, facilitando assim operações com o operador =.

### GIST

Usado em colunas de tipos geométricos, busca por textos inteiros (full-text search), etc. 

### SP-GIST

Usado em colunas com tipos de dados como polígonos ou pontos.

### GIN

Trabalha com arrays e tipos com vários valores componentes. Também é usado em full-text search.

### BRIN

Trabalha com blocos físicos ordenados consecutivamente na tabela. Bom para tabelas grandes e ordenadas, como logs de tempo.

## Índices multicolunas

É possível criar índices passando várias colunas como parâmetro. Entretanto, dependendo do custo de execução das consultas, o postgres pode escolher analisar linha a linha ao invés do índice.

```sql
CREATE INDEX nome ON tabela (coluna1, coluna2);
```

## Unique Indexes

São índices que singularizam cada valor da coluna. Um unique index é criado quando geramos uma chave primária, por exemplo.

```sql
CREATE UNIQUE INDEX nome ON tabela (colunas...) [ NULLS [ NOT ] DISTINCT ];
```

Por padrão, ao gerar um unique index, cada NULL na tabela é considerado diferente, pois ele singulariza cada valor. Caso você use o NULLS NOT DISTINCT, ele considera todos os NULL iguais.

## Expression indexes

Caso sejam frequentes consultas numa tabela que usam determinada expressão, é possível criar um índice com uma expressão sql.

Por exemplo, imagine que, numa tabela `vendas`, seja comum dar descontos de 10% no atributo `valor` dos produtos. Podemos gerar um índice para essa operação:

```sql
CREATE INDEX idx_valor_desconto ON vendas ((valor * 0.9));
```

Agora, se executarmos `SELECT * FROM vendas WHERE (valor * 0.9) > 100;`, usaremos o índice criado.

## Partial indexes

Em suma, são índices com condições. São úteis, pois só indexam uma parte da tabela, diminuindo o custo de operação. Sem contar que facilitam consultas com a mesma condição do index.

```sql
CREATE INDEX idx_cliente_ativo ON clientes (nome) WHERE ativo IS TRUE;
```

## Conclusão

Não me aprofundei tanto em índices por que é um conteúdo específico e complexo. Vamos agora trabalhar com transações e currency.

[Anterior: Views](Views.md)
<br>
[Próximo: Transações e Currency](Transações-e-Currency.md)
