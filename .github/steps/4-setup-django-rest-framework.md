## Passo 4: Configurar o Django REST Framework, iniciar o servidor e testar a API

Neste passo, vamos realizar as seguintes tarefas:

- Configurar o Django REST Framework.
- Iniciar o servidor.
- Testar a API usando curl.

1. Abra todos os arquivos na pasta `docs` e mantenha este arquivo aberto no editor durante todo o exercício.
    1. O modo agente usa `mona-high-school-fitness-tracker.md` e `octofit_story.md` como referência para criar a aplicação.
2. Copie e cole os seguintes prompts no chat do GitHub Copilot e selecione "Agente" em vez de "Perguntar" ou "Editar" no menu suspenso onde você está inserindo o prompt.

> 🪧 **Nota:** 
- Não altere o modelo de GPT-4, isso será uma atividade opcional no final do curso.
- Lembre-se de que o modo agente do Copilot é conversacional, então ele pode fazer perguntas e você pode fazer perguntas também.
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar os comandos apresentados pelo modo agente do Copilot.
- Mantenha os arquivos criados e atualizados pelo modo agente do Copilot até que ele termine.
- O modo agente tem a capacidade de avaliar sua base de código, executar comandos e adicionar/refatorar/excluir partes do seu código e se auto corrigir automaticamente se ele ou você cometer um erro no processo.

### :keyboard: Atividade: Configurar o Django REST Framework, reiniciar o servidor e testar a API

> 🪧 **Nota:** 
- Certifique-se de substituir [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] pelo nome do seu codespace.
  - ex. redesigned-spork-g6pj46rr9hpp6x
- Você pode obter o nome do codespace executando o seguinte comando no terminal: `echo $CODESPACE_NAME`.

> ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de Mergington. Vamos configurar o codespace para a URL, iniciar o servidor via VS Code launch.json e testar a API.
> 
> 1. Ative o ambiente virtual Python.
> 2. Atualize #file:octofit-tracker/backend/octofit_tracker/views.py para substituir o retorno dos endpoints da URL da API REST pela URL do codespace https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev para Django e evitar problemas de certificado HTTPS.
> 3. Certifique-se de que o backend Django funciona em [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev e localhost:8000.
> 4. Teste os endpoints da API usando o comando curl.
> 5. Permita o acesso do host à URL do codespace e localhost:8000.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

> ❕ **Importante:** Não inicie o aplicativo Python Django da maneira que o modo agente do GitHub Copilot sugere, clique em **cancelar**. Siga a próxima atividade em vez disso.

### :keyboard: Atividade: Iniciar o aplicativo Python Django e verificar a saída
Agora, vamos realmente tentar executar a aplicação Django! Na barra lateral esquerda, selecione a aba `Executar e Depurar` e pressione o ícone **Iniciar Depuração**.

<img src="https://github.com/user-attachments/assets/baef4dfe-0751-45cb-9e16-8ff26ba9ff58" width=30% height=30%>

> ❕ **Importante:**
- Certifique-se de substituir [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] pelo nome do seu codespace.
- ex. redesigned-spork-g6pj46rr9hpp6x
- Você pode obter o nome do codespace executando o seguinte comando no terminal: `echo $CODESPACE_NAME`.

1. Agora que atualizamos nosso produto Django para incluir o nome do nosso codespace para o endpoint da URL,
   vamos verificar nossas mudanças na branch `build-octofit-app`.

1. Com nossas novas mudanças concluídas, por favor, **commit** e **push** as mudanças para o GitHub.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para continuarmos trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/backend/octofit_tracker/settings.py`
  - `octofit-tracker/backend/octofit_tracker/views.py`
- Se Mona encontrou um erro, basta fazer uma correção e enviar suas mudanças novamente. Mona verificará seu trabalho quantas vezes forem necessárias.

</details>
