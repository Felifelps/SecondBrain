# SQL Básico Parte 2

[Anterior: SQL Básico](SQL-Básico.md)
<br>
[Próximo: Estruturando](Estruturando.md)

## DML (Data Manupulation Language)

A DML inclui comandos relacionados à manipulação de registros (linhas) das tabelas. Como no tópico anterior, vamos aprender os principais comandos na prática.

## SELECT

O `SELECT`, como já vimos, tem como função selecionar determinados dados de uma ou mais tabelas. Por enquanto, veremos apenas consultas simples. 

Para praticarmos, crie uma nova tabela:

```sql
CREATE TABLE users (
    username VARCHAR(255),
    email VARCHAR(255),
    followers INT
);
```

Para selecionar certas colunas da tabela, basta especificá-las no comando:

```sql
SELECT username, email FROM users;
```

Caso queira selecionar apenas a coluna `email`, use:

```sql
SELECT email FROM users;
```

Como ainda não temos nenhum registro, apenas vimos tabelas vazias. Vamos criar alguns usuários.

## INSERT INTO

Para inserir registros (linhas) numa tabela, usamos o comando `INSERT INTO`. Vamos criar alguns usuários:

```sql
INSERT INTO users (username, email, followers) 
VALUES 
    ('João', 'joão@email.com', 45),
    ('Maria', 'maria@email.com', 0),
    ('Marcelo', 'marcelo@email.com', 1);
```

Caso queira ver os registros, use um `SELECT` para ver as linhas adicionadas.

> [!WARNING]
> Como se pode ver acima, **ao adicionar textos (para VARCHARs por exemplo), devemos colocá-los entre aspas simples ('')!**

## WHERE

A cláusula `WHERE` tem o poder de filtrar as colunas que o comando usado vai acessar.

Ele faz isso a partir de uma condição. Rode o seguinte:

```sql
SELECT *
FROM users
WHERE followers > 5;
```

Seu output será apenas aquelas colunas nas quais o valor followers é maior que 50:

```
 username |     email      | followers
----------+----------------+-----------
 João     | joão@email.com |        45 
(1 linha)
```

A cláusula `WHERE` pode ser utilizada em vários contextos. Veremos [melhor aqui](Consultas.md).

## UPDATE

Digamos que Maria tenha ganhado alguns seguidores e precisemos editar a tabela para adicioná-los. Podemos usar o seguinte comando para isso:

```sql
UPDATE users
SET followers = 5
WHERE username = 'Maria';
```
Observe a mudança com o `SELECT`.

> [!WARNING]
> Se você rodar o update sem o `WHERE`, todas as linhas serão alteradas.

## DELETE

Agora, digamos que Marcelo tenha excluído sua conta de usuário. Não é mais necessário que eu tenha dados sobre essa conta em minha tabela, portanto, vamos removê-la:

```sql
DELETE FROM users
WHERE username = "Marcelo";
```

E pronto! Deletamos a conta de Marcelo!!

> [!WARNING]
> Se você omitir o `WHERE` num `DELETE`, você excluirá todas as linhas!!

## Conclusão

Muita coisa, mas é importante. Agora veremos sobre a estruturação de bancos de dados.

[Anterior: SQL Básico](SQL-Básico.md)
<br>
[Próximo: Estruturando](Estruturando.md)
