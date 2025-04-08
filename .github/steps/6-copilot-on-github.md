## Passo 6: Usando o GitHub Copilot em uma pull request

Parabéns! Você terminou de codificar para este exercício (e VS Code). Agora é hora de mesclar nosso trabalho. :tada: Para finalizar, vamos aprender sobre dois recursos de acesso limitado do Copilot que podem acelerar nossas pull requests!

#### Resumos de Pull Request do Copilot

Normalmente, você revisaria suas anotações e mensagens de commit e, em seguida, as resumiria para a descrição da sua pull request. Isso pode levar algum tempo, especialmente se as mensagens de commit forem inconsistentes ou o código não estiver bem documentado. Felizmente, o Copilot pode considerar todas as mudanças na pull request e fornecer os destaques importantes, e com referências também!

> [!NOTA]  
> Isso não está disponível no nível **Copilot Free**. https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/using-github-copilot-for-pull-requests/creating-a-pull-request-summary-with-github-copilot

#### Revisão do Copilot

Mais olhos em nosso trabalho são sempre úteis, então vamos pedir ao Copilot para fazer uma primeira revisão antes de fazermos um processo normal de revisão por pares. O Copilot é ótimo para detectar erros comuns que podem ser corrigidos com ajustes simples, mas lembre-se de usá-lo de forma responsável.

> [!NOTA]  
> Isso está em **Pré-visualização Pública** para organizações. https://docs.github.com/en/copilot/using-github-copilot/code-review/using-copilot-code-review

### :keyboard: Atividade: Resumir e revisar uma PR com o Copilot

Tanto os **resumos de pull request** quanto a **revisão do copilot** têm acesso limitado, então esta atividade é principalmente opcional. Se você tiver acesso, Mona ficará feliz em verificar seu trabalho! Caso contrário, você pode pular as etapas opcionais.

1. Em um navegador da web, abra outra aba e navegue até o repositório do seu exercício.

1. Você pode notar um **banner de notificação** sugerindo criar uma nova pull request. Clique nele ou use a aba **Pull Requests** no topo para criar uma nova pull request. Por favor, use os seguintes detalhes:

   - **base:** `main`
   - **compare:** `build-octofit-app`
   - **title:** `Adicionar validação de registro e mais atividades`

1. (Opcional) Na área **Adicionar uma descrição**, entre no modo de edição se necessário, depois clique no ícone **Ações do Copilot** e na ação **Resumo**. Após um momento, o Copilot adicionará uma descrição. :memo:

   <img alt="Botão de resumo do Copilot" width="300px" src="https://github.com/user-attachments/assets/3fc5fab4-db03-4ab8-8a16-cdd71ec2ded0">

1. (Opcional) No painel de informações à direita no topo, localize a seção **Revisores** e clique no botão **Solicitar** ao lado de um ícone do **Copilot**. Aguarde um momento para o Copilot adicionar um comentário de revisão à sua pull request!

   <img alt="Botão de revisão do Copilot" width="300px" src="https://github.com/user-attachments/assets/39b15002-a235-4c25-b09d-6a8097e27b62">

   > **Dica:** Observe uma entrada de log que o Copilot foi solicitado para uma revisão.

1. Na parte inferior, pressione o botão **Merge pull request**. Bom trabalho! Você terminou! :tada:

1. Aguarde um momento para Mona verificar seu trabalho, fornecer feedback e postar uma revisão final desta lição!
