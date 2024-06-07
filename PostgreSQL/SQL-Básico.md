# SQL Básico

[Anterior: Configurando](Configurando.md)
[Próximo: Estruturando](Estruturando.md)

## Introdução

A *Structured Query Language*, vulgo SQL, é uma linguagem padrão que usada para a manipulação de tabelas de bancos de dados. Dentre suas utilidades, temos:

- criação, atualização e exclusão de tabelas;
- inserção, atualização e remoção de registros;
- chaves de tabela (relações entre tabelas);
- consulta de dados avançada;
- controle de acesso.

## Sublinguagens

De acordo com sua utilidade, os comandos SQL são agrupados em quatro principais sublinguagens:

- **DDL (Data Definition Language)**: manipulação de tabelas;
- **DML (Data Manipulation Language)**: manipulação de registros;
- **DCL (Data Control Language)**: controle de acesso aos dados;
- **TCL (Transaction Control Language)**: controle de transações.

> [!TIP]
> Alguns adicionam também a *Data Query Language* (DQL), voltada apenas para consultas (nesse caso, ela faz parte da DML).

Neste tópico vamos tratar o essencial da DDL e DML.

## DDL (Data Definition Language)

Os comandos da DDL são voltados para a criação, manipulação e exclusão de tabelas no banco de dados. A melhor forma de aprender, é na prática.

### CREATE TABLE

Conecte-se ao SQL Shell, como feito no [tópico anterior](Configurando.md#sqlshell), e rode o seguinte código (basta copiar, colar no SQL Shell e apertar enter):

```sql
CREATE TABLE client (
     nome VARCHAR(255),
     idade INT
);
```

Seu terminal deve estar dessa forma:

```
postgres=# CREATE TABLE client (
postgres(#      nome VARCHAR(255),
postgres(#      idade INT
postgres(# );
CREATE TABLE
```

Agora, rode o seguinte comando:

```sql
SELECT * FROM client;
```

E seu terminal deve estar dessa forma:

```
postgres=# SELECT * FROM client;
 nome | idade
------+-------
(0 linha)
```

Agora vamos entender o que aconteceu:

1. Você usou o comando `CREATE TABLE` para criar um tabela de nome `client`;

2. Essa tabela recebeu duas colunas: 

    - `nome`, do tipo `VARCHAR` (sequencia de texto) com um limite de 255 caracteres;
    - `idade`, do tipo `INT` (um número inteiro)

3. Após isso, você usou o comando `SELECT` para exibir todos os valores (*) da tabela `client`.

O comando `CREATE TABLE` segue a seguinte sintaxe:

```sql
CREATE TABLE <nome-tabela> (
    <nome-coluna-1> <tipo-coluna-1>,
    <nome-coluna-2> <tipo-coluna-2>
);
```

> [!WARNING] 
> **A última coluna não tem vírgula no final!!**

### ALTER TABLE

Ainda com o SQL Shell aberto, vamos alterar a tabela que criamos. Rode o seguinte comando:

```sql
ALTER TABLE client
ADD email VARCHAR(200);
```

Agora rode o mesmo comando `SELECT` do exemplo anterior, e veja que a coluna `email` foi adicionada à tabela.

Mas digamos que eu queira renomear a coluna `idade` para `sobrenome`. Para fazer isso, rode o seguinte:

```sql
ALTER TABLE client
RENAME COLUMN idade TO sobrenome;
```

Agora temos as colunas `nome`, `sobrenome` e `email`. Porém, a coluna `sobrenome` está com o tipo `INT`, embora não represente mais um número inteiro e sim uma sequência de caracteres. 

Para mudar isso, basta rodar o seguinte código:

```sql
ALTER TABLE client
ALTER COLUMN sobrenome TYPE VARCHAR(255);
```

Agora, digamos que eu tenha desistido da coluna `sobrenome` e quero excluí-la. Para fazer isso, rode:

```sql
ALTER TABLE client
DROP COLUMN sobrenome;
```

E pronto! Agora, se você usar o `SELECT` novamente, verá uma tabela vazia com as colunas `nome` e `email`.

### DROP TABLE

Mas uma tabela vazia, por enquanto, não é necessária. Vamos deletá-la do banco de dados:

```sql
DROP TABLE client;
```

E pronto! A tabela `client` foi excluída do database!

## DML (Data Manupulation Language)

A DML inclui comandos relacionados à manipulação de registros (linhas) das tabelas. Como no tópico anterior, vamos aprender os principais comandos na prática.

### SELECT

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

### INSERT INTO

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

### UPDATE

Digamos que Maria tenha ganhado alguns seguidores e precisemos editar a tabela para adicioná-los. Podemos usar o seguinte comando para isso:

```sql
UPDATE users
SET followers = 5
WHERE username = 'Maria';
```
Observe a mudança com o `SELECT`.

### DELETE

Agora, digamos que Marcelo tenha excluído sua conta de usuário. Não é mais necessário que eu tenha dados sobre essa conta em minha tabela, portanto, vamos removê-la:

```sql
DELETE FROM users
WHERE username = "Marcelo";
```

E pronto! Deletamos a conta de Marcelo!!

> [!TIP]
> Se quiser excluir todos os dados de uma tabela, basta executar `DELETE FROM <nome-da-tabela>;` (Use com sabedoria).

## Conclusão

Muita coisa, mas ainda tem mais. Vamos continuar estudando SQL no próximo tópico.

[Anterior: Configurando](Configurando.md)
[Próximo: Estruturando](Estruturando.md)
