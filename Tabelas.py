
def montarTabela(preps):

    colunas = len(preps)

    if (colunas == 0):
        tabela = None
        return tabela

    linhas = int(2 ** colunas)
    Tabela = {i: [] for i in preps}

    k = 0
    for prep in Tabela:
        linha = 0
        grupo = int(2 ** (colunas - (k+1)))
        grupoLinha = int(linhas/grupo)
        for i in range(grupoLinha):
            j=0
            while(j < grupo):
                if (i%2):
                    Tabela[prep].append(False)
                else:
                    Tabela[prep].append(True)
                linha += 1
                j+=1
        k += 1
    return Tabela

def printTabela(Tabela):
    for prep in Tabela:
        print(prep, end="\t\t")
    print('\n')
    for linha in range(len(Tabela["p"])):
        for i in Tabela:
            print(Tabela[i][linha], end="\t\t")
        print('\n')


def coletarPreposicoes(s):
    listaPreps = 'p q r s t'.split(" ")
    preps = []
    for i in range(len(s)):
        if s[i] in listaPreps:
            if s[i] not in preps:
                preps.append(s[i])
    return preps


def avaliarOperacoes(s, opp):

    preps = coletarPreposicoes(s)
    matriz = montarTabela(preps) 

    for i in opp:
        matriz[i] = []

    listaOperaçoes = list(matriz.keys())[len(preps):]
    print(listaOperaçoes)

    for key in listaOperaçoes:

        if ("v" not in key and "^" not in key) and "~" in key:
            prep = key[1]
            matriz[key] = [not i for i in matriz[prep]]

        elif key[-2] == "^" or key[-3] == "^":
            
            if key[-2] == "~":
                prepA = key[:-3]
                prepB = key[-2:]
            else:
                prepA = key[:-2]
                prepB = key[-1:]
            
            andLista = []
            for i in range(len(matriz[prepA])):
                andLista.append(matriz[prepA][i] and matriz[prepB][i])
            matriz[key] = andLista

        elif key[-2] == "v" or key[-3] == "v":

            if key[-2] == "~":
                prepA = key[:-3]
                prepB = key[-2:]
            else:
                prepA = key[:-2]
                prepB = key[-1:]

            orLista = []
            for i in range(len(matriz[prepA])):
                orLista.append(matriz[prepA][i] or matriz[prepB][i])
            matriz[key] = orLista

        elif "-" in key:
            index = key.index("-")
            prepA = key[:index]
            prepB = key[index+2:]

        
    printTabela(matriz)

def checkNegacao(prop, opp):
    i = 0
    while(i < len(prop)):
        if prop[i] == "~":
            prep = prop[i+1]
            opp.append(f"~{prep}")
            prop[i] = f"~{prep}"
            prop.pop(i+1)
        i+=1
    return prop

def checkAndOr(prop, opp):
    i = 0
    while(i < len(prop)):
        if prop[i] == "^" or prop[i] == "v":
            prepA = prop[i-1]
            prepB = prop[i+1]
            opp.append(f"{prepA}{prop[i]}{prepB}")
            prop.insert(i+2, f"{prepA}{prop[i]}{prepB}")
        i+=1

    return prop


def operacoes(s):
    props = [i for i in s]
    opp = []

    if "-" in props:
        index = props.index("-")
        propsA = props[:index]
        propsB = props[index+2:]
        props = []
        props.append(propsA) 
        props.append(propsB) 

        for prop in props:
            prop = checkNegacao(prop, opp)
            prop = checkAndOr(prop, opp)
        
        opp.append(f"{s[:index]}->{s[index+2:]}")

    else:
        props = checkNegacao(props, opp)
        props = checkAndOr(props, opp)

    return opp

    
if __name__ == "__main__":
    logAfirm = input('Digite a afirmação lógica: ')
    operacoes = operacoes(logAfirm)
    avaliarOperacoes(logAfirm, operacoes)
