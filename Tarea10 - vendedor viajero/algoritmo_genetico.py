from typing import List
import random

from dominio_tsp import DominioTSP

def optimizar(dominio: DominioTSP, tam_pobl: int, porc_elite: float, prob_mut: float, reps: int) -> List[int]:
    """Algoritmo genético para optimización estocástica."""
    
    poblacion = dominio.generar_n(tam_pobl)
    
    for _ in range(reps):
        elite_size = int(tam_pobl * porc_elite)
        elite = seleccionar_elite(poblacion, dominio, elite_size)
        nueva_poblacion = elite.copy()
        
        while len(nueva_poblacion) < tam_pobl:
            padre_a = seleccionar_padre(poblacion, dominio)
            padre_b = seleccionar_padre(poblacion, dominio)
            
            hijo = dominio.cruzar(padre_a, padre_b)
            
            if random.random() < prob_mut:
                hijo = dominio.mutar(hijo)
            
            nueva_poblacion.append(hijo)
        
        poblacion = nueva_poblacion
    
    mejor_solucion = elite[0]
    
    for solucion in elite:
        if dominio.fcosto(solucion) < dominio.fcosto(mejor_solucion):
            mejor_solucion = solucion
    
    return mejor_solucion


def seleccionar_elite(poblacion: List[List[int]], dominio: DominioTSP, size: int) -> List[List[int]]:
    """Selecciona la élite de la población basándose en la función de costo."""
    
    poblacion_ordenada = sorted(poblacion, key=lambda x: dominio.fcosto(x))
    
    return poblacion_ordenada[:size]


def seleccionar_padre(poblacion: List[List[int]], dominio: DominioTSP) -> List[int]:
    """Selecciona un padre aleatorio de la población basándose en la ruleta de selección."""
    
    total_fitness = sum(dominio.fcosto(solucion) for solucion in poblacion)
    r = random.uniform(0, total_fitness)
    
    acumulado = 0
    
    for solucion in poblacion:
        fitness = dominio.fcosto(solucion)
        acumulado += fitness
        
        if acumulado >= r:
            return solucion
    
    # Si no se encuentra un padre, se devuelve uno aleatorio
    return random.choice(poblacion)

