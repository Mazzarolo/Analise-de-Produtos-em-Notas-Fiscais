import csv

with open("File3.csv", "r", encoding="utf8") as arq:
    arq_csv = list(csv.reader(arq, delimiter=","))
    refs = 0
    tot = 0
    max = 0
    maxProd = arq_csv[0][1]
    cat = arq_csv[0][2]
    for i, coluna in enumerate(arq_csv):
        # print(f'{i + 1}) Produto: {coluna[0]} Referência: {coluna[1]} Categoria: {coluna[2]}')
        if cat != coluna[2] or i + 1 == len(arq_csv):
            if i + 1 == len(arq_csv):
                tot += 1
                refs += 1
            print(f'Categoria: {cat}, Total de Variações de Produtos: {tot}, Total de Produtos: {refs}, Média: {tot/refs}')
            print(f'\tReferência que mais ocorre na categoria: {maxProd}, Total de Ocorrências: {max}\n')
            tot = 0
            refs = 0
            max = 0
            maxProd = coluna[1]
        tot += 1
        chave = 0
        ref = coluna[1]
        cat = coluna[2]
        for j in range(i):
            if ref == arq_csv[j][1]:
                chave = 1
        if chave == 0:
            refs += 1
            oc = 0
            for j, col in enumerate(arq_csv):
                if ref == arq_csv[j][1]:
                    oc += 1
            if oc > max:
                max = oc
                maxProd = coluna[1]
