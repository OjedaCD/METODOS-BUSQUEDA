import tkinter as tk
import heapq
import GRAFOS as g

class Dijkstra:
    def __init__(self, inicio, destino):
        self.inicio = inicio
        self.destino = destino
        
    def dijkstra(self, grafo, inicio, destino):
        distances = {vertex: float('infinity') for vertex in grafo}
        distances[inicio] = 0

        pq = [(0, inicio)]
        path = {}

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in grafo[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    path[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

        return path, distances[destino]

    def mostrar_camino(self):
        
        inicio = self.inicio
        destino = self.destino

        if inicio not in g.grafoP or destino not in g.grafoP:
            str("Nodo inválido")
            return

        path, distance = self.dijkstra(g.grafoP, inicio, destino)

        if distance == float('infinity'):
            str("No se encontró un camino")
            return
        path_nodes = [destino]
        node = destino
        while node != inicio:
            node = path[node]
            path_nodes.append(node)
        path_nodes.reverse()
        
        ruta_str = ' -> '.join(path_nodes)
        coste = str(round(distance,2))
        return ruta_str, coste
        

    