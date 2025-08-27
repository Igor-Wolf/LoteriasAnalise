import csv
from itertools import combinations

# Gera todas as combinações de 6 números entre 1 e 60
combinacoes = combinations(range(1, 61), 6)

# Abre (ou cria) o arquivo CSV para escrita
with open('combinacoes_mega_sena.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    
    # Escreve um cabeçalho opcional
    writer.writerow(['N1', 'N2', 'N3', 'N4', 'N5', 'N6'])
    
    # Escreve todas as combinações
    for combinacao in combinacoes:
        writer.writerow(combinacao)

print("Arquivo CSV gerado com sucesso!")
