# Estruturando

[Anterior: Estruturando](Estruturando.md)
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

### Exemplo

Imagine que eu queira organizar o catálogo de livros de uma biblioteca. Para estruturar esse banco de dados, podemos criar a entidade Livro, com os atributos relacionados ao livro:

**Entidade**: Livro

**Atributos**: Título, Autor, Edição, Gênero, Código, etc.

Logo, teríamos uma tabela Livro com as colunas Título, Autor, Edição...

Aproveitando o embalo, é possível criar ainda várias entidades que complementam a entidade Livro:

**Entidade**: Gênero

**Atributos**: Nome do gênero

e

**Entidade**: Autor

**Atributos**: Nome, Data de Nascimento

Acabamos de criar nossas primeiras entidades. Agora, vamos tratar dos relacionamentos entre elas.

## Relacionamentos

No MER, as entidades conversam a partir de **relacionamentos**, que podem ser de três tipos:

- **um para um (1:1)**: cada um dos participantes só faz referência ao outro. Ex: Um Usuário (1) possui um Cronograma (1) de estudos e vice-e-versa.

- **um para muitos (1:n)**: uma das entidades se relaciona com várias da outra, mas cada uma das relacionadas apenas se relaciona com a primeira. Ex: Uma Categoria define vários Produtos (n), mas cada Produto só pode ter uma Categoria (1).

- **muitos para muitos (n:n)**: cada entidade pode se relacionar com uma ou mais entidades do outro tipo. Ex: Um Usuário pode ter vários Usuários como amigos (n) assim como pode ser amigo de vários outros Usuários (n).

### Continuando o exemplo

Agora vamos relacionar as entidades da biblioteca:

- Livro <(n)--(1)> Gênero
- Autor <(n)--(n)> Livro

Agora temos as relações. Mas ainda falta um ponto importante: como eu posso identificar cada tabela?

## Chaves primária e estrangeira

Para identificar cada registro da tabela e poder referenciá-los nos relacionamentos são utilizadas **chaves primárias**.

A chave primária de uma tabela é a coluna que identifica unicamente cada registro feito na tabela. Os valores da chave primária **são únicos**.

Ex:

Tabela Autor

| id | nome    | data_nasc
| -- | ------- | ---
| 1  | Autor 1 | ...
| 2  | Autor 2 | ...
| 3  | Autor 3 | ...
...

Como podemos ver, a coluna `id` é responsável por identificar cada autor. Seus valores são únicos para cada autor.

Já uma **chave estrangeira** é **uma chave primária referenciada em outra tabela.**

Ex:

Tabela Livro

| id | titulo  | autor | ... |
| -- | ------- | ----- | --- |
| 1  | Livro 1 | 2     | ... |
| 2  | Livro 2 | 3     | ... |
| 3  | Livro 3 | 3     | ... |
...

Na tabela Livro, temos a coluna `id`, que é a chave primária dessa tabela, e, para referenciar o autor, temos a coluna `autor`, que referencia a chave primária do autor do livro. 

O autor do Livro 1 é o Autor 2, e assim por diante.

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

[Anterior: Estruturando](Estruturando.md)
<br>
[Próximo: Diagrama ER](Diagrama-ER.md)
