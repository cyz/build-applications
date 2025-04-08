## Passo 1: Olá modo agente do GitHub Copilot

Bem-vindo ao seu exercício **"Construir aplicações com o modo agente do GitHub Copilot"**! :robot:

Neste exercício, você usará o modo agente do GitHub Copilot para construir um aplicativo que rastreia suas metas e progresso de fitness. 🏋️‍♂️🏃‍♀️💪

### O que é o modo agente do GitHub Copilot?

O modo agente do Copilot pode criar aplicativos do zero, realizar refatorações em vários arquivos, escrever e executar testes, e migrar código legado para frameworks modernos. Ele pode gerar automaticamente documentação, integrar novas bibliotecas ou ajudar a responder perguntas sobre uma base de código complexa. O modo agente do Copilot ajuda você a ser super produtivo, tendo um colaborador de IA que entende o ambiente de trabalho. Ele pode orquestrar seu fluxo de desenvolvimento interno enquanto mantém você no controle.

O modo agente do Copilot opera de maneira mais autônoma e dinâmica para alcançar o resultado desejado. Para processar uma solicitação, o Copilot percorre os seguintes passos e itera várias vezes conforme necessário:

- Determina o contexto relevante e os arquivos a serem editados autonomamente.
- Oferece tanto mudanças de código quanto comandos de terminal para completar a tarefa. Por exemplo, o Copilot pode compilar código, instalar pacotes, executar testes e mais.
- Monitora a correção das edições de código e a saída dos comandos de terminal e itera para remediar problemas.

> 💡 **Dica:** Você pode aprender mais sobre o modo agente do GitHub Copilot na https://code.visualstudio.com/docs/copilot/copilot-edits#_use-agent-mode-preview.

### :keyboard: Atividade: Conhecendo seu ambiente de desenvolvimento do modo agente do GitHub Copilot

1. Clique com o botão direito no botão abaixo para abrir a página **Criar Codespace** em uma nova aba.

   https://github.com/codespaces/badge.svg](https://codespaces.new/{{full_repo_name}}?quickstart=1)

   - O nível gratuito do Codespaces que vem com todas as contas do GitHub é suficiente, assumindo que você ainda tenha minutos disponíveis.
   - As configurações padrão do Codespace são suficientes.

1. Confirme que o campo **Repositório** é sua cópia do exercício, não o original, e clique no botão verde **Criar Codespace**.

   - ✅ Sua cópia: `/{{{full_repo_name}}}`
   - ❌ Original: `/skills/build-applications-w-copilot-agent-mode`

1. Aguarde um momento para o Visual Studio Code carregar.
    1. Você pode precisar mudar para a edição insiders do VS Code no codespace, já que o modo agente foi lançado em 4/4 como um lançamento faseado para os usuários.
   <img width="323" alt="Imagem" src="https://github.com/user-attachments/assets/8ff8868b-9120-4055-8449-175e85552ba2" />

1. Antes de continuarmos, vamos tirar um momento para nos familiarizarmos com a pasta do projeto.

   - A barra de navegação à esquerda é onde você pode acessar o explorador de arquivos, o depurador e a pesquisa.
   - O painel inferior (Ctrl+J) mostra a saída do depurador, permite executar comandos de terminal e configurar as portas do serviço web.
   - Nossa pasta de documentos contém outro repositório de aplicativo de amostra que dará contexto ao modo agente do Copilot para construir seu aplicativo. Mais sobre isso nos próximos passos!

1. No topo do VS Code, localize e clique no ícone do Copilot para abrir um painel de chat do Copilot.

   <img width="150" alt="imagem" src="https://github.com/user-attachments/assets/5e64db46-95cb-415d-badc-b6b8677f10c1" />

1. Se esta for sua primeira vez usando o GitHub Copilot, você terá que aceitar os termos de uso para continuar.
    - Clique no botão **Aceitar** para continuar.
    - Se você estiver usando o chat do Copilot pela primeira vez, também terá que aceitar os termos de uso para continuar.
    - Clique no botão **Aceitar** para continuar.

### :keyboard: Atividade: Use o modo agente do Copilot para criar uma branch e publicá-la. 🙋

Ótimo trabalho! Agora que estamos familiarizados com o aplicativo e sabemos que ele funciona, vamos pedir ajuda ao Copilot para iniciar uma branch para podermos fazer algumas personalizações.

1. Se ainda não estiver lá, volte para o VS Code.

1. Abra a janela de chat do GitHub Copilot se ainda não estiver aberta.
2. Copie e cole o seguinte prompt no chat do GitHub Copilot e selecione **Agente** em vez de **Perguntar** ou **Editar** no menu suspenso onde você está inserindo o prompt.

   <img src="https://github.com/user-attachments/assets/e172f5c0-bc2a-45a9-a301-9af8bfbd6a2e" width=30% height=30%>

> 🪧 **Nota:**
- Não altere o modelo de GPT-4, isso será uma atividade opcional no final do curso.
- Lembre-se de que o modo agente do Copilot é conversacional, então ele pode fazer perguntas e você pode fazer perguntas também.
- Aguarde um momento para o Copilot responder e pressione o botão continuar para executar os comandos apresentados pelo modo agente do Copilot.

1. Vamos pedir ao modo agente do Copilot para nos ajudar a lembrar o comando e criar a branch `build-octofit-app` e publicá-la.

   > ![Static Badge](https://img.shields.io/badge/-Prompt-text?style=flat-square&logo=github%20copilot&labelColor=512a97&color=ecd8ff)
   >
   > ```prompt
   > Ei copilot, como posso criar e publicar uma nova branch Git chamada build-octofit-app?
   > ```

   O modo agente do Copilot responderá e perguntará se você deseja habilitá-lo para executar o comando. Responda com **Sim**</br>

   <img src=https://github.com/user-attachments/assets/8dafaa5f-80db-41ea-a189-b5d603c11d63 width=40% height=40%>

1. Agora que estamos satisfeitos com o comando, pressione o botão `Continuar` para deixar o modo agente do Copilot executá-lo para nós. Não há necessidade de copiar e colar!

1. Após um momento, olhe na barra de status inferior do VS Code, à esquerda, para ver a branch ativa. Deve agora dizer `build-octofit-app`. Se sim, você terminou esta etapa!

1. Agora que sua branch foi enviada para o GitHub, Mona já deve estar ocupada verificando seu trabalho. Dê a ela um momento e fique de olho nos comentários. Você verá ela responder com informações de progresso e a próxima lição.

<details>
<summary>Tendo problemas? 🤷</summary><br/>

Se você não receber feedback, aqui estão algumas coisas para verificar:

- Certifique-se de que criou a branch com o nome exato `build-octofit-app`. Sem prefixos ou sufixos.
- Certifique-se de que a branch foi realmente publicada no seu repositório.

</details>
