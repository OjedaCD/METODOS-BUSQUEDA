import tkinter as tk
from PIL import ImageTk, Image
import BFS as bfs
import DFS as dfs
import Voraz as v
import Dijktra as d
import AEstrella as ae
import BranchBound as bb
import GRAFOS as g


class GUI:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Mapa ITCG")
        ventana.geometry("1350x650")
        


# Crear el label en la parte superior
        self.label_superior = tk.Label(ventana, text="INGRESE EL EDIFICIO CON LA POSICIÓN ACTUAL  Y EL DESTINO, DESPUÉS ELIGA EL ALGORITMO PARA DETERMINAR LA RUTA", font=("Arial", 16))
        self.label_superior.pack(pady=10)
        self.label_superior.configure(font=("Arial", 14, "bold"))

        # Crear el grupo de botones
        marco_botones = tk.Frame(ventana)
        marco_botones.pack()

        self.boton1 = tk.Button(marco_botones, text="Búsqueda por Anchura", width=25, height=3,command=self.mostrar_resultado_bfs)
        self.boton2 = tk.Button(marco_botones, text="Búsqueda por Profundidad", width=25, height=3,command=self.mostrar_resultado_dfs)
        self.boton3 = tk.Button(marco_botones, text="Avarisiosa", width=25, height=3, command=self.mostrar_resultado_Avarisiosa)
        self.boton4 = tk.Button(marco_botones, text="Dijktra", width=25, height=3,command=self.mostrar_resultado_Dijktra)
        self.boton5 = tk.Button(marco_botones, text="A*", width=25, height=3, command=self.mostrar_resultado_AEstrella)
        self.boton6 = tk.Button(marco_botones, text=" Branch & Bound", width=25, height=3, command=self.mostrar_resultado_BrachBound)

        self. boton1.pack(side="left", padx=(30,10))
        self.boton2.pack(side="left", padx=10)
        self.boton3.pack(side="left", padx=10)
        self.boton4.pack(side="left", padx=10)
        self.boton5.pack(side="left", padx=10)
        self.boton6.pack(side="left", padx=(10,30))

        # Colocar la imagen debajo de los botones

        self.imagen = ImageTk.PhotoImage(Image.open(r'C:\Users\ojeda\Desktop\Escuela\TEC\Semestre 10\Inteligencia Artificial\Individual\Unidad 1\1.11 Mapa ITCG\Métodos de búsqueda\ITCG2.jpg').resize((1300, 418)))

        self.label_imagen = tk.Label(ventana, image=self.imagen)
        self.label_imagen.pack(pady=10)

        # Crear los inputs para los valores y el botón para mostrar el resultado
        marco_valores = tk.Frame(ventana)
        marco_valores.pack()

        self.label_inicio = tk.Label(marco_valores, text="Posicion actual:")
        self.label_inicio.pack(side="left", padx=10)
        self.label_inicio.configure(font=("Arial", 14, "bold"), )

        self.input_inicio = tk.Entry(marco_valores)
        self.input_inicio.pack(side="left", padx=10)
    
        self.label_destino = tk.Label(marco_valores, text="Destino:")
        self.label_destino.pack(side="left", padx=10)
        self.label_destino.configure(font=("Arial", 14, "bold"))

        self.input_destino = tk.Entry(marco_valores)
        self.input_destino.pack(side="left", padx=10)

        self.label_resultado = tk.Label(ventana, text="", font=("Arial", 14, "bold"))
        self.label_resultado.pack()
        
    def mostrar_resultado_bfs(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = bfs.BFS(inicio, destino)
        resultado = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado BFS es: {resultado}")
        
    def mostrar_resultado_dfs(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = dfs.DFS(inicio, destino)
        resultado = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado DFS es: {resultado}")
        
    def mostrar_resultado_Avarisiosa(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = v.Voraz(inicio, destino)
        resultado, coste = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado Voraz es: {resultado} \n El coste es: {round(coste,2)*16} metros exactos")
        
    def mostrar_resultado_Dijktra(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = d.Dijkstra(inicio, destino)
        resultado, coste = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado Dijkstra es: {resultado} \n El coste es: {coste} metros exactos")
    
    def mostrar_resultado_AEstrella(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = ae.AEstrella(inicio, destino)
        resultado, coste = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado A* es: {resultado} \n El coste es: {round(coste,2)*16} metros exactos")
      
    def mostrar_resultado_BrachBound(self):
        inicio = self.input_inicio.get().upper()
        destino = self.input_destino.get().upper()
        camino = bb.BranchBound(inicio, destino)
        resultado, coste = camino.mostrar_camino()
        self.label_resultado.configure(text=f"El resultado Branch&Bound es: {resultado} \n El coste es: {round(coste,2)*16} metros exactos")
    

ventana = tk.Tk()
app = GUI(ventana)
ventana.mainloop()