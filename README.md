# REFactor Race Python

## EQUIPE

- Integrante 1: [Nome completo]
- Integrante 2: [Nome completo]
- Integrante 3: [Nome completo]
  ...

## PENDÊNCIAS PARA A ENTREGA

### 1. Manter a ordem dos produtos duplicados

A função atual pode alterar a ordem dos produtos duplicados porque utiliza um `set`, que não garante a preservação da ordem original de entrada. É necessário ajustar a função para manter a ordem em que os produtos aparecem na lista original.

### 2. Adicionar os testes que faltam no GitHub

O repositório ainda contém apenas os quatro testes iniciais. É necessário atualizar o arquivo de testes com dois cenários adicionais: frete grátis e cliente funcionário. Dessa forma, a implementação ficará de acordo com o que foi documentado neste README.

### 3. Corrigir o erro de importação dos testes

O arquivo de testes tenta importar o código principal diretamente, mas o módulo está localizado na pasta `src/`. É necessário ajustar a importação no início de `test_checkout.py` para que o Python encontre o módulo corretamente, inclusive em um ambiente configurado do zero.

### 4. Renomear o arquivo de métricas

O arquivo está nomeado como `METRICS.MD`, mas o padrão definido para a entrega é `METRICS.md`. É necessário renomeá-lo e atualizar as métricas com os resultados reais da execução dos testes, incluindo a quantidade de testes aprovados e o percentual de cobertura obtido.

### 5. Criar os arquivos de configuração

É necessário criar os arquivos `.gitignore` e `requirements-dev.txt` na raiz do projeto, conforme a estrutura mínima indicada no enunciado.

O arquivo `requirements-dev.txt` deverá incluir as seguintes ferramentas:

- `pytest`
- `pytest-cov`
-
