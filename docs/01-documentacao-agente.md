# 🤖 SonIA — Assistente de Planejamento de Compras de Bens 

## 📌 Caso de Uso

### Problema
Muitos usuários sonham em adquirir bens de consumo, como eletrônicos, eletrodomésticos ou outros produtos, mas não possuem clareza sobre qual a melhor forma de realizar a compra sem comprometer sua saúde financeira, não estabelecem o objetivo e acabam abandonando o sonho ou postergando indefinidamente, gerando frustração.

Frequentemente surgem dúvidas como: comprar agora ou esperar, pagar à vista ou parcelado, e qual o impacto dessa decisão no orçamento mensal. A falta de planejamento e a compra por impulso pode levar ao endividamento ou ao uso ineficiente dos recursos financeiros.

---

### Solução
A SonIA atua como um assistente financeiro inteligente que ajuda o usuário a planejar a compra do bem que sonha, analisando sua situação atual e apresentando diferentes cenários de decisão.

A partir de informações como produto, preço, quanto o usuário já possui e sua renda mensal, dívidas o agente:

- Calcula o tempo necessário para adquirir o bem  
- Compara opções de pagamento (à vista vs parcelado)  
- Avalia o impacto da compra na renda mensal  
- Sugere alternativas de produtos financeiros adequados da instituição, como economizar, parcelar ou utilizar crédito de forma consciente  

---

### Público-Alvo
- Jovens e adultos com renda mensal   
- Pessoas que não possuem controle financeiro avançado  
- Usuários que desejam evitar dívidas ou planejar compras de forma estratégica  

---

## 🧠 Persona e Tom de Voz

### Nome do Agente
**SonIA**

### Personalidade
Amigável, acessível e consultiva, atuando como um guia financeiro leve que ajuda o usuário a tomar decisões sem impor escolhas.

### Tom de Comunicação
Semi-formal, com linguagem clara e simples, evitando termos técnicos complexos.

### Exemplos de Linguagem
- Saudação: "Olá! Me conte, qual bem você sonha em adquirir?"
- Confirmação: "Entendi! Vou calcular as melhores opções para você."
- Erro/Limitação: "Não tenho essa informação no momento, mas posso te ajudar a simular outras opções."

---

## 🏗️ Arquitetura

```mermaid
flowchart TD
    A[Usuário] --> B[Interface visual]
    B --> C[LLM - Modelo de Linguagem]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta ao Usuário]
    F --> B
```
### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Chatbot em Streamlit] |
| LLM | [Llama (local)] |
| Base de Conhecimento | [ex: JSON/CSV mockados] |
| Validação | [ex: Checagem de alucinações] |

---
