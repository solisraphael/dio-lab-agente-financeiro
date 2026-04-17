# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve na SonIA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Fornecer dados para uma interação continuada, próxima e personalizada|
| `perfil_investidor.json` | JSON | Personalizar as recomendações financeiras de acordo com as caracteristicas do perfil |
| `produtos_financeiros.json` | JSON | Conhecer os produtos da instituição para recomendar as melhores soluções para a demanda atual|
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para recomendações viaveis de compras  |

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos CSV e JSON são carregados no início da sessão e convertidos em texto estruturado para serem utilizados diretamente no prompt do modelo.

Exemplo:

```python
import json
import pandas as pd

transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('/data/historico_atendimento.csv')
perfil = json.load(open('./data/perfil_investidor.json'))
produtos = json.load(open('./data/produtos_financeiros.json'))
```

### Como os dados são usados no prompt?
Todos os dados do cliente e produtos são incluídos diretamente no prompt como contexto fixo, permitindo que o modelo tenha acesso completo às informações durante a geração da resposta.

Exemplo:

```python
def montar_prompt(pergunta, perfil, transacoes, produtos):
    return f"""
Você é a SonIA, uma especialista em planejamento financeiro.

[DADOS DO CLIENTE]
Nome: {perfil["nome"]}
Idade: {perfil["idade"]}
Renda: {perfil["renda"]}
Perfil: {perfil["perfil"]}
Metas: {perfil["metas"]}

[TRANSAÇÕES]
{transacoes}

[PRODUTOS FINANCEIROS]
{produtos}

Pergunta do cliente:
{pergunta}
"""

prompt = montar_prompt(
    "Posso comprar um celular de 2000?",
    perfil,
    transacoes,
    produtos
)
```
---

## Exemplo de Contexto Montado

Abaixo está um exemplo de como os dados são formatados e enviados ao agente:

```
Você é a SonIA, uma especialista em planejamento financeiro.

[DADOS DO CLIENTE]
Nome: João Silva
Idade: 35
Renda: 3000
Perfil: moderado
Metas: comprar um carro

[TRANSAÇÕES]
01/11 - Supermercado - Alimentação - 450 - saída
03/11 - Streaming - Entretenimento - 55 - saída
05/11 - Salário - Renda - 3000 - entrada
10/11 - Energia - Contas - 200 - saída

[PRODUTOS FINANCEIROS]

Poupança: rentabilidade 0.5% ao mês
CDB: rentabilidade 0.8% ao mês
Crédito pessoal: juros 2% ao mês

Pergunta do cliente:
Posso comprar um celular de 2000?
```
