import os
from langchain_community.utilities import SQLDatabase
from langchain_ollama import OllamaLLM
from langchain_experimental.sql import SQLDatabaseChain
from dotenv import load_dotenv
from llm_split import OllamaLLMSplit

load_dotenv()

SQL_CONNECTION = os.getenv("SQL_CONNECTION")

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
    verbose=True,
    return_direct=True
    )

# Questão do Usuário
question = "Qual produto gerou a maior receita? Retorne os cinco primeiros resultados."

# Gerar e executar consulta SQL
response = db_chain.invoke(
    {"query": question}
)

# Imprimir resposta
print("\nFinal Response:")
print(response)