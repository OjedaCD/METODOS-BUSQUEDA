import queue
import GRAFOS as g
class BranchBound:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        
    def branchbound(self, grafo, inicio, destino):
        cola = queue.PriorityQueue()
        visitados = set()
        cola.put((0, [inicio]))
        while not cola.empty():
            (costo, camino) = cola.get()
            nodo_actual = camino[-1]
            if nodo_actual == destino:
                return (costo, camino)
            if nodo_actual not in visitados:
                visitados.add(nodo_actual)
                for nodo_vecino, costo_arista in grafo[nodo_actual].items():
                    if nodo_vecino not in visitados:
                        costo_total = costo + costo_arista
                        camino_total = camino + [nodo_vecino]
                        cola.put((costo_total, camino_total))


    # Función para manejar el botón presionado
    def mostrar_camino(self):
        inicio = self.inicio
        destino = self.destino
        
        resultado = self.branchbound(g.grafoP, inicio, destino)
        if resultado:
            coste, camino = resultado
            ruta_str = " -> ".join(camino)
            return ruta_str, coste
        else:
            return str("No se encontró un camino")

