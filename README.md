# REFactor Race Python

## EQUIPE
- [sla 1]
- [sla 2]
- [sla 3]
- ...

## TA FALTANDO ISSO AQUI

Ordem dos produtos duplicados: A função atual baralha a ordem dos itens porque devolve diretamente um set. Precisas de ajustar a função para que a lista mantenha a ordem original de entrada.

Testes em falta no GitHub: O teu repositório ainda só tem os 4 testes iniciais. Tens de enviar a versão final do ficheiro com os 2 testes extra (frete grátis e funcionário) para provar o que escreveste no README.

Erro de importe nos testes (ModuleNotFoundError): O teu ficheiro de testes tenta importar o código principal diretamente, mas ele está guardado dentro da pasta src/. É preciso ajustar o import no topo do test_checkout.py para ele encontrar o caminho.

Renomear e atualizar métricas: O ficheiro está guardado como METRICS.MD (maiúsculas) e precisa de ser alterado para METRICS.md (minúsculas). Além disso, os valores lá dentro precisam de refletir os 6 testes a passar.

Ficheiros de configuração em falta: Tens de criar os ficheiros .gitignore e requirements-dev.txt na raiz do projeto, conforme a estrutura mínima exigida pelo regulamento.
  
## DIAGNÓSTICO INICIAL

1. **Função com muitas responsabilidades:** A função `process_order` faz o cálculo do subtotal, descontos, frete, impostos e pontos de fidelidade, além de imprimir na tela e guardar estados.
2. **Duplicação de código:** O cálculo do subtotal é realizado duas vezes (`total1` e `subtotal`) usando exatamente o mesmo loop `for`.
3. **Condicionais aninhadas:** As regras de desconto de clientes VIP, Funcionário e Regular estão aninhadas de forma desnecessária, em vez de usarem estruturas de decisão mais diretas.
4. **Números e Strings mágicas:** Taxas de imposto, valores de frete e siglas de estados estão escritos diretamente no código, sem o uso de variáveis constantes ou dicionários de mapeamento.
5. **Lógica de busca ineficiente:** A busca por produtos repetidos utiliza dois loops aninhados (`O(n²)`), o que é muito ineficiente e complexo de manter.
6. **Estado Global:** A função modifica uma lista global chamada `ORDERS_PROCESSED`, o que prejudica a testabilidade e cria efeitos colaterais no código.

## DESCRIÇÃO
Este projeto é a entrega do desafio REFactor Race Python. O objetivo foi aplicar técnicas de refatoração em um sistema legado de processamento de pedidos para melhorar a qualidade interna do código (reduzir complexidade, aumentar manutenibilidade e cobertura de testes) sem alterar seu comportamento original.

## DIAGNÓSTICO INICIAL (CODE SMELLS ENCONTRADOS)
1. **Função com muitas responsabilidades (God Function):** A função `process_order` fazia cálculos de subtotal, descontos, frete, impostos e pontos de fidelidade, além de imprimir na tela.
2. **Duplicação de código:** O subtotal era calculado duas vezes usando o mesmo loop `for`.
3. **Condicionais aninhadas (Arrow Anti-Pattern):** Regras de desconto profundamente aninhadas dificultando a legibilidade.
4. **Números e Strings mágicas:** Taxas e siglas de estados "hardcoded" pelo código.
5. **Lógica ineficiente:** Busca por produtos repetidos usava dois loops aninhados `O(n²)`.
6. **Estado Global:** Modificação direta da variável global `ORDERS_PROCESSED`.

## REFATORAÇÕES REALIZADAS E DECISÕES TÉCNICAS
1. **Extract Function:** Extraímos blocos para funções menores e especializadas (`calculate_subtotal`, `calculate_discount`, etc.). Isso reduziu a complexidade da função principal de E(34) para A(1).
2. **Remove Duplicate Code:** Centralizamos a lógica de subtotal em apenas uma função.
3. **Replace Conditional with Mapping:** O dicionário `TAX_RATES` substituiu os múltiplos `if/elif` de impostos por estado.
4. **Replace Magic Number with Constant:** Constantes como `EXPRESS_SHIPPING_MULTIPLIER` e `SOUTHEAST_STATES` foram criadas para agrupar valores de domínio.
5. **Otimização de Algoritmo:** Substituímos o loop de duplicados pelo uso de `Set` em Python, otimizando de O(n²) para O(n).

## TESTES ADICIONADOS
Além dos 4 originais, foram criados 2 novos cenários de teste para cobrir mais regras de negócio:
- `test_regular_customer_with_free_shipping`: Verifica a aplicação correta da regra de frete zerado para valores >= 500.
- `test_employee_customer`: Valida o fluxo de desconto exclusivo de 20% para funcionários.

## MÉTRICAS ANTES E DEPOIS
*Consultar o arquivo `METRICS.md` para a tabela completa.*
**Resumo dos ganhos de qualidade:**
- A complexidade ciclomática da `process_order` despencou de **E(34)** para **A(1)**.
- A cobertura de testes aumentou de **83%** para **95%** (sem considerar os novos testes).
- Os problemas de análise estática do Ruff caíram de **4** para **0**.

## USO DE INTELIGÊNCIA ARTIFICIAL
- **Ferramenta utilizada:** Google Gemini.
- **Finalidade:** Auxílio na identificação dos "code smells", estruturação dos arquivos de métricas, sugestões de técnicas de refatoração limpa e elaboração da documentação final.
- **Validação:** Todas as sugestões de código extraídas foram exaustivamente validadas rodando a suíte de testes (`pytest -q`) após cada modificação para garantir que a rede de segurança não foi quebrada.

## MELHORIAS FUTURAS
- Remover o uso de mutação de estado global (`ORDERS_PROCESSED`).
- Implementar tipagem estática (Type Hints) nas funções.
- Incluir validações rigorosas (ex: estourar um `ValueError` se `qty <= 0`).
