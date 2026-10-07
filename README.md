# Analisador de Faturas em Python

## Sobre o projeto

O objetivo principal deste projeto foi consolidar conceitos básicos de programação e transformar exercícios isolados em um pequeno fluxo completo de processamento de dados.

O projeto foi desenvolvido para praticar fundamentos de Python através de um cenário de análise de faturas.

O programa permite cadastrar várias faturas, armazenar seus dados, classificá-las por valor, identificar situações que precisam de atenção e gerar indicadores gerais sobre os registros cadastrados.

## Funcionalidades

- Cadastro de múltiplas faturas
- Registro do nome do cliente, valor e status da fatura
- Classificação de faturas por faixa de valor
- Identificação de faturas que necessitam de atenção
- Identificação de casos críticos
- Cálculo da quantidade total de faturas
- Cálculo do valor total das faturas
- Cálculo da média dos valores
- Contagem de faturas atrasadas
- Soma do valor total das faturas atrasadas
- Contagem de casos críticos
- Contagem de faturas de alto valor

## Conceitos praticados

- Variáveis
- Tipos de dados
- Condicionais: `if`, `elif` e `else`
- Operadores lógicos: `and` e `or`
- Listas
- `append()`
- `for`
- `range()`
- `len()`
- `sum()`
- Funções
- Parâmetros
- `return`
- `input()`
- Contadores
- Acumuladores
- Relacionamento entre listas através de posições

## Como executar

1. Tenha o Python instalado no computador.
2. Clone ou baixe este repositório.
3. Abra a pasta do projeto.
4. Execute o arquivo principal:

```bash
python app.py
```

## Exemplo de uso

O programa primeiro pergunta quantas faturas serão cadastradas.

Depois, para cada fatura, solicita:
- Nome do cliente
- Valor da fatura
- Status da fatura

Exemplo:

```text
Quantas faturas deseja cadastrar? 2

Nome do cliente: Ana
Digite o valor da sua fatura: 500
Digite o status da sua fatura: PAGA

Nome do cliente: Bruno
Digite o valor da sua fatura: 900
Digite o status da sua fatura: ATRASADA
```

## Tecnologias utilizadas

- Python
- Git
- GitHub
- Visual Studio Code

## Próximas evoluções

- Leitura de dados através de arquivos CSV
- Análise de dados com Pandas
- Integração com banco de dados SQL
- Tratamento de erros e validação das entradas
- Uso de logs
- Automação do processamento das faturas