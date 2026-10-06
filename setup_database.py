import os
import streamlit as st
from langchain_community.utilities import SQLDatabase
from langchain_ollama import OllamaLLM
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv
from llm_split import OllamaLLMSplit

load_dotenv()

SQL_CONNECTION = os.getenv("SQL_CONNECTION")

# Configuração da página Streamlit
st.set_page_config(page_title="SQL AI Assistant", page_icon=":bar_chart:", layout="centered")

# Conectar ao banco de dados PostgreSQL
# Certifique-se de ter um banco de dados PostgreSQL configurado com as credenciais corretas
db = SQLDatabase.from_uri(
    SQL_CONNECTION
)

# Carregar modelo Ollama
# Usamos temperature = 0 pois queremos o modelo determinístico e preciso
llm = OllamaLLMSplit(
    model = "codellama",
    temperature = 0
)

# Criar SQL chain
db_chain = SQLDatabaseChain.from_llm(
    llm = llm,
    db = db,
    verbose=False,
    return_direct=True
    )

# Questão do Usuário
#question = "Qual produto gerou a maior receita? Retorne os cinco primeiros resultados."

# Streamlit interface
st.title("SQL AI Assistant")
st.markdown("Faça perguntas sobre as suas vendas em linguagem natural e obtenha respostas diretamente do banco de dados.")
question = st.text_input(
    "Faça pergunta sobre dados da sua empresa:",
    placeholder = "Ex: Qual foi o produto que mais vendeu?"
    )

if question:
    with st.spinner("Processando sua pergunta..."):
        try:
            # Gerar e executar consulta SQL
            response = db_chain.invoke(
                {
                    "query": question
                }
            )

            # Imprimir resposta
            st.subheader("IA Resposta:")
            st.success(f"Resposta: {response}")
            
        except Exception as e:
            st.error(f"Ocorreu um erro ao processar sua pergunta: {e}")
            st.info("Certifique-se de que a pergunta está relacionada aos dados disponíveis no banco de dados.")
        
        




# Gerar e executar consulta SQL
response = db_chain.invoke(
    {"query": question}
)

# Imprimir resposta
print("\nFinal Response:")
print(response)