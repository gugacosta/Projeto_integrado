# Sistema de Gerenciamento de Estacionamentos - Projeto_Integrado-PUCMINAS

Sistema de gerenciamento de estacionamentos privativos, com opção de clientes rotativos
e fidelizados.

## Tabela de Conteúdos

- [Sobre](#sobre)
- [Funcionalidades](#funcionalidades)
- [Requisitos do Sistema](#requisitos-do-sistema)
- [Instalação](#instalação)
- [Deploy](#deploy)
- [Estrutura](#estrutura)


## Sobre

Este projeto desenvolve uma aplicação web com os frameworks Django e Bootstrap e persistencia de dados atráves do SGBD MYSql.

## Funcionalidades

1. Visualização de informações sobre o funcionamento do estacionamento para todos.
2. Botão com link direto para API do Whatsapp e entrar em contato com o administrador.
3. Cadastro de usuários.
4. Gestão de vagas, clientes e planos.
5. Interatividade com o cliente.

## Requisitos do Sistema

Hardware:

Processador: Dual-core ou superior, com velocidade de clock de 1.8 GHz ou mais.
Memória RAM: 4 GB ou mais.
Armazenamento: 128 GB de armazenamento em estado sólido (SSD) ou superior para melhor desempenho.
Sistema Operacional:
    Linux (ex.: Ubuntu Server, CentOS)
    Windows Server (versão mais recente)
    macOS Server (para ambiente de desenvolvimento)

Servidor Web:
Nginx/Apache + gunicorn

SGBD:
MySQL v. 8 +

Linguagem de Programação:
Python v3.7 +
Django v4.0+

## Instalação

Após realizar o clone do projeto realize os seguintes comandos:
pip install -r requirements.txt
python site_estacionamento/manage.py migrate

## Deploy

Crie um banco de dados com o nome db_estacionamento e usuário administrador com
todas as permissoes: estacionamento_admin.

Para se realizar o deploy em produção é necessário se realizar alguma etapas para garantir a segurança
da aplicação. Segue o procedimento completo em:
https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

## Estrutura 
![Estrutura]([docs/projecttree.jpg](https://github.com/gugacosta/Projeto_integrado/blob/main/docs/projectree.JPG)https://github.com/gugacosta/Projeto_integrado/blob/main/docs/projectree.JPG)
