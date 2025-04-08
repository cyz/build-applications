## Passo 2: Configuração inicial da aplicação: Estrutura de diretórios, requisitos do Python e MongoDB

Neste passo, vamos realizar as seguintes tarefas:

- Criar a estrutura de diretórios da aplicação octofit-tracker.
- Criar os diretórios octofit-tracker/backend e octofit-tracker/frontend.
- Criar o arquivo octofit-tracker/backend/requirements.txt.

1. Abra todos os arquivos na pasta `docs` e mantenha este arquivo aberto no editor durante todo o exercício.
    1. O modo agente usa `mona-high-school-fitness-tracker.md` e `octofit_story.md` como referência para criar a aplicação.
2. Copie e cole os seguintes prompts no chat do GitHub Copilot e selecione "Agente" em vez de "Perguntar" ou "Editar" no menu suspenso onde você está inserindo o prompt.

<img src="https://github.com/user-attachments/assets/e172f5c0-bc2a-45a9-a301-9af8bfbd6a2e" width=40% height=40%>

> 🪧 **Nota:** 
- Não altere o modelo de GPT-4, isso será uma atividade opcional no final do curso.
- Lembre-se de que o modo agente do Copilot é conversacional, então ele pode fazer perguntas e você pode fazer perguntas também.
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar os comandos apresentados pelo modo agente do Copilot.
- Mantenha os arquivos criados e atualizados pelo modo agente do Copilot até que ele termine.
- O modo agente tem a capacidade de avaliar sua base de código, executar comandos e adicionar/refatorar/excluir partes do seu código e se auto corrigir automaticamente se ele ou você cometer um erro no processo.

### :keyboard: Atividade: Prompt para o GitHub Copilot no modo agente para iniciar a criação da nossa aplicação

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Vamos seguir os seguintes passos e gerar instruções nesta ordem e executar os comandos.
> Use docs/mona-high-school-fitness-tracker.md como guia para a estrutura do projeto e requisitos.
>
> 1. Entenda a história da criação do aplicativo de fitness a partir do arquivo docs/octofit_story.md.
> 2. Crie a estrutura inicial de diretórios para a aplicação octofit-tracker: octofit-tracker/backend, octofit-tracker/frontend.
> 3. Configure o ambiente virtual Python no backend, crie o arquivo octofit-tracker/backend/requirements.txt com base no docs/mona-high-school-fitness-tracker.md e instale os pacotes necessários.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```
>

> ❕ **Importante:** Uma vez que a atividade acima instalar todos os pacotes necessários, prossiga para a próxima atividade.

### :keyboard: Atividade: Vamos iniciar e verificar se o MongoDB está em execução

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md, use octofit como o nome do aplicativo das escolas de mergington. Vamos iniciar e verificar se o MongoDB está em execução.
>
> 1. Inicie o serviço MongoDB.
> 2. Verifique se o serviço MongoDB está em execução.
> 
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

> ❕ **Importante:**
- Se o comando for concluído no terminal, mas o modo agente mostrar que ainda está em execução, clique em parar.
- Você pode precisar colar o prompt novamente no modo agente.

### :keyboard: Atividade: Vamos iniciar e verificar se o MongoDB está em execução

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md, use octofit como o nome do aplicativo das escolas de mergington. Vamos iniciar e verificar se o MongoDB está em execução.
>
> 1. Inicie o serviço MongoDB.
> 2. Verifique se o serviço MongoDB está em execução.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

> ❕ **Importante:**
- Se o comando for concluído no terminal, mas o modo agente mostrar que ainda está em execução, clique em parar.
- Você pode precisar colar o prompt novamente no modo agente.

1. Agora que criamos a estrutura de diretórios do aplicativo, configuramos um ambiente virtual Python e o modo agente do Copilot ajudou a escrever um requirements.txt para instalar todas as dependências do projeto, vamos verificar nossas mudanças na branch `build-octofit-app`.

1. Com nossas novas mudanças concluídas, por favor, **commit** e **push** as mudanças para o GitHub.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para continuarmos trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para o seguinte arquivo na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/requirements.txt` e ele contém o pacote `Django==4.1`
- Se Mona encontrou um erro, basta fazer uma correção e enviar suas mudanças novamente. Mona verificará seu trabalho quantas vezes forem necessárias.

</details>
