# Estruturando

[Anterior: SQL Básico Parte 2](SQL-Básico2.md)
<br>
[Próximo: Diagrama ER](Diagrama-ER.md)

## Introdução

Agora que aprendemos a criar e manipular tabelas com SQL, vamos aprender como funciona a estruturação de um banco de dados relacional.

Para que os dados possam ser facilmente acessados e estejam nem organizados é necessária uma boa estruturação das tabelas e colunas. 

Isso pode ser feito a partir do *Modelo Entidade-Relacionamento* (MER).

## Modelo Entidade-Relacionamento

Para estruturar um banco de dados de forma que ele abstraia eficientemente conceitos da realidade, utilizamos o MER.

Para aprendermos a utilizá-lo, faremos um exemplo simples.

## Entidades

Segundo o MER, primeiro devemos abstrair as entidades e seus atributos da realidade e colocá-los no modelo.

Uma **entidade representa um conceito ou objeto da realidade** como uma tabela no banco de dados. Cada entidade possui características comuns chamadas de **atributos**, que são as colunas da tabela.

Vamos entender melhor utilizando o exemplo.

## Exemplo

Imagine que eu queira organizar o catálogo de livros de uma biblioteca. Para estruturar esse banco de dados, podemos criar a entidade Livro, com os atributos relacionados ao livro:

| **Entidade**: Livro
| --------------------------------------------------------- |
|**Atributos**: Título, Autor, Edição, Gênero, Código, etc.


Logo, teríamos uma tabela Livro com as colunas Título, Autor, Edição...

Aproveitando o embalo, é possível criar ainda várias entidades que complementam a entidade Livro:

| **Entidade**: Gênero
| ---------------------------- |
| **Atributos**: Nome do gênero

e

| **Entidade**: Autor
| --------------------------------------- |
| **Atributos**: Nome, Data de Nascimento

Acabamos de criar nossas primeiras entidades. Agora, vamos tratar dos relacionamentos entre elas.

## Relacionamentos e cardinalidades

No MER, as entidades conversam a partir de **relacionamentos**, que podem ser de três tipos (ou cardinalidades):

- **um para um (1:1)**: cada um dos participantes só faz referência ao outro. Ex: Um Usuário (1) possui um Cronograma (1) de estudos e vice-e-versa.

- **um para muitos (1:n)**: uma das entidades se relaciona com várias da outra, mas cada uma das relacionadas apenas se relaciona com a primeira. Ex: Uma Categoria define vários Produtos (n), mas cada Produto só pode ter uma Categoria (1).

- **muitos para muitos (n:n)**: cada entidade pode se relacionar com uma ou mais entidades do outro tipo. Ex: Um Usuário pode ter vários Usuários como amigos (n) assim como pode ser amigo de vários outros Usuários (n).

## Continuando o exemplo

Agora vamos relacionar as entidades da biblioteca:

- Livro <($n$)--($1$)> Gênero:
    - Um livro possui $1$ gênero
    - Um gênero identifica $n$ livros
- Autor <($n$)--($n$)> Livro
    - Um autor pode escrever $n$ livros
    - Um livro pode ter $n$ autores

Agora temos as relações. Mas ainda falta um ponto importante: como eu posso identificar cada tabela?

## Chaves primária e estrangeira

Para identificar cada registro da tabela e poder referenciá-los nos relacionamentos são utilizadas **chaves primárias**.

A chave primária de uma tabela é a coluna que identifica unicamente cada registro feito na tabela. Os valores da chave primária **são únicos**.

Ex:

Tabela autores

| id | nome    | data_nasc
| -- | ------- | ---
| 1  | Autor 1 | ...
| 2  | Autor 2 | ...
| 3  | Autor 3 | ...
...

Como podemos ver, a coluna `id` é responsável por identificar cada autor. Seus valores são únicos para cada autor.

Já uma **chave estrangeira** é **uma chave primária referenciada em outra tabela.**

Ex:

Tabela livros

| id | titulo  | autor | ... |
| -- | ------- | ----- | --- |
| 1  | Livro 1 | 2     | ... |
| 2  | Livro 2 | 3     | ... |
| 3  | Livro 3 | 3     | ... |
...

Na tabela Livro, temos a coluna `id`, que é a chave primária dessa tabela, e, para referenciar o autor, temos a coluna `autor`, que referencia a chave primária do autor do livro. 

O autor do Livro 1 é o Autor 2, e assim por diante.

### No SQL

Podemos adicionar chaves estrangeiras na criação de uma tabela ou depois.

Na criação temos:

```sql
CREATE TABLE livros (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor_id INT,
    FOREIGN KEY (autor_id) REFERENCES autores(autor_id) ON DELETE CASCADE
);
```

E após temos:

```sql
ALTER TABLE livros
ADD CONSTRAINT fk_autor
FOREIGN KEY (autor_id)
REFERENCES autores(autor_id);
```

### ON DELETE

Seria quebra de integridade deletar um autor e deixar os livros, pois eles não teriam mais a referência do autor.

Para especificar como agir a isso, ao definirmos um `FOREIGN KEY`, definimos o `ON DELETE` com uma das opções abaixo:

- `NO ACTION`: retorna erro de integridade.
- `CASCADE`: deleta todas as linhas que referenciam a linha deletada.
- `SET NULL` ou `SET DEFAULT`: coloca a coluna de referência como `NULL` ou como o valor padrão da coluna, respectivamente.

## Muitos para muitos

Os relacionamentos 1:1 e 1:n, como vimos, podem ser representados por colunas específicas nas tabelas.

Entretanto, o relacionamento n:n exige uma abordagem especial: a criação de uma nova tabela para o relacionamento.

Ex:

Tabela Usuário

| id | usuario |
| -- | ------- |
| 1  | User 1  |
| 2  | User 2  |
| 3  | User 3  |

Tabela Amizades

| usuario | amigo |
| ------- | ----- |
| 1       | 2     |
| 2       | 1     |
| 3       | 1     |
| 1       | 2     |

Então, como vemos, a tabela Amizades, que representa o relacionamento entre os Usuários, apenas relaciona as chaves primárias de cada tabela.

## Conclusão

Agora que aprendemos a estruturar bancos de dados relacionais, aprenderemos a representar graficamente esse modelo.

[Anterior: SQL Básico Parte 2](SQL-Básico2.md)
<br>
[Próximo: Diagrama ER](Diagrama-ER.md)
