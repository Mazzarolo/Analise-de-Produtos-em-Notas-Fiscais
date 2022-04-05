import csv
import editdistance

with open("File3.csv", "r", encoding="utf8") as arq:
    arq_csv = list(csv.reader(arq, delimiter=","))
    max = 0
    refs = 0
    tot = 0
    maxProd = arq_csv[0][1]
    cat = arq_csv[0][2]
    for i, coluna in enumerate(arq_csv):
        if cat != coluna[2] or i + 1 == len(arq_csv):
            print(f'\n\tDistância de Edição Média da Categoria {cat}: {tot / refs}')
            print(f'\tReferência com Maior distância de edição da categoria: {maxProd}, Dintância Média de edição: {max}\n')
            refs = 0
            tot = 0
            max = 0
            maxProd = coluna[1]
        chave = 0
        ref = coluna[1]
        cat = coluna[2]
        for j in range(i):
            if ref == arq_csv[j][1]:
                chave = 1
        if chave == 0:
            refs += 1
            med = 0
            oc = 0
            for j, col in enumerate(arq_csv):
                if ref == arq_csv[j][1]:
                    oc += 1
                    med += editdistance.eval(ref, arq_csv[j][0])
            med = med / oc
            tot += med
            print(f'Categoria: {cat}, Referência: {ref}, Distância Média de Edição: {med}')
            if med > max:
                max = med
                maxProd = coluna[1]
