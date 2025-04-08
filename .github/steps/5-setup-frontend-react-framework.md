## Passo 5: Configurar o framework React no frontend, atualizar os componentes e iniciar o aplicativo OctoFit Tracker

Neste passo, vamos realizar as seguintes tarefas:

- Configurar o framework React no frontend do octofit-tracker.
- Atualizar os seguintes componentes para incluir o framework React:
  - src/App.js
  - src/index.js
  - src/components/Activities.js
  - src/components/Leaderboard.js
  - src/components/Teams.js
  - src/components/Users.js
  - src/components/Workouts.js
- Iniciar o aplicativo React e verificar a saída.

1. Abra todos os arquivos na pasta `docs` e mantenha este arquivo aberto no editor durante todo o exercício.
    1. O modo agente usa `mona-high-school-fitness-tracker.md` e `octofit_story.md` como referência para criar a aplicação.
2. Copie e cole os seguintes prompts no chat do GitHub Copilot e selecione "Agente" em vez de "Perguntar" ou "Editar" no menu suspenso onde você está inserindo o prompt.

> 🪧 **Nota:** 
- Não altere o modelo de GPT-4, isso será uma atividade opcional no final do curso.
- Lembre-se de que o modo agente do Copilot é conversacional, então ele pode fazer perguntas e você pode fazer perguntas também.
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar os comandos apresentados pelo modo agente do Copilot.
- Mantenha os arquivos criados e atualizados pelo modo agente do Copilot até que ele termine.
- O modo agente tem a capacidade de avaliar sua base de código, executar comandos e adicionar/refatorar/excluir partes do seu código e se auto corrigir automaticamente se ele ou você cometer um erro no processo.

### :keyboard: Atividade: Instalar o framework React no frontend do octofit-tracker

> https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington. Vamos configurar o codespace para o framework React no frontend do octofit-tracker.
>
> 1. Crie o diretório octofit-tracker/frontend.
> 2. Crie o aplicativo react no diretório octofit-tracker/frontend.
> 3. Instale versões estáveis do framework React e módulos com base no docs/mona-high-school-fitness-tracker.md.
> 4. Instale o bootstrap estável no diretório octofit-tracker/frontend.
> 5. Importe o css do bootstrap no arquivo src/index.js.
> 6. Instale o react-router-dom estável no diretório octofit-tracker/frontend.
> 7. Não altere o arquivo .gitignore.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

### :keyboard: Atividade: Atualizar os componentes React do frontend do octofit-tracker

> 🪧 **Nota:** 
- Certifique-se de substituir [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] pelo nome do seu codespace.
  - ex. redesigned-spork-g6pj46rr9hpp6x
- Você pode obter o nome do codespace executando o seguinte comando no terminal: `echo $CODESPACE_NAME`.

