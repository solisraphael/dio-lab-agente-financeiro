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

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos CSV e JSON são carregados no início da sessão e convertidos em estruturas de dados em memória para acesso rápido.

Exemplo:

```python
import json
import csv

def carregar_csv(caminho):
    with open(caminho, 'r') as f:
        return list(csv.DictReader(f))

def carregar_json(caminho):
    with open(caminho, 'r') as f:
        return json.load(f)

transacoes = carregar_csv("transacoes.csv")
historico = carregar_csv("historico_atendimento.csv")
perfil = carregar_json("perfil_investidor.json")
produtos = carregar_json("produtos_financeiros.json")
```

### Como os dados são usados no prompt?
Os dados não são inseridos integralmente no prompt. Eles são filtrados e organizados conforme a necessidade da interação, sendo injetados dinamicamente como contexto.

Exemplo:

```python
def montar_contexto(perfil, transacoes):
    renda = perfil["renda"]
    gastos = sum(float(t["valor"]) for t in transacoes if t["tipo"] == "saida")

    return f"""
[PERFIL]
Renda: {renda}
Perfil: {perfil["perfil"]}

[FINANÇAS]
Gastos mensais: {gastos}
Saldo estimado: {renda - gastos}
"""

def montar_prompt(pergunta, contexto):
    return f"""
Você é a SonIA, uma especialista em planejamento financeiro.

{contexto}

Pergunta do cliente:
{pergunta}
"""

contexto = montar_contexto(perfil, transacoes)
prompt = montar_prompt("Posso comprar um celular de 2000?", contexto)

resposta = modelo.generate(prompt)
```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000

Últimas transações:
- 01/11: Supermercado - R$ 450
- 03/11: Streaming - R$ 55
...
```
