# Avaliação e Métricas


A avaliação foi realizada utilizando duas abordagens complementares:

1. **Testes estruturados:** Cenários com perguntas específicas e validação das respostas esperadas;
2. **Feedback simulado:** Avaliação qualitativa com base no comportamento esperado de um consultor financeiro.

---

## Métricas de Qualidade

| Métrica | O que avalia | Resultado obtido |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu corretamente com base nos dados? | 4.5 / 5 |
| **Segurança** | O agente evitou inventar informações? | 5 / 5 |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | 4.8 / 5 |

> Observação: O agente apresentou alta consistência ao utilizar os dados fornecidos, com respostas alinhadas ao perfil financeiro e evitando recomendações arriscadas.

---

## Exemplos de Cenários de Teste

### Teste 1: Planejamento de compra

- **Pergunta:** "Posso comprar um celular de 2000?"
- **Resposta esperada:** Análise da capacidade financeira + plano de ação com poupança ou parcelamento
- **Resultado:** ✔ Correto

---

### Teste 2: Estratégia de poupança

- **Pergunta:** "Quero comprar algo de 2000, o que faço?"
- **Resposta esperada:** Plano com valor mensal e tempo estimado de poupança
- **Resultado:** ✔ Correto

---

### Teste 3: Recomendação baseada no perfil

- **Pergunta:** "Vale a pena parcelar uma compra?"
- **Resposta esperada:** Resposta considerando perfil (ex: conservador → evitar risco)
- **Resultado:** ✔ Correto

---

### Teste 4: Pergunta fora do escopo

- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Informar que o agente é especializado em finanças
- **Resultado:** ✔ Correto

---

### Teste 5: Dados insuficientes

- **Pergunta:** "Posso financiar um carro?"
- **Resposta esperada:** Solicitar mais informações antes de recomendar
- **Resultado:** ✔ Correto

---

## Resultados

**O que funcionou bem:**
- Uso consistente dos dados do cliente para tomada de decisão
- Geração de planos de ação detalhados com valores e prazos
- Respostas alinhadas ao perfil financeiro (conservador, moderado)
- Boa capacidade de evitar respostas fora do contexto
- Estrutura de resposta clara (Análise, Recomendação, Sugestões)

**O que pode melhorar:**
- Refinar cálculos financeiros para cenários mais complexos
- Considerar rendimentos de investimentos de forma mais precisa
- Melhorar respostas em casos com dados incompletos
- Incluir comparações entre múltiplas estratégias (ex: à vista vs parcelado vs investir)

---

## Métricas Avançadas (Opcional)

Durante os testes, foram observados os seguintes aspectos técnicos:

- **Tempo de resposta:** médio entre 1 a 3 segundos por interação
- **Consumo de tokens:** moderado, devido ao envio completo de contexto no prompt
- **Taxa de erro:** baixa, com respostas consistentes na maioria dos testes

Para projetos mais robustos, ferramentas como **LangWatch** e **LangFuse** podem ser utilizadas para monitoramento detalhado de performance, logs e comportamento do modelo.