> https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington. Vamos atualizar os componentes React do frontend do octofit-tracker.
>
> - Atualize os seguintes componentes para incluir o framework React e apontar para a API do backend:
>   - src/App.js
>   - src/index.js
>   - src/components/Activities.js
>   - src/components/Leaderboard.js
>   - src/components/Teams.js
>   - src/components/Users.js
>   - src/components/Workouts.js
> - Em cada componente, substitua a URL de fetch pela URL do codespace https://[REPLACE-THIS-WITH-YOUR-CODESPACE-NAME]-8000.app.github.dev/api/<component> para o backend do Django rest framework.
> - Certifique-se de usar a porta e o protocolo corretos, http ou https.
> - Atualize src/App.js para incluir a navegação principal para todos os componentes.
> - Certifique-se de que o react-router-dom seja usado para o menu de navegação.
> - O aplicativo react deve mostrar o menu de navegação e os componentes.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
> ```

> ❕ **Importante:**
- Certifique-se de substituir [REPLACE-THIS-WITH-YOUR-CODESPACE-NAME] pelo nome do seu codespace.
  - ex. redesigned-spork-g6pj46rr9hpp6x
- Você pode obter o nome do codespace executando o seguinte comando no terminal: `echo $CODESPACE_NAME`.

### :keyboard: Atividade: Iniciar o aplicativo react e verificar a saída

Agora, vamos realmente tentar executar a aplicação react! Na barra lateral esquerda, selecione a aba `Executar e Depurar` e pressione o ícone **Iniciar Depuração**.

<img src="https://github.com/user-attachments/assets/8ab08e4e-539a-4ca9-8270-be4b1f0df176"  width=30% height=30%>

### :keyboard: Atividade: Vamos adicionar formatação, estruturação e estilo ao aplicativo octofit tracker

> https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington. Vamos estilizar isso como App.css e deixá-lo bonito.
>
> - Vamos fazer com que o App.js e todos os arquivos javascript dos componentes no aplicativo sejam consistentes com o seguinte:
>   - Use tabelas bootstrap para os dados em todos os componentes javascript.
>   - Use botões bootstrap para os botões.
>   - Use cabeçalhos bootstrap para os cabeçalhos.
>   - Use links bootstrap para os links.
>   - Use navegação bootstrap para o menu de navegação.
>   - Use formulários bootstrap para os formulários.
>   - Use cartões bootstrap para os cartões.
>   - Use modais bootstrap para os modais.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

### :keyboard: Atividade Opcional: Vamos deixar o aplicativo octofit tracker bonito, agradável e adicionar um pouco de cor

> https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff
>
> ```prompt
> Com base no exemplo do aplicativo monafit tracker no arquivo docs/mona-high-school-fitness-tracker.md e use octofit como o nome do aplicativo das escolas de mergington. Vamos estilizar isso como App.css e deixá-lo bonito.
> 
> - Edite o arquivo App.css para fazer o seguinte:
>   - Adicione um pouco de cor ao fundo.
>   - Adicione um pouco de cor ao texto.
>   - Adicione um pouco de cor às tabelas.
>   - Adicione um pouco de cor aos botões.
>   - Adicione um pouco de cor aos cabeçalhos.
>   - Adicione um pouco de cor aos links.
>   - Adicione um pouco de cor ao menu de navegação.
> - Adicione o logotipo octofitapp-small justificado à esquerda no aplicativo e deixe-o bonito.
> - Adicione um favicon ao aplicativo e deixe-o bonito.
>
> Não prossiga para a próxima atividade até que todos esses passos sejam concluídos.
>```

### :keyboard: Atividade Opcional: Iterar na aparência e tentar diferentes modelos

> 🧪 **Experimente isto:**
- Tente criar seus próprios prompts para alterar a aparência do aplicativo, adicionar recursos e experimentar diferentes modelos.
- Quando estiver satisfeito com o aplicativo, você pode fazer commit das alterações e enviá-las para sua branch `build-octofit-app`.

1. Agora que criamos o frontend REACT para todos os componentes da aplicação, vamos verificar nossas mudanças na branch `build-octofit-app`.

1. Com nossas novas mudanças concluídas, por favor, **commit** e **push** as mudanças para o GitHub.

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e compartilhar a próxima lição para continuarmos trabalhando!

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que suas mudanças de commit foram feitas para os seguintes arquivos na branch `build-octofit-app` e enviadas/sincronizadas para o GitHub:
  - `octofit-tracker/frontend/src/components/Activities.js` e ele contém `-8000.app.github.dev/api/activities/`
  - `octofit-tracker/frontend/src/components/Leaderboard.js` e ele contém `-8000.app.github.dev/api/leaderboard/`
  - `octofit-tracker/frontend/src/components/Teams.js` e ele contém `-8000.app.github.dev/api/teams/`
  - `octofit-tracker/frontend/src/components/Users.js` e ele contém `-8000.app.github.dev/api/users/`
  - `octofit-tracker/frontend/src/components/Workouts.js` e ele contém `-8000.app.github.dev/api/workouts/`
- Se Mona encontrou um erro, basta fazer uma correção e enviar suas mudanças novamente. Mona verificará seu trabalho quantas vezes forem necessárias.

</details>
