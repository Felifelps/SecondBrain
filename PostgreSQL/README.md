# PostgreSQL - Tutorial

[Início](/README.md)

#### **Partes do tutorial:**

1. [Instalação](Instalação.md)

  - [No Windows](Instalação.md#No%20Windows)
  - [Componentes instalados](Instalação.md#Componentes%20instalados)
  - [PostgreSQL Server](Instalação.md#PostgreSQL%20Server)
  - [pgAdmin](Instalação.md#pgAdmin)
  - [Command Line Tools](Instalação.md#Command%20Line%20Tools)
  - [Conclusão](Instalação.md#Conclusão)

2. [Configurando](Configurando.md)

  - [Introdução](Configurando.md#Introdução)
  - [SQLShell](Configurando.md#SQLShell)
  - [pgAdmin](Configurando.md#pgAdmin)
  - [Conclusão](Configurando.md#Conclusão)

3. [SQL Básico](SQL-Básico.md)

  - [Introdução](SQL-Básico.md#Introdução)
  - [Sublinguagens](SQL-Básico.md#Sublinguagens)
  - [CREATE TABLE](SQL-Básico.md#CREATE%20TABLE)
  - [Data Types](SQL-Básico.md#Data%20Types)
  - [ALTER TABLE](SQL-Básico.md#ALTER%20TABLE)
  - [DROP TABLE](SQL-Básico.md#DROP%20TABLE)
  - [Conclusão](SQL-Básico.md#Conclusão)

4. [SQL Básico Parte 2](SQL-Básico2.md)

  - [DML (Data Manupulation Language)](SQL-Básico2.md#DML%20(Data%20Manupulation%20Language))
  - [SELECT](SQL-Básico2.md#SELECT)
  - [INSERT INTO](SQL-Básico2.md#INSERT%20INTO)
  - [WHERE](SQL-Básico2.md#WHERE)
  - [UPDATE](SQL-Básico2.md#UPDATE)
  - [DELETE](SQL-Básico2.md#DELETE)
  - [Conclusão](SQL-Básico2.md#Conclusão)

5. [Estruturando](Estruturando.md)

  - [Introdução](Estruturando.md#Introdução)
  - [Entidades e atributos](Estruturando.md#Entidades%20e%20atributos)
  - [Exemplo](Estruturando.md#Exemplo)
  - [Relacionamentos e cardinalidades](Estruturando.md#Relacionamentos%20e%20cardinalidades)
  - [Continuando o exemplo](Estruturando.md#Continuando%20o%20exemplo)
  - [Chaves primária e estrangeira](Estruturando.md#Chaves%20primária%20e%20estrangeira)
  - [No SQL](Estruturando.md#No%20SQL)
  - [ON DELETE](Estruturando.md#ON%20DELETE)
  - [Muitos para muitos](Estruturando.md#Muitos%20para%20muitos)
  - [Conclusão](Estruturando.md#Conclusão)

6. [Diagrama ER](Diagrama-ER.md)

  - [Introdução](Diagrama-ER.md#Introdução)
  - [Formas](Diagrama-ER.md#Formas)
  - [Analisando o Diagrama](Diagrama-ER.md#Analisando%20o%20Diagrama)
  - [Conclusão](Diagrama-ER.md#Conclusão)

7. [Normalização](Normalização.md)

  - [Introdução](Normalização.md#Introdução)
  - [Primeira Forma Normal (1FN)](Normalização.md#Primeira%20Forma%20Normal%20(1FN))
  - [Segunda Forma Normal (2FN)](Normalização.md#Segunda%20Forma%20Normal%20(2FN))
  - [Terceira Forma Normal (3FN)](Normalização.md#Terceira%20Forma%20Normal%20(3FN))
  - [Conclusão](Normalização.md#Conclusão)

8. [Consultas](Consultas.md)

  - [Introdução](Consultas.md#Introdução)
  - [SELECT](Consultas.md#SELECT)
  - [AS](Consultas.md#AS)
  - [SELECT DISTINCT](Consultas.md#SELECT%20DISTINCT)
  - [WHERE](Consultas.md#WHERE)
  - [Operadores do where](Consultas.md#Operadores%20do%20where)
  - [Exemplos](Consultas.md#Exemplos)
  - [ORDER BY](Consultas.md#ORDER%20BY)
  - [Combinando e alterando condições](Consultas.md#Combinando%20e%20alterando%20condições)
  - [AND](Consultas.md#AND)
  - [OR](Consultas.md#OR)
  - [NOT](Consultas.md#NOT)
  - [LIMIT](Consultas.md#LIMIT)
  - [Conclusão](Consultas.md#Conclusão)

9. [Funções de agregação](Funções-de-Agregação.md)

  - [Introdução](Funções-de-Agregação.md#Introdução)
  - [MIN e MAX](Funções-de-Agregação.md#MIN%20e%20MAX)
  - [GROUP BY e HAVING](Funções-de-Agregação.md#GROUP%20BY%20e%20HAVING)
  - [COUNT](Funções-de-Agregação.md#COUNT)
  - [SUM e AVG](Funções-de-Agregação.md#SUM%20e%20AVG)
  - [Conclusão](Funções-de-Agregação.md#Conclusão)

10. [Join](Join.md)

  - [Introdução](Join.md#Introdução)
  - [INNER JOIN](Join.md#INNER%20JOIN)
  - [LEFT JOIN](Join.md#LEFT%20JOIN)
  - [RIGHT JOIN](Join.md#RIGHT%20JOIN)
  - [FULL OUTER JOIN](Join.md#FULL%20OUTER%20JOIN)
  - [Conclusão](Join.md#Conclusão)

11. [Subconsultas](Subconsultas.md)

  - [Introdução](Subconsultas.md#Introdução)
  - [Subconsultas como condição](Subconsultas.md#Subconsultas%20como%20condição)
  - [Subconsultas com FROM](Subconsultas.md#Subconsultas%20com%20FROM)
  - [Subconsultas com JOIN](Subconsultas.md#Subconsultas%20com%20JOIN)
  - [Conclusão](Subconsultas.md#Conclusão)

<br> (Daqui pra baixo ainda está por vir)
12. [Views](Views.md)
13. [Índices](Índices.md)
14. [Transações e Currency](Transações-e-Currency.md)
15. [Procedures e Functions](Procedures-e-Functions.md)
16. [Triggers](Triggers.md)
17. [Segurança e Acesso](Segurança-e-Acesso.md)
18. [Backup](Backup.md)
19. [Extensões](Extensões.md)


## O que é PostgreSQL?

Não, PostgreSQL não é um banco de dados. Ele é um *Sistema de Gerenciamento de Banco de Dados Relacionais* (SGBDR) open-source, ou seja, um software gratuito e de código aberto que gerencia bancos de dados relacionais.

Como o nome sugere, ele utiliza *Structured Query Language* (SQL) para manipulação e controle dos dados envolvidos. Neste tutorial, vamos aprender muita coisa sobre SQL, bancos de dados relacionais a partir do PostgreSQL.

## Banco de dados relacional?

Um banco de dados relacional é um tipo de banco de dados que organiza os dados em tabelas, estas organizadas em linhas e colunas. 

O diferencial está nas relações entre cada tabela, que são especificadas a partir de chaves primárias e estrangeiras (tópicos futuros). Sua principal vantagem é sua capacidade de manter a integridade e a consistência dos dados. São amplamente utilizados em aplicações.

## E o que é SQL?

SQL, ou *Structured Query Language*, é uma linguagem padrão cujo principal objetivo é manipular tabelas de bancos de dados relacionais. Ela possui comandos relacionados à consulta; criação, atualização e exclusão de registros; manipulação de bancos, dentre outros.

## Conclusão

Explicados esses conceitos, vamos ao que importa. Mas, antes de começarmos, precisamos instalar o necessário na sua máquina.

[Próximo: Instalação](Instalação.md)
