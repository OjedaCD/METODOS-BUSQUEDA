import heapq
import GRAFOS as g

class AEstrella:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        
    # Función heurística
    def heuristica(self, inicio, destino):
        return 0  # Haremos que la heurística sea cero para que A* sea idéntico a Dijkstra

    # Algoritmo A*
    def aestrella(self, inicio, destino, grafo):
        heap = [(0, inicio, [])]
        visitados = set()
        while heap:
            (costo, nodo_actual, camino) = heapq.heappop(heap)
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                camino = camino + [nodo_actual]
                if nodo_actual == destino:
                    return (camino, costo)
                for vecino, costo_arista in grafo[nodo_actual].items():
                    if vecino not in visitados:
                        costo_total = costo + costo_arista + self.heuristica(vecino, destino)
                        heapq.heappush(heap, (costo_total, vecino, camino))
        return None

    # Función para manejar la entrada del botón
    def mostrar_camino(self):
        inicio = self.inicio
        destino = self.destino
        
        if inicio in g.grafoP and destino in g.grafoP:
            resultado = self.aestrella(inicio, destino, g.grafoP)
            if resultado:
                camino, coste = resultado
                ruta_str = ' -> '.join(camino)
                return ruta_str, coste
            else:
                return str("No se encontró un camino")
        else:
            return str("Nodos no encontrados en el grafo")
        

