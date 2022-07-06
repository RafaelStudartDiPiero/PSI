# PSI

O objetivo desse projeto é criar o site da PSI,a Plataforma de Serviços do ITA, um marketplace de serviços para alunos do ITA.  
A motivação inicial desse projeto foi analisar problemas gerais na comunidade iteana que poderiam ser resolvidos com o desenvolvimento de uma aplicação web.
Percebemos que todo iteano já passou pela situação de precisar realizar uma tarefa, mesmo que simples, porém não ter o conhecimento ou o tempo necessário para tal.
Assim, propomos a criação da PSI, com objetivo conectar alunos que precisam de ajuda a alunos que possam fornecer esses serviços.

# Detalhes da Implementação

O site foi desenvolvido com o framework Django da linguagem Python 3, utilizando um docker para cuidar dos requisitos de maneira unificada.
Para o armazenamento de dados, utilizou-se o PostgreSQL, considerando sua compatibilidade com o Django e suas funcionalidades.
O deploy do site foi realizado por meio da plataforma .... .

# Arquitetura

Deve-se explicar rapidamente como foi realizada a distribuição de arquivos e diretórios no projeto:

## Pages:

  Define a implementação, urls e vistas das páginas genéricas Home e About.
  
## PSI:

  Determina a implementação das interações do site como um todo, descrevendo o _overlevel_ do mesmo.

## Services:

  Descreve a interação dos serviços, como seu armazenamento, criação, alteração e visualização, tanto em lista quanto em detalhes.

## Static:

  Contém alguns arquivos constantes para implementação, como o _style.css_ utilizado.

## Templates:

  Contém os arquivos _.html_ que são utilizados para gerar as vistas do site.

## Users:

  Descreve o comportamento dos usuários, como registro, login, autenticação, visualização e avaliação.

  Além disso, temos alguns arquivos genéricos que estão na raiz que devem ser explicados:
  
## Manage

  O arquivo que descreve depências do _Django_ e o funcionamento correto do site.

## Dockerfile

  Responsável pelas intruções de construção do _docker_ utilizado.

## Requirements

  Contém as dependências necessárias para o funcionamento correto do site.
