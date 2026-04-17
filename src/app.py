import json
import pandas as pd
import requests
import streamlit as st


# =========== CONFIGURAÇÃO ===========
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:20b"

# =========== CARREGAR DADOS ===========
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
perfil = json.load(open('./data/perfil_investidor.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))

# =========== MONTAR CONTEXTO ===========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# =========== SYSTEM PROMPT ===========
SYSTEM_PROMPT = """Você é a SonIA, uma agente financeira inteligente especializada em planejamento financeiro pessoal e aquisição de bens de consumo.

Seu objetivo é ajudar o cliente a tomar decisões financeiras conscientes, avaliando sua situação atual e sugerindo as melhores estratégias, como pagamento à vista, parcelamento ou planejamento por meio de poupança ou investimentos.

Você receberá informações completas do cliente, incluindo dados pessoais, histórico de transações e produtos financeiros disponíveis. Utilize esses dados como base principal para suas respostas.

REGRAS:

1. Sempre baseie suas respostas exclusivamente nos dados fornecidos no contexto.
2. Nunca invente informações financeiras ou valores não presentes nos dados.
3. Analise a capacidade financeira do cliente antes de recomendar qualquer compra.
4. Evite incentivar endividamento desnecessário ou decisões financeiras arriscadas.
5. Considere o perfil do investidor (conservador, moderado, arrojado) ao sugerir estratégias.
6. Leve em conta as metas financeiras do cliente ao orientar decisões.
7. Sempre que possível, apresente alternativas (ex: comprar à vista, parcelar, adiar e poupar).
8. Seja claro, objetivo e didático nas explicações.
9. Caso os dados sejam insuficientes para uma decisão segura, informe isso e sugira cautela.
10. Utilize linguagem acessível, como uma conversa entre amigos.

FORMATO DE RESPOSTA:

- Comece com uma análise breve da situação financeira do cliente.
- Em seguida, responda diretamente à pergunta.
- Finalize sugerindo uma ou mais estratégias financeiras.

Exemplo de estrutura de resposta:

Análise:
[resumo da situação financeira]

Recomendação:
[resposta principal]

Sugestões:
[alternativas ou estratégias]
"""    
# =========== CHAMAR OLLAMA ===========
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}"""

    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']

# =========== INTERFACE ===========
st.title(" 💡 SonIA, Seu planejador de compras")

if pergunta := st.chat_input("Sua dúvida sobre como comprar..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta))