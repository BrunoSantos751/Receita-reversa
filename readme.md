# 🔪 Receita Reversa (PromptChef)

## 🎯 Objetivo do Projeto

O **Receita Reversa** é uma aplicação de linha de comando (CLI) desenvolvida em Python que utiliza a Inteligência Artificial do **Google Gemini** para solucionar um problema comum: *o que cozinhar com os ingredientes disponíveis na geladeira?*

Ao invés de pesquisar receitas e comprar ingredientes, o usuário fornece os ingredientes que *já tem*, e a IA atua como um "Chef IA", gerando uma receita original e completa, no formato passo a passo, otimizando o uso do que está disponível.

## ⚙️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Linguagem:** Python | Linguagem principal para o desenvolvimento do script CLI. |
| **API de IA:** Google Gemini | O modelo `gemini-2.5-flash` é usado para gerar o conteúdo da receita. |
| **Gestão de Variáveis:** `python-dotenv` | Garante que a chave da API (secreta) seja carregada de forma segura através do arquivo `.env`. |
| **Versionamento:** Git & GitHub | Controle de versão e publicação do projeto. |

---

## 🚀 Como Executar Localmente

Siga os passos abaixo para configurar e rodar o projeto em sua máquina..

### 1. Clonar o Repositório

```bash
git clone [https://github.com/SEU_USUARIO/ReceitaReversa.git](https://github.com/SEU_USUARIO/ReceitaReversa.git)
cd ReceitaReversa
```

### 2. Instalar Dependências

Instale todas as bibliotecas necessárias listadas no requirements.txt:

```bash
pip install -r requirements.txt
```

### 3. Configuração da Chave da API (Requisito Obrigatório)
O projeto requer uma chave de API válida do Google Gemini para funcionar. Sem esta chave, o script não fará a chamada à API e não funcionará.

-    Obtenha sua chave no [Google AI Studio ([Link para Obter Chave](https://ai.google.dev/api))].

-    Crie um novo arquivo chamado .env na raiz do projeto.

-    Copie o conteúdo do .env.example para o .env e insira sua chave secreta, substituindo o texto entre aspas:

-   Conteúdo do .env:
-   
```bash
GEMINI_API_KEY="SUA_CHAVE_SECRETA_AQUI"
```

### 4. Execução do Programa

Com o ambiente ativado e a chave configurada, execute o script principal:

```bash
python app.py
```
programa solicitará interativamente as informações necessárias para gerar a receita:

-    Lista de ingredientes (Obrigatório)

-    Tempo máximo de preparo (Opcional)

-    Tipo de prato (Opcional)

A IA retornará a receita formatada em Markdown diretamente no seu terminal.


## 🏗️ Estrutura e Organização do Código

O código em `app.py` é estruturado em funções para clareza e manutenção, seguindo boas práticas de organização:

  * `obter_input_usuario()`: Responsável por coletar as entradas do usuário.
  * `construir_prompt()`: Monta a string de instrução detalhada (*prompt engineering*) enviada à API, incorporando as variáveis do usuário.
  * `gerar_receita()`: Gerencia a autenticação através do `.env` e faz a requisição real para o modelo `gemini-2.5-flash`.
  * `main()`: Orquestra o fluxo principal do programa.

