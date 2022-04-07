import csv
import editdistance

TOP = 3

with open("File4.csv", "r", encoding="utf8") as arq:
    arq_csv = list(csv.reader(arq, delimiter=","))
    refs = 0
    tot = 0
    cat = arq_csv[0][2]
    print(f'\nTOP {TOP}\n')
    for i, coluna in enumerate(arq_csv):
        if cat != coluna[2] or i + 1 == len(arq_csv):
            print(f'\n\tPorcentagem de acerto Médio da Categoria {cat}: {tot / refs}%\n')
            refs = 0
            tot = 0
        top = TOP
        chave = 0
        ref = coluna
        cat = coluna[2]
        for j in range(i):
            if ref[1] == arq_csv[j][1]:
                chave = 1
        if chave == 0:
            refs += 1
            str = ""
            tops = [ref]
            percent = 0
            for j in range(top):
                max = 0
                topWord = ref
                oc = 0
                for k, col in enumerate(arq_csv):
                    key = 0
                    for word in tops:
                        if word[0] == col[0]:
                            key = 1
                    if key == 0 or j == 0:
                        aux = (1 - editdistance.eval(ref[1], col[0])/min(len(ref[1]), len(col[0])))
                        if aux > max:
                            max = aux
                            topWord = col
                        elif aux == max:
                            if col[1] == ref[1] and topWord[1] != ref[1]:
                                max = aux
                                topWord = col
                    if col[1] == ref[1]:
                        oc += 1
                if j == 0:
                    tops[0] = topWord
                else:
                    tops.append(topWord)
                ocTop = 0
                for word in tops:
                    if word[1] == ref[1]:
                        ocTop += 1
                if ocTop == oc:
                    top = len(tops)
                    break
            for j, word in enumerate(tops):
                str += word[0]
                if j + 1 != len(tops):
                    str += ","
                if word[1] == ref[1]:
                    percent += 1
            percent = (percent * 100) / len(tops)
            tot += percent
            #print(f'Categoria: {cat}, Referência: {ref[1]}, Porcentagem de acerto: {percent}%')
            #print(f'\tTop {top}: {str}')
