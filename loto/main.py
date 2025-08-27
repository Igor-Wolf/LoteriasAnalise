import csv
from itertools import combinations

# Gera todas as combinações de 15 números entre 1 e 25
combinacoes = combinations(range(1, 26), 15)

# Abre (ou cria) o arquivo CSV para escrita
with open('combinacoes_lotofacil.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)

    # Cabeçalho opcional
    writer.writerow([f'N{i+1}' for i in range(15)])
    
    # Escreve todas as combinações
    for combinacao in combinacoes:
        writer.writerow(combinacao)

print("Arquivo CSV da Lotofácil gerado com sucesso!")
