def contar_rutas_mas_cortas(C):
    X= len(C)
    Y= len(C[0])
    if X == 0 or Y == 0:
        return 0
    if C[0][0] == 1:
        return 0
    if C[1][0] == 1 and C[0][1] == 1:
        return 0
    for i in range(0,X):
        if C[i][0] == 0:
            C[i][0] = 1
        else:
            C[i][0] = 0
    for j in range(1, Y):
        if C[0][j] == 0:
            C[0][j] = 1
        else:
            C[0][j] = 0
    for i in range(1, X):
        for j in range(1, Y):
            if C[i][j] != 1:
                C[i][j] = C[i - 1][j] + C[i][j - 1]
            else:
                C[i][j] = 0
    return C[X-1][Y - 1]
