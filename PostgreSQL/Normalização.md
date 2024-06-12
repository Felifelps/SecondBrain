# Normalização

[Anterior: Diagrama ER](Diagrama-ER.md)
<br>
[Próximo: Consultas](Consultas.md)

## Introdução

Para diminuir a redundância e repetição de informações num banco de dados, o submetemos, no processo de estruturação, ao processo de normalização.

Esse processo consiste na aplicação de regras específicas para a otimização do banco de dados. Cada conjunto de regras transforma sua base de dados em uma estrutura específica conhecida como **forma normal**.

Existem várias formas normais, mas aqui estudaremos as três primeiras.

## Primeira Forma Normal (1FN)

Nesta forma normal, a base deve seguir as seguintes regras:

- cada célula deve ser atômica (conter apenas uma informação);
- cada coluna deve comportar apenas um tipo de dado;

Ex:

Forma errada:

| Nome  | Telefone
| ----- | --------
| João  | 40028922
| Maria | 89929902, 09928332

Na 1FN:

| Nome  | Telefone
| ----- | --------
| João  | 40028922
| Maria | 89929902
| Maria | 09928332

## Segunda Forma Normal (2FN)

Para que uma base esteja nesta forma normal, deve seguir as seguintes regras:

- estar na 1FN;
- associar cada atributo não-chave a uma chave primária, para evitar repetições;

Ex:

Forma errada (cada curso possui um único professor):

| Curso      | Horário | Professor
| ---------- | ------- | ---------
| Matemática | 10:30AM | João
| Inglês     | 11:45AM | Marcela
| Inglês     | 02:00PM | Marcela


Na 2FN (não se repetem informações desnecessárias):

| Curso      | Horário 
| ---------- | ------- 
| Matemática | 10:30AM
| Inglês     | 11:45AM 
| Inglês     | 02:00PM 

| Curso      | Professor
| ---------- | ---------
| Matemática | João
| Inglês     | Marcela

## Terceira Forma Normal (3FN)

A 3FN inclui as seguintes regras:

- a tabela deve estar na 2FN;
- caso um atributo não-chave dependa de outro atributo não-chave em uma tabela, deve-se criar uma nova tabela relacionando-os e remover um dos dois.

Ex:

Forma errada (cada professor usa uma sala fixa):

| Curso      | Horário | Professor | Sala
| ---------- | ------- | --------- | ----
| Matemática | 10:30AM | João      | 1°
| Inglês     | 11:45AM | Marcela   | 3°
| Inglês     | 02:00PM | Marcela   | 3°

Na 3FN:

| Curso      | Horário 
| ---------- | ------- 
| Matemática | 10:30AM
| Inglês     | 11:45AM 
| Inglês     | 02:00PM 

| Curso      | Professor | Sala
| ---------- | --------- | ----
| Matemática | João      | 1°
| Inglês     | Marcela   | 3°

## Conclusão

A partir das formas normais, podemos minimizar os custos de uma base de dados (em largas escalas) e aumentar a eficiência de nossas consultas, que, inclusive, serão o próximo tópico.

[Anterior: Diagrama ER](Diagrama-ER.md)
<br>
[Próximo: Consultas](Consultas.md)