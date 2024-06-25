def encontrar_ruta(C):
    X = len(C)
    Y = len(C[0])
    R = [[0]*Y for i in range(X)]
    
    def backtracking(x, y):
        if x == X - 1 and y == Y - 1:
            R[x][y] = 1
            return True
        
        if C[x][y] == 1 or R[x][y] == 1:
            return False
        
        R[x][y] = 1
        if x < X - 1 and backtracking(x + 1, y):
            return True
        if y < Y - 1 and backtracking(x, y + 1):
            return True
        if x > 0 and backtracking(x - 1, y):
            return True
        if y > 0 and backtracking(x, y - 1):
            return True
        
        R[x][y] = 0
        return False
    
    if backtracking(0, 0):
        return R
    else:
        return []
