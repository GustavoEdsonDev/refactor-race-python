## DIAGNÓSTICO INICIAL

1. **Função com muitas responsabilidades:** A função `process_order` faz o cálculo do subtotal, descontos, frete, impostos e pontos de fidelidade, além de imprimir na tela e guardar estados.
2. **Duplicação de código:** O cálculo do subtotal é realizado duas vezes (`total1` e `subtotal`) usando exatamente o mesmo loop `for`.
3. **Condicionais aninhadas:** As regras de desconto de clientes VIP, Funcionário e Regular estão aninhadas de forma desnecessária, em vez de usarem estruturas de decisão mais diretas.
4. **Números e Strings mágicas:** Taxas de imposto, valores de frete e siglas de estados estão escritos diretamente no código, sem o uso de variáveis constantes ou dicionários de mapeamento.
5. **Lógica de busca ineficiente:** A busca por produtos repetidos utiliza dois loops aninhados (`O(n²)`), o que é muito ineficiente e complexo de manter.
6. **Estado Global:** A função modifica uma lista global chamada `ORDERS_PROCESSED`, o que prejudica a testabilidade e cria efeitos colaterais no código.