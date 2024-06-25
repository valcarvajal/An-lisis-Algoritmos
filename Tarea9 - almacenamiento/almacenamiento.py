def maximizar(As, D):
    As = sorted(As, key = lambda tam : tam[1])
    lista, suma = [], 0
    for i in range(len(As)):
        suma += As[i][1]
        if suma <= D:
            lista += [As[i]]
        else:
            break
    return lista

