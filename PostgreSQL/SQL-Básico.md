# SQL Básico

[Anterior: Configurando](Configurando.md)
<br>
[Próximo: SQL Básico Parte 2](SQL-Básico2.md)

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

Neste tópico vamos tratar o essencial da DDL.

Os comandos da DDL são voltados para a criação, manipulação e exclusão de tabelas no banco de dados. A melhor forma de aprender, é na prática.

## CREATE TABLE

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

## Data Types

Como vimos, ao criar as colunas, definimos um tipo para os valores que serão inseridos nela. Esses são os Data Types.

Os mais utilizados do Postgres são:

- **integer (ou int)**: Armazena números inteiros de tamanho médio. Ex: `age INTEGER`.
- **numeric (ou decimal)**: Armazena números com precisão exata. Ex: `price NUMERIC(10, 2)`.
- **varchar(n)**: Cadeia de caracteres com tamanho variável. Ex: `name VARCHAR(50)`.
- **text**: Cadeia de caracteres com tamanho variável sem limite específico. Ex: `description TEXT`.
- **date**: Armazena uma data (ano, mês, dia). Ex: `birthdate DATE`.
- **timestamp**: Armazena data e hora (com ou sem fuso horário). Ex: `created_at TIMESTAMP`, `updated_at TIMESTAMP WITH TIME ZONE`.
- **boolean**: Armazena valores booleanos (true, false). Ex: `is_active BOOLEAN`.
- **json/jsonb**: Armazena dados JSON. Ex: `metadata JSONB`.
- **uuid**: Identificador universal único. Ex: `uuid UUID`.
- **array**: Armazena um array de qualquer tipo de dado. Ex: `tags TEXT[]`.
- **inet**: Endereço de host IP. Ex: `ip_address INET`.

> [!TIP] 
> Caso queira se aprofundar nos Data Types, visite [esse site](https://www.geeksforgeeks.org/postgresql-data-types/).

## ALTER TABLE

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

## DROP TABLE

Mas uma tabela vazia, por enquanto, não é necessária. Vamos deletá-la do banco de dados:

```sql
DROP TABLE client;
```

E pronto! A tabela `client` foi excluída do database!

## Conclusão

Agora que vimos o básico da DML, nos introduzimos ao uso do SQL. No próximo tópico, veremos o essencial acerca da DML!

[Anterior: Configurando](Configurando.md)
<br>
[Próximo: SQL Básico Parte 2](SQL-Básico2.md)