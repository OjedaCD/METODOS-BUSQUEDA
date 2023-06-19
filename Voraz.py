import heapq
import GRAFOS as g

class Voraz:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino

    def voraz(self, grafo, inicio, destino):
        heap = [(0, inicio, [])]
        visitados = set()

        while heap:
            (coste, nodo, ruta) = heapq.heappop(heap)

            if nodo not in visitados:
                ruta = ruta + [nodo]
                visitados.add(nodo)

                if nodo == destino:
                    return ruta, coste

                for siguiente, peso in grafo[nodo].items():
                    if siguiente not in visitados:
                        heapq.heappush(heap, (coste + peso, siguiente, ruta))

        return None, None

    def mostrar_camino(self):
    
        inicio = self.inicio
        destino = self.destino
        ruta, coste = self.voraz(g.grafoP, inicio, destino)

        if ruta:
            ruta_str = ' -> '.join(ruta)
            return ruta_str, coste
            
        else:
            return str("No se encontró un camino")

