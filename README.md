# To-do List.

Nesse repositório contém um projeto fullstack realizado o front-end com Html, Css, BootStrap 4 e o back-end com Python e o framework Django.

Desenvolvi esse projeto com o intuito de aplicar conhecimentos sobre class based views do Django.

O projeto consiste em um sistema (CRUD) to-do list, onde o usuário do sistema consegue realizar login no sistema,
cadastrar-se como novo usuário, cadastrar tarefas, editar, deletar e visualizar todos as tarefas concluidas em uma tela onde as tarefas são apresentadas em uma tabela.

### Pré-requisitos

- Python instalado;
- Criação do ambiente virtual (Linux: python3 -m venv venv ou no Windows: python -m venv venv);
- Ativação do ambiente criado anteriormente (Linux: source venv/bin/activate ou no Windows: venv\Scripts\activate);
- Instalação dos requirements.txt disponibilizados (pip insall -r requirements.txt);
- O banco de dados é de sua escolha, mas nesse projeto utilizei o SQLite (Caso escolha um banco de dados diferente do padrão não esqueça de realizar as alterações no arquivo settings.py);
- OBS¹: Caso tenha o Docker intalado será o suficiente e apenas precisará rodar o docker compose disponibilizado
(No diretório do projeto rodar o comando: docker compose -f docker-compose.yml up -d --build);
- OBS²: Caso opte por rodar o projeto sem usar o docker, é necessário remover algumas configurações de variáveis de ambiente existente no settings.py e deixar padrão;



### Execução do sistema

- Basta entrar no diretório do projeto e no terminal rodar o comando: python manage.py runserver ou docker compose -f docker-compose.yml up -d --build;
- O servidor será executado e se acessar localhost:8000 acessará a página inicial do sistema onde poderá realizar o cadastro ou o login;

### Exemplo da execução

- Obs: As páginas são acessíveis somente com o usuário autenticado, obviamente, login e cadastro são de livre acesso.

#### Rota para a página inicial (localhost);

- Página inicial simples com botões para direcionar o usuário para login/cadastro.

![Rota index](docs/img/tarefas-index.png)


#### Rota para login (accounts/login);

- Consta algumas validações, o formulário tem que estar preenchido
e com os dados certos para a liberação do acesso.

![Rota de login](docs/img/tarefas-login.png)


#### Rota para cadastro de usuário (accounts/registro);

- Consta algumas validações, o formulário tem que estar preenchido
e com os dados certos para a liberação do acesso.

![Rota de cadastro de usuário](docs/img/tarefas-cadastro-user.png)


#### Rota para o dashboard (/tarefas);

 - Dashboard para visualizar as tarefas que precisam ser realizadas ou em outro status. Nessa tela o usuário pode realizar algumas ações.

![Rota para o dashboard](docs/img/tarefas-principal.png)


#### Rota para cadastrar tarefas (/tarefas/add) ou editar (/tarefas/id/atualizar);

- Realizar o cadastro ou editar a tarefa, pois usa o mesmo formulário.

![Rota para cadastrar tarefa](docs/img/tarefas-cadastrar.png)


#### Rota para visualizar as tarefas concluídas (tarefas/concluidas);

- Visualizar tarefas concluidas.

![Rota para listar tarefas concluídas](docs/img/tarefas-concluido.png)


#### Rota para visualizar as tarefas em andamento (tarefas/andamento);

- Visualizar tarefas em andamento.

![Rota para listar tarefas em andamento](docs/img/tarefas-andamento.png)


#### Modal detalhes;

- Ao clicar no botão detalhes sobe um modal com as informações da tarefa.

![Modal detalhes](docs/img/tarefas-detalhes.png)


#### Modal alterar;

- Ao clicar no botão alterar sobe um modal com botões para realizar ações.

![Modal ações](docs/img/tarefas-acoes.png)



#### Rota para excluir uma tarefas (/tarefas/id/deletar);

- Realizar a exclusão da tarefa.

![Rota para excluir tarefa](docs/img/tarefas-excluir.png)





