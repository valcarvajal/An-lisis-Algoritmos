import csv
import random
from typing import List


class DominioTSP():
    """
    Esta clase modela el dominio del problema del Vendedor Viajero para su resolución
    con algoritmos probabilísticos.
    
    ... (el código anterior se mantiene igual) ...
    """

    # matriz de adyacencia del grafo, contiene las distancias entre ciudades
    __matriz_ady = []

    # mapeo de nombres de ciudad (en hilera) y su representación numérica correspondiente
    __ciudades_números = {}

    # mapeo de representaciones numéricas de ciudades (índice de la lista) y nombres de ciudad (en hilera)
    __números_ciudades = []

    # contiene el número que representa a la correspondiente ciudad de inicio
    __ciudad_inicio = -1

    # número de ciudades en el grafo
    __n = -1    

    def __init__(self, ciudades_rutacsv: str, ciudad_inicio: str) -> None:
        """Construye un objeto de modelo de dominio para una instancia
        específica del problema del vendedor viajero.

        Entradas:
        ciudades_rutacsv (str)
            Ruta al archivo csv que contiene la matriz de pesos entre las ciudades
            para las que se quiere resolver el problema del vendedor viajero.

        ciudad_inicio (str)
            Nombre de la ciudad que será el inicio y fin del circuito a calcular.

        Salidas:
            Una instancia de DominioTSP correctamente inicializada.
        """

        with open(ciudades_rutacsv, 'r') as archivo_csv:
            lector = csv.reader(archivo_csv, delimiter=',')
            primera_fila = True
            número_ciudad = 0
            for fila in lector:
                if primera_fila:
                    self.__números_ciudades = fila[1:]
                    primera_fila = False
                else:
                    ciudad = fila[0]
                    if ciudad == ciudad_inicio:
                        self.__ciudad_inicio = número_ciudad

                    self.__ciudades_números[ciudad] = número_ciudad
                    número_ciudad += 1

                    self.__matriz_ady.append([float(w) for w in fila[1:]])

            self.__n = len(self.__números_ciudades)

    def validar(self, sol: List[int]) -> bool:
        """Valida que la solución dada cumple con los requisitos del problema.

        Si n es el número de ciudades en el grafo, la solución debe:
        - Tener tamaño (n-1)
        - Contener sólo números enteros menores que n (las ciudades se numeran de 0 a (n-1))
        - No contener elementos repetidos
        - No contener la ciudad de inicio/fin del circuito

        Entradas:
        sol (List[int])
            La solución a validar.

        Salidas:
        (bool) True si la solución es válida, False en cualquier otro caso
        """

        # sol debe representar un camino completo
        if len(sol) != (self.__n - 1):
            return False

        for ciudad in sol:
            # sol no debe contener a la ciudad de inicio
            if ciudad == self.__ciudad_inicio:
                return False

            # sol no debe contener ciudades que no estén en el grafo
            if ciudad >= self.__n:
                return False

        # sol no debe contener duplicados
        if len(sol) != len(set(sol)):
            return False

        return True

    def texto(self, sol: List[int]) -> str:
        """Construye una representación en hilera legible por humanos de la solución
        con el fin de reportar resultados al usuario final.

        La hilera cumple con el siguiente formato:
        Nombre ciudad inicio -> Nombre ciudad 1 -> ... -> Nombre ciudad n -> Nombre ciudad inicio

        Entradas:
        sol (List[int])
            Solución a representar como texto legible

        Salidas:
        (str) Hilera en el formato mencionado anteriormente.
        """

        inicio = self.__números_ciudades[self.__ciudad_inicio]
        return ' -> '.join([inicio] + [self.__números_ciudades[c] for c in sol] + [inicio])

    def generar(self) -> List[int]:
        """Construye aleatoriamente una lista que representa una posible solución al problema.

        Entradas:
        ninguna

        Salidas:
        (List[int]) Una lista que representa una solución válida para esta instancia del vendedor viajero
        """

        sol = [c for c in range(self.__n) if c != self.__ciudad_inicio]
        random.shuffle(sol)
        return sol

    def generar_n(self, n: int) -> List[List[int]]:
        """Construye aleatoriamente una lista de estructuras de datos que representa n 
        posibles soluciones al problema.

        Entradas:
        n (int)
            Número de soluciones aleatorias a generar.

        Salidas:
        (List[int]) Lista que contiene n estructuras de datos, cada una representando
        una posible solución al problema modelado por el objeto de dominio.
        """

        soluciones = []

        for _ in range(n):
            soluciones.append(self.generar())

        return soluciones
        
    def fcosto(self, sol: List[int]) -> float:
        """Calcula el costo asociado con una solución dada."""
        costo = 0.0
        prev_city = self.__ciudad_inicio

        for city in sol:
            costo += self.__matriz_ady[prev_city][city]
            prev_city = city

        costo += self.__matriz_ady[prev_city][self.__ciudad_inicio]

        return costo

    def cruzar(self, sol_a: List[int], sol_b: List[int]) -> List[int]:
        """Produce una nueva posible solución cruzando las dos soluciones dadas por parámetro."""
        n = len(sol_a)
        punto_cruce = random.randint(0, n - 1)
        hijo = sol_a[:punto_cruce]

        for city in sol_b:
            if city not in hijo:
                hijo.append(city)

        return hijo

    def mutar(self, sol: List[int]) -> List[int]:
        """Produce una nueva solución aplicando un ligero cambio a la solución dada por parámetro."""

        i = random.randint(0, len(sol) - 1)
        j = random.randint(0, len(sol) - 1)

        while i == j:
            j = random.randint(0, len(sol) - 1)

        sol_mutada = sol.copy()
        sol_mutada[i], sol_mutada[j] = sol_mutada[j], sol_mutada[i]

        return sol_mutada


