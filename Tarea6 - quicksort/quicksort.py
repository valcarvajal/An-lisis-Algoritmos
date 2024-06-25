import random
import math

def particion(A, pivote):
    lt = []
    gt = []
    
    for i in range(1, len(A)):
        if A[i] > pivote: gt.append(A[i])
        else: lt.append(A[i])
    
    return lt, pivote, gt

def quicksort(A):
    if len(A) < 2: return A
    
    lt, pivote, gt = particion(A, A[0])
    
    return quicksort(lt) + [pivote] + quicksort(gt)


def quicksort_mejorado(A):
    if len(A) < 2: return A
    
    pivote_rand = random.randint(0, len(A))
    
    lt, pivote, gt = particion(A, math.ceil(sum(A) / len(A)))
    
    return quicksort(lt) + [pivote] + quicksort(gt)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
