# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve na SonIA |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Fornecer dados para uma interação continuada, próxima e personalizada|
| `perfil_investidor.json` | JSON | Personalizar as recomendações financeiras de acordo com as caracteristicas do perfil |
| `produtos_financeiros.json` | JSON | Conhecer os produtos da instituição para recomendar as melhores soluções para a demanda atual|
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente para recomendações viaveis de compras  |


---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[Sua descrição aqui]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[ex: Os JSON/CSV são carregados no início da sessão e incluídos no contexto do prompt]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Sua descrição aqui]

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
