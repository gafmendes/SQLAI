# SQL AI Assistant

Faça perguntas sobre as vendas da sua empresa em linguagem natural e receba respostas baseadas diretamente nos dados do PostgreSQL.

O projeto combina [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), [Ollama](https://ollama.com/) e um banco PostgreSQL. O modelo local `codellama` transforma a pergunta em uma consulta SQL, executada pela aplicação através da conexão configurada.

![Interface do SQL AI Assistant](image/image-1791319153059.png)

## Por que usar

- Consulte dados de vendas sem escrever SQL manualmente.
- Execute o modelo localmente com Ollama.
- Use uma interface web simples para perguntas e respostas.
- Mantenha as credenciais do banco fora do código usando variáveis de ambiente.
- Adapte o fluxo a outros bancos compatíveis com SQLAlchemy alterando a URL de conexão.

## Como começar

### Pré-requisitos

- Python 3.10 ou superior.
- PostgreSQL acessível pela máquina que executará o Streamlit.
- [Ollama](https://ollama.com/download) instalado e em execução.
- O modelo `codellama` baixado:

```bash
ollama pull codellama
```

### Instalação

Clone o repositório e crie um ambiente virtual:

```bash
git clone <URL_DO_REPOSITORIO>
cd SQLAI
python -m venv .venv
```

Ative o ambiente virtual.

No PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No macOS/Linux:

```bash
source .venv/bin/activate
```

Instale as dependências do projeto e os pacotes necessários para PostgreSQL e `.env`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install psycopg2-binary python-dotenv
```

> `psycopg2-binary` e `python-dotenv` são usados pelo código atual, mas ainda não estão declarados em `requirements.txt`.

### Configuração

Crie um arquivo `.env` na raiz do projeto. O arquivo já é ignorado pelo Git, portanto não versione credenciais.

```env
SQL_CONNECTION=postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco
```

A URL segue o formato aceito pelo SQLAlchemy. Substitua usuário, senha, host, porta e nome do banco pelos valores do seu ambiente.

### Executar

Inicie a aplicação com:

```bash
streamlit run setup_database.py
```

Abra no navegador o endereço exibido pelo Streamlit, normalmente `http://localhost:8501`, e faça uma pergunta como:

```text
Qual foi o produto que mais vendeu em janeiro de 2026?
```

As tabelas e colunas disponíveis no banco precisam ser compreensíveis para o modelo e conter os dados necessários para responder à pergunta.

## Estrutura do projeto

| Arquivo | Responsabilidade |
| --- | --- |
| `setup_database.py` | Configura o Streamlit, conecta ao banco e executa a cadeia SQL. |
| `llm_split.py` | Personaliza o modelo Ollama para remover cercas de código SQL da resposta. |
| `requirements.txt` | Lista as dependências principais do projeto. |
| `.env` | Guarda configurações locais, como `SQL_CONNECTION`; não deve ser versionado. |

## Onde obter ajuda

Consulte a documentação das ferramentas usadas no projeto:

- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Documentação do LangChain](https://python.langchain.com/docs/)
- [Documentação do Ollama](https://docs.ollama.com/)
- [Documentação do SQLAlchemy](https://docs.sqlalchemy.org/)
- [Documentação do PostgreSQL](https://www.postgresql.org/docs/)

Para relatar um problema ou propor uma melhoria, abra uma issue no repositório com:

- o sistema operacional e a versão do Python;
- a mensagem de erro completa;
- os passos para reproduzir o problema;
- informações sobre o banco e o modelo usado, sem incluir credenciais ou dados sensíveis.

## Contribuição

Contribuições são bem-vindas. Para propor uma mudança:

1. Crie um branch a partir de `main`.
2. Faça uma alteração pequena e focada.
3. Verifique localmente a aplicação com `streamlit run setup_database.py`.
4. Abra um pull request descrevendo o problema e a solução.

Antes de enviar alterações, não inclua `.env`, credenciais, dumps do banco ou dados de clientes. Ainda não há um arquivo `CONTRIBUTING.md` no repositório; as regras específicas de revisão podem ser adicionadas quando o projeto estabelecer um processo formal.

## Licença

Este repositório ainda não contém um arquivo `LICENSE`. Adicione uma licença antes de distribuir o projeto ou aceitar contribuições sob termos definidos.