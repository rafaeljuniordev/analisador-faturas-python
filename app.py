# Mini Projeto 01 - Analisador de Faturas

# Algoritmo:
# 1. Cadastrar clientes e faturas
# 2. Armazenar os dados em listas
# 3. Classificar cada fatura
# 4. Analisar a situação
# 5. Exibir relatório individual
# 6. Calcular indicadores gerais


def classificar_fatura(valor_fatura):
    if valor_fatura >= 500:
        return 'Fatura de alto valor'
    elif 200 <= valor_fatura <= 499:
        return 'Fatura de valor médio'
    else:
        return 'Fatura de baixo valor'

def analisar_situacao(valor_fatura, status_fatura):
    if valor_fatura > 500 and status_fatura == 'ATRASADA':
        return 'CASO CRÍTICO'
    elif status_fatura == 'ATRASADA' or valor_fatura > 800:
        return 'Necessita de atenção'
    else:
        return 'Regular'

def exibir_relatorio(nome_cliente, valor_fatura, status_fatura, classificacao, situacao):
    print('=== ANÁLISE DA FATURA ===')
    print("Cliente:", nome_cliente)
    print('Valor da fatura:', valor_fatura)
    print('Status:', status_fatura)
    print('Classificação:', classificacao)
    print('Situação:', situacao)

clientes = []
valores_faturas = []
status_faturas = []


for posicao in range(3):
    nome_cliente = input('Nome do cliente:')
    valor_fatura = int(input('Digite o valor da sua fatura:'))
    status_fatura = input('Digite o status da sua fatura:')

    clientes.append(nome_cliente)
    valores_faturas.append(valor_fatura)
    status_faturas.append(status_fatura)   


for posicao in range(len(clientes)):
    classificacao = classificar_fatura(valores_faturas[posicao])
    situacao = analisar_situacao(valores_faturas[posicao], status_faturas[posicao])
    exibir_relatorio(clientes[posicao], valores_faturas[posicao], status_faturas[posicao], classificacao, situacao)


quantidade_atrasadas = 0
valor_total_atrasadas = 0
quantidade_criticas = 0
quantidade_alto_valor = 0


for posicao in range(len(status_faturas)):
    if valores_faturas[posicao] > 500 and status_faturas[posicao] == 'ATRASADA':
        quantidade_criticas += 1

    if status_faturas[posicao] == 'ATRASADA':
        quantidade_atrasadas += 1
        valor_total_atrasadas += valores_faturas[posicao]
    
    if valores_faturas[posicao] >= 500:
        quantidade_alto_valor += 1

quantidade_faturas = len(valores_faturas)
valor_total = sum(valores_faturas)
media_faturas = valor_total / quantidade_faturas

print('=== RELATÓRIO GERAL DE FATURAS ===')
print('Quantidade de faturas:',quantidade_faturas)
print('Valor total:', valor_total)
print('Média das faturas:', media_faturas)
print('Faturas atrasadas:', quantidade_atrasadas)
print('Valor total das faturas atrasadas:', valor_total_atrasadas)
print('Quantidade de casos críticos:', quantidade_criticas)
print('Quantidade de faturas de alto valor:', quantidade_alto_valor)