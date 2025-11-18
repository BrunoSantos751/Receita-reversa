import os
from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

# 1. Carregar variáveis de ambiente do arquivo .env
load_dotenv()

def obter_input_usuario():
    """Coleta os dados necessários do usuário via linha de comando."""
    print("--- 🔪 RECEITA REVERSA: Seu Chef AI ---")
    
    # Input obrigatório
    ingredientes = input("🥕 1. Liste todos os ingredientes disponíveis (separados por vírgula): ")
    if not ingredientes:
        print("❌ Os ingredientes são obrigatórios. Tente novamente.")
        return None, None, None

    # Inputs opcionais
    tempo_maximo = input("⏰ 2. Tempo máximo de preparo que você tem (ex: 45 minutos): ")
    tipo_prato = input("🍽️ 3. Tipo de prato desejado (ex: Jantar rápido, Sobremesa, Vegano): ")
    
    return ingredientes, tempo_maximo, tipo_prato

def construir_prompt(ingredientes, tempo_maximo, tipo_prato):
    """Monta a string do prompt de instrução para a API."""
    
    # Define valores padrão se os campos opcionais estiverem vazios
    tempo_maximo_str = tempo_maximo if tempo_maximo else "Não há restrição de tempo."
    tipo_prato_str = tipo_prato if tipo_prato else "Qualquer tipo de prato criativo."
    
    prompt = f"""
    Você é um chef de cozinha de Inteligência Artificial, especialista em criar receitas a partir de ingredientes limitados( ).
    
    Baseado nas informações abaixo, crie UMA ÚNICA receita completa e original, que utilize a maior parte dos ingredientes fornecidos.
    
    ***
    INGREDIENTES DISPONÍVEIS: {ingredientes}
    TEMPO MÁXIMO DE PREPARO: {tempo_maximo_str}
    TIPO DE PRATO DESEJADO: {tipo_prato_str}
    ***
    
    A sua resposta deve seguir RIGOROSAMENTE a seguinte estrutura em Markdown, sem texto adicional antes ou depois:
    
    ## 🍽️ [NOME CRIATIVO DA RECEITA]
    
    ### ⏰ Tempo Total: [VALOR ESTIMADO]
    
    ### 🥕 Ingredientes
    * [Lista completa dos ingredientes e quantidades necessárias]
    
    ### 👩‍🍳 Modo de Preparo
    1. [Passo 1]
    2. [Passo 2]
    3. [Passo 3]
    [Continue a lista de passos...]
    
    ### 💡 Nota do Chef
    [Breve sugestão de acompanhamento ou substituição.]
    """
    return prompt.strip()

def gerar_receita(prompt):
    """Conecta-se à API do Gemini e gera a receita."""
    
    # Tenta obter a chave da API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("\n❌ ERRO: A chave da API (GEMINI_API_KEY) não foi encontrada no arquivo .env.")
        print("Por favor, verifique se você criou o arquivo .env e inseriu a chave corretamente.")
        return

    try:
        # Inicializa o cliente Gemini
        cliente = genai.Client(api_key=api_key)
        
        # Chama a API
        print("\n✨ Gerando sua receita reversa... Aguarde um momento.")
        
        # Escolhe um modelo adequado para geração de texto (como gemini-2.5-flash)
        response = cliente.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config={"temperature": 0.8} # Temperatura mais alta incentiva a criatividade
        )
        
        # Imprime o resultado formatado
        print("\n" + "="*50)
        print("✅ RECEITA PRONTA!")
        print(response.text)
        print("="*50)
        
    except APIError as e:
        print(f"\n❌ ERRO da API: Não foi possível conectar ou gerar o conteúdo. Detalhes: {e}")
    except Exception as e:
        print(f"\n❌ Um erro inesperado ocorreu: {e}")


def main():
    """Função principal que orquestra o fluxo do programa."""
    
    ingredientes, tempo_maximo, tipo_prato = obter_input_usuario()
    
    if ingredientes:
        prompt = construir_prompt(ingredientes, tempo_maximo, tipo_prato)
        # Opcional: Descomente a linha abaixo para ver o prompt exato enviado à API
        # print("\n--- PROMPT ENVIADO ---\n", prompt, "\n----------------------")
        gerar_receita(prompt)

if __name__ == "__main__":
    main()