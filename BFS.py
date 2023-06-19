from collections import deque
import GRAFOS as g

class BFS:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        

    def bfs(self, inicio, destino):
        # Creamos un diccionario para almacenar los padres de cada nodo
        padres = {inicio: None}
        # Creamos una cola para almacenar los nodos por visitar
        cola = deque([inicio])
        # Mientras la cola no esté vacía, seguimos explorando
        while cola:
            actual = cola.popleft()
            # Si encontramos el destino, reconstruimos el camino y lo devolvemos
            if actual == destino:
                camino = [destino]
                padre = padres[destino]
                while padre is not None:
                    camino.append(padre)
                    padre = padres[padre]
                camino.reverse()
                return camino
            # Si no hemos encontrado el destino, seguimos explorando
            for adyacente in g.grafo[actual]:
                if adyacente not in padres:
                    padres[adyacente] = actual
                    cola.append(adyacente)
        # Si llegamos aquí es porque no se encontró el destino
        return None

    def mostrar_camino(self):
        # Obtenemos el nodo de inicio y destino de los campos de entrada
        inicio = self.inicio
        destino = self.destino
        # Buscamos el camino desde el nodo de inicio hasta el nodo destino
        camino = self.bfs(inicio, destino)
        # Mostramos el camino en la etiqueta correspondiente
        if camino is not None:
            return str(" -> ".join(camino))
        else:
            return str("No se encontró un camino")