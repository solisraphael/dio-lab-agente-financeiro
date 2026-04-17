# 🤖 SonIA — Assistente de Planejamento de Compras de Bens

## Contexto

A tomada de decisão financeira ainda é um desafio para grande parte das pessoas, especialmente quando envolve a aquisição de bens de consumo. Muitas decisões são feitas sem análise adequada da renda, dos gastos e da real capacidade financeira, resultando em endividamento e falta de planejamento.

A SonIA surge como uma **agente financeira inteligente**, utilizando IA Generativa para transformar dados financeiros em orientações práticas e personalizadas, sendo capaz de:

- **Antecipar necessidades**, sugerindo estratégias antes mesmo da decisão de compra
- **Personalizar recomendações** com base no perfil, renda e histórico de gastos do cliente
- **Cocriar soluções financeiras**, como planos de poupança, parcelamento e estratégias híbridas
- **Garantir segurança**, evitando respostas genéricas ou informações não baseadas nos dados fornecidos

> [!TIP]
> Este projeto utiliza dados simulados para representar um cliente fictício e demonstrar o funcionamento de um agente financeiro em um cenário real.

---

### 1. Documentação do Agente

A SonIA foi projetada para atuar como uma consultora financeira digital focada em auxiliar clientes a realizar o sonho da aquisição de bens de consumo de forma consciente e controlada.

- **Caso de Uso:** Planejamento financeiro para compra de bens (ex: celulares, TVs, carros), com geração de planos de ação personalizados
- **Persona e Tom de Voz:** Consultora financeira clara, objetiva e didática, com linguagem acessível para usuários leigos
- **Arquitetura:** Sistema baseado em carregamento de dados (perfil, transações e produtos), construção de contexto e envio para modelo LLaMA para geração de resposta
- **Segurança:** Uso exclusivo dos dados fornecidos, regras no system prompt para evitar alucinação e respostas fora do contexto

📄 **Detalhes completos:** [`docs/01-documentacao-agente.md`](./docs/01-documentacao-agente.md)

---

### 2. Base de Conhecimento

A base de conhecimento da SonIA é composta por dados simulados que representam a realidade financeira de um cliente.

| Arquivo | Formato | Descrição |
|---------|---------|-----------|
| `transacoes.csv` | CSV | Histórico de entradas e saídas financeiras do cliente |
| `historico_atendimento.csv` | CSV | Registro de interações anteriores com o agente |
| `perfil_investidor.json` | JSON | Dados pessoais, renda, perfil financeiro e metas |
| `produtos_financeiros.json` | JSON | Lista de produtos financeiros disponíveis com rentabilidade |

Esses dados são utilizados diretamente no prompt, permitindo que o modelo gere respostas personalizadas e contextualizadas.

📄 **Detalhes completos:** [`docs/02-base-conhecimento.md`](./docs/02-base-conhecimento.md)

---

### 3. Prompts do Agente

Os prompts são responsáveis por definir o comportamento da SonIA e garantir respostas consistentes e úteis.

- **System Prompt:** Define regras, comportamento e formato das respostas
- **Exemplos de Interação:** Cenários reais com perguntas e respostas esperadas, incluindo planos de ação com valores e prazos
- **Tratamento de Edge Cases:** Situações como falta de dados ou perguntas fora do escopo são tratadas com respostas seguras e orientativas

A SonIA utiliza prompts estruturados para garantir:
- uso correto dos dados
- respostas seguras
- recomendações práticas e acionáveis

📄 **Detalhes completos:** [`docs/03-prompts.md`](./docs/03-prompts.md)
---

### 4. Aplicação Funcional

Foi desenvolvido um **protótipo funcional da agente SonIA**, capaz de interagir com o usuário e fornecer recomendações financeiras personalizadas.

A aplicação consiste em:
- Chatbot interativo para simulação de conversas com o cliente
- Integração com modelo de linguagem (LLM) executado localmente (LLaMA)
- Utilização de uma base de conhecimento composta por dados de perfil, transações e produtos financeiros
- Geração de respostas estruturadas com análise, recomendação e plano de ação detalhado

📁 **Pasta:** [`src/`](./src/)

---

### 5. Avaliação e Métricas

A qualidade da SonIA foi avaliada com base em testes estruturados e análise do comportamento do agente frente a diferentes cenários financeiros.

**Métricas utilizadas:**
- **Assertividade:** capacidade de responder corretamente com base nos dados fornecidos
- **Segurança:** evitar invenção de informações ou recomendações indevidas
- **Coerência:** alinhamento das respostas com o perfil financeiro do cliente
- **Qualidade do plano de ação:** geração de estratégias práticas com valores e prazos definidos

📄 **Detalhes completos:** [`docs/04-metricas.md`](./docs/04-metricas.md)

---

### 6. Pitch

Foi desenvolvido um pitch apresentando a proposta da SonIA como uma solução para auxiliar usuários na tomada de decisões financeiras conscientes.

O pitch aborda:
- O problema do endividamento e falta de planejamento financeiro
- A solução proposta pela SonIA com recomendações personalizadas
- Demonstração prática do agente em funcionamento
- Diferenciais como geração de planos de ação detalhados

📄 **Pitch completo:** [`docs/05-pitch.md`](./docs/05-pitch.md)
---

## Ferramentas Sugeridas

Todas as ferramentas abaixo possuem versões gratuitas:

| Categoria | Ferramentas |
|-----------|-------------|
| **LLMs** | [ChatGPT](https://chat.openai.com/), [Copilot](https://copilot.microsoft.com/), [Gemini](https://gemini.google.com/), [Claude](https://claude.ai/), [Ollama](https://ollama.ai/) |
| **Desenvolvimento** | [Streamlit](https://streamlit.io/), [Gradio](https://www.gradio.app/), [Google Colab](https://colab.research.google.com/) |
| **Orquestração** | [LangChain](https://www.langchain.com/), [LangFlow](https://www.langflow.org/), [CrewAI](https://www.crewai.com/) |
| **Diagramas** | [Mermaid](https://mermaid.js.org/), [Draw.io](https://app.diagrams.net/), [Excalidraw](https://excalidraw.com/) |

---

## Estrutura do Repositório

```
📁 lab-agente-financeiro/
│
├── 📄 README.md
│
├── 📁 data/                          # Dados mockados para o agente
│   ├── historico_atendimento.csv     # Histórico de atendimentos (CSV)
│   ├── perfil_investidor.json        # Perfil do cliente (JSON)
│   ├── produtos_financeiros.json     # Produtos disponíveis (JSON)
│   └── transacoes.csv                # Histórico de transações (CSV)
│
├── 📁 docs/                          # Documentação do projeto
│   ├── 01-documentacao-agente.md     # Caso de uso e arquitetura
│   ├── 02-base-conhecimento.md       # Estratégia de dados
│   ├── 03-prompts.md                 # Engenharia de prompts
│   ├── 04-metricas.md                # Avaliação e métricas
│   └── 05-pitch.md                   # Roteiro do pitch
│
├── 📁 src/                           # Código da aplicação
│   └── app.py                        # (exemplo de estrutura)
│
├── 📁 assets/                        # Imagens e diagramas
│   └── ...
│
└── 📁 examples/                      # Referências e exemplos
    └── README.md
```

---


