# Alexa Skill - Status do Metrô de São Paulo

Esta é uma skill da Alexa que informa o status das linhas do Metrô e da CPTM de São Paulo.

## Como funciona

A skill utiliza a API [metro-sp-api](https://github.com/ale-jr/metro-sp-api) para obter o status das linhas em tempo real.

## Como implantar na AWS

1.  **Crie uma função Lambda:**
    *   Acesse o [console da AWS](https://aws.amazon.com/console/).
    *   Vá para o serviço Lambda e crie uma nova função.
    *   Use as seguintes configurações:
        *   **Nome da função:** `metro-sp-status`
        *   **Runtime:** Python 3.9
        *   **Arquitetura:** x86_64
    *   Clique em "Criar função".

2.  **Faça o upload do código:**
    *   Na guia "Código-fonte", clique em "Fazer upload de".
    *   Selecione "Arquivo .zip".
    *   Faça o upload do arquivo `metro-sp-status.zip` que você criou.
    *   Clique em "Salvar".

3.  **Configure o gatilho da Alexa:**
    *   Na guia "Gatilhos", clique em "Adicionar gatilho".
    *   Selecione "Alexa" na lista de gatilhos.
    *   O Alexa Skills Kit será habilitado automaticamente.
    *   Anote o ARN da sua função Lambda. Você precisará dele mais tarde.

4.  **Crie a skill na Amazon Developer Console:**
    *   Acesse o [console de desenvolvedor da Amazon](https://developer.amazon.com/alexa/console/ask).
    *   Clique em "Criar skill".
    *   Use as seguintes configurações:
        *   **Nome da skill:** Status do Metrô de São Paulo
        *   **Idioma padrão:** Português (Brasil)
        *   **Modelo:** Personalizado
        *   **Método de hospedagem:** Provisionado pela AWS
    *   Clique em "Criar skill".
    *   Escolha o modelo "Começar do zero".

5.  **Configure a skill:**
    *   **Invocação:** Defina o nome de invocação da skill como "status do metrô".
    *   **Modelos de interação:**
        *   Vá para o "Editor de JSON" e cole o conteúdo do arquivo `pt-BR.json` que se encontra na raiz do projeto.
        *   Clique em "Salvar modelo".
    *   **Endpoint:**
        *   Selecione "AWS Lambda ARN".
        *   Cole o ARN da sua função Lambda que você anotou anteriormente.
    *   Clique em "Salvar endpoints".

6.  **Teste a skill:**
    *   Vá para a guia "Teste" e ative o teste para "Desenvolvimento".
    *   Use o simulador para testar a skill. Você pode dizer "abrir status do metrô" para iniciar.

## Como criar o pacote de implantação

Para criar o arquivo `metro-sp-status.zip`, siga estas etapas:

1.  Instale as dependências:
    ```bash
    pip install -r requirements.txt -t ./package
    ```
2.  Copie o diretório `src` para o diretório `package`:
    ```bash
    cp -r src ./package
    ```
3.  Copie o arquivo `lambda_function.py` para o diretório `package`:
    ```bash
    cp lambda_function.py ./package
    ```
4.  Compacte o conteúdo do diretório `package` em um arquivo `metro-sp-status.zip`:
    ```bash
    cd package && zip -r ../metro-sp-status.zip . && cd ..
    ```

Agora você pode usar o arquivo `metro-sp-status.zip` para implantar a skill na AWS.
