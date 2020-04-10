def cacaParentes(s):

    props = [i for i in s]

    cacaParentes = []
    for i in range(len(props)):
        if props[i] == "(":
            par = []
            par.append(i)
            cacaParentes.append(par)
            ponteiro_fecha = 1
            jindex = i + 1
            while (jindex < len(props)):
                if props[jindex] == "(":
                    ponteiro_fecha += 1
                    jindex += 1
                elif props[jindex] == ")":
                    ponteiro_fecha -= 1    
                    if ponteiro_fecha == 0:
                        par.append(jindex)
                        jindex = len(props)
                    else:
                        jindex += 1
                else:
                    jindex += 1

    cacaParentes.reverse()
    return cacaParentes

print(cacaParentes("~(pvq^(p^q))"))