# Índices

[Anterior: Views](Views.md)
<br>
[Próximo: Transações e Currency](Transações-e-Currency.md)

## Introdução

Um índice serve para facilitar operações de busca numa tabela. Em geral, um índice organiza os registros de uma tabela de forma que, ao invés de buscar linha por linha por aquela condição, a instrução possa pesquisar pelos mais acessados, e, assim, ser mais eficiente.

Após a criação de um índices, o postgres fica responsável por atualizá-lo, caso a tabela seja modificada, e de decidir usá-lo ou não nas pesquisas.

Entretanto, o uso de índices possui suas desvantagens, como maior custo de processamento na criação dos mesmos e na modificação de tabelas.

Em resumo, use poucos índices e escolha bem as colunas que pretende usar.

## Criando um índice

Um índice se liga a uma coluna da tabela, facilitando buscas que a utilizem como parâmetro. Para criar um índice, use:

```sql
CREATE INDEX nome_indice ON tabela (coluna);
```



[Anterior: Views](Views.md)
<br>
[Próximo: Transações e Currency](Transações-e-Currency.md)
