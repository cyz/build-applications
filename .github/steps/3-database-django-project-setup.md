## Passo 3: Inicializar e criar o banco de dados octofit_db MongoDB, projeto/aplicativo Django, atualizar arquivos do projeto/aplicativo Django e popular o banco de dados MongoDB

Neste passo, vamos realizar as seguintes tarefas:

- Configurar a estrutura do banco de dados octofit_db MongoDB.
- Atualizar os arquivos do aplicativo octofit-tracker/backend/octofit_tracker:
  - settings, models, serializers, urls, views, tests e admin.
- Popular o banco de dados octofit_db com dados de teste.
- Verificar se os dados de teste foram populados no banco de dados octofit_db.

1. Abra todos os arquivos na pasta `docs` e mantenha este arquivo aberto no editor durante todo o exercício.
    1. O modo agente usa `mona-high-school-fitness-tracker.md` e `octofit_story.md` como referência para criar a aplicação.
2. Copie e cole os seguintes prompts no chat do GitHub Copilot e selecione "Agente" em vez de "Perguntar" ou "Editar" no menu suspenso onde você está inserindo o prompt.

> 🪧 **Nota:** 
- Não altere o modelo de GPT-4, isso será uma atividade opcional no final do curso.
- Lembre-se de que o modo agente do Copilot é conversacional, então ele pode fazer perguntas e você pode fazer perguntas também.
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar os comandos apresentados pelo modo agente do Copilot.
- Mantenha os arquivos criados e atualizados pelo modo agente do Copilot até que ele termine.
- O modo agente tem a capacidade de avaliar sua base de código, executar comandos e adicionar/refatorar/excluir partes do seu código e se auto corrigir automaticamente se ele ou você cometer um erro no processo.

### :keyboard: Atividade: Configurar o projeto/aplicativo Python Django

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington, vamos configurar o projeto/aplicativo Python Django e executar o servidor.
>
> 1. O diretório octofit-tracker/backend armazenará o projeto e aplicativo django com o nome octofit-tracker.
> 2. Configure a configuração adicional para o projeto/aplicativo django com o nome octofit-tracker.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

> 🪧 **Nota:** 
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar cada comando apresentado pelo modo agente do Copilot.
- Mantenha os arquivos criados e atualizados até que o modo agente do Copilot tenha terminado.

> ❕ **Importante:** Não inicie o aplicativo Python Django da maneira que o modo agente do GitHub Copilot sugere, clique em **cancelar**.

### :keyboard: Atividade: Inicializar e criar o banco de dados octofit_db MongoDB

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo da escola de Merington. Vamos inicializar o banco de dados octofit_db.
>
> 1. Inicialize o banco de dados mongo octofit_db.
> 2. Crie uma estrutura de tabela correta para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 3. Certifique-se de que há um ID único para a chave primária na coleção de usuários.
>   ex. db.users.createIndex({ "email": 1 }, { unique: true })
> 4. Execute o comando para mim para criar o banco de dados.
> 5. Liste as coleções no banco de dados octofit_db.
> 
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
> ```

> ❕ **Importante:**
- Se não houver botão "Continuar", basta puxar o lado esquerdo do painel de chat do GitHub Copilot para a esquerda, e ele deve aparecer.
- Se isso não funcionar, você pode precisar copiar e colar a resposta no terminal se não houver botão "Continuar".

### :keyboard: Atividade: Atualizar os arquivos do projeto/aplicativo Python Django

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo da escola de Merington. Vamos atualizar os arquivos do aplicativo octofit-tracker/backend/octofit_tracker.
>
> 1. Atualize o arquivo octofit-tracker/backend/octofit_tracker/settings.py para incluir a conexão com o banco de dados MongoDB.
> 2. Atualize o arquivo octofit-tracker/backend/octofit_tracker/models.py para incluir os modelos para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 3. Atualize o arquivo octofit-tracker/backend/octofit_tracker/serializers.py para incluir os serializers para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 4. Atualize o arquivo octofit-tracker/backend/octofit_tracker/urls.py para incluir as URLs para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 5. Atualize o arquivo octofit-tracker/backend/octofit_tracker/views.py para incluir as views para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 6. Atualize o arquivo octofit-tracker/backend/octofit_tracker/tests.py para incluir os testes para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 7. Atualize o arquivo octofit-tracker/backend/octofit_tracker/admin.py para incluir o admin para as coleções de usuários, equipes, atividades, leaderboard e treinos.
> 8. Certifique-se de que api_root está em octofit-tracker/backend/octofit_tracker/urls.py.
> 9. Habilite CORS no arquivo octofit-tracker/backend/octofit_tracker/settings.py para permitir solicitações de origem cruzada do aplicativo frontend React e permitir todas as origens, métodos e cabeçalhos.
> 10. Permita todos os hosts no arquivo settings.py.
> 11. Instale os componentes do middleware CORS.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
> ```

> ❕ **Importante:** Não inicie o aplicativo Python Django da maneira que o modo agente do GitHub Copilot sugere, clique em **cancelar**.

### :keyboard: Atividade: Popular o banco de dados octofit_db com dados de teste dos arquivos do projeto/aplicativo Django

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington. Vamos popular o banco de dados octofit_db com dados de teste. Use os mesmos dados do arquivo docs/mona-high-school-fitness-tracker.md.
> 
> 1. Crie um arquivo de dados de teste no diretório octofit-tracker/backend/octofit_tracker.
> 2. Certifique-se de que o servidor Python Django está em execução no ambiente virtual Python, faça as migrações e migre o banco de dados.
> 3. Popule o banco de dados octofit_db com dados de teste para as coleções de usuários, equipes, atividades, leaderboard e treinos com base nos dados de teste no arquivo docs/mona-high-school-fitness-tracker.md populate_db.py.
> 4. Verifique se os dados de teste foram populados no banco de dados octofit_db.
> 
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
> ```

Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.

> ❕ **Importante:**
- Não inicie o aplicativo Python Django da maneira que o modo agente do GitHub Copilot sugere, clique em **cancelar**.
- Se não houver botão "Continuar", basta puxar o lado esquerdo do painel de chat do GitHub Copilot para a esquerda, e ele deve aparecer.
- Se isso não funcionar, você pode precisar copiar e colar a resposta no terminal se não houver botão "Continuar".

1. Agora que criamos a estrutura do banco de dados, atualizamos nossos arquivos do projeto Django e populamos o banco de dados, vamos verificar nossas mudanças na branch `build-octofit-app`.

1. Com nossas novas mudanças concluídas, por favor, **commit** e **push** as mudanças para o GitHub.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para continuarmos trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/management/commands/populate_db.py`
- Se Mona encontrou um erro, basta fazer uma correção e enviar suas mudanças novamente. Mona verificará seu trabalho quantas vezes forem necessárias.

</details>
