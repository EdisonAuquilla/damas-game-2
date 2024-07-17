import tkinter as tk
from .ficha import Ficha
from .movimientos import Movimientos
from .capturas import Capturas

class Tablero(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("600x600")
        self.title("Damas Game")
        self.tablero = tk.Canvas(self, width=600, height=600)
        self.tablero.pack(fill="both", expand=1)
        self.dibujar_cuadricula()
        self.agregar_fichas()
        self.ficha_seleccionada = None
        self.turno = "negro"
        self.tablero.bind("<Button-1>", self.on_click)

    def dibujar_cuadricula(self):
        for i in range(6):
            for j in range(6):
                color = "#FFE4C4" if (i + j) % 2 == 0 else "#8c564b"
                self.tablero.create_rectangle(j * 100, i * 100, (j + 1) * 100, (i + 1) * 100, fill=color)

    def agregar_fichas(self):
        self.fichas = []
        for i in range(2):
            for j in range(6):
                if (i + j) % 2 != 0:
                    color = "negro"
                    ficha = Ficha(self.tablero, color, i, j)
                    self.fichas.append(ficha)

        for i in range(4, 6):
            for j in range(6):
                if (i + j) % 2 != 0:
                    color = "blanco"
                    ficha = Ficha(self.tablero, color, i, j)
                    self.fichas.append(ficha)

    def on_click(self, event):
        x, y = event.x, event.y
        item = self.tablero.find_closest(x, y)
        if item:
            if self.ficha_seleccionada:
                self.ficha_seleccionada.deseleccionar()
                self.mover_ficha(event)
            self.ficha_seleccionada = next((ficha for ficha in self.fichas if ficha.canvas_id == item[0]), None)
            if self.ficha_seleccionada and self.ficha_seleccionada.color == self.turno:
                self.ficha_seleccionada.seleccionar()

    def mover_ficha(self, event):
        movimientos = Movimientos(self)
        movimientos.mover(event)

    def cambiar_turno(self):
        self.turno = "blanco" if self.turno == "negro" else "negro"

    def validar_movimiento(self, current_row, current_col, new_row, new_col, color):
        movimientos = Movimientos(self)
        return movimientos.validar(current_row, current_col, new_row, new_col, color)

    def realizar_captura(self, current_row, current_col, new_row, new_col, color):
        capturas = Capturas(self)
        capturas.realizar(current_row, current_col, new_row, new_col, color)

if __name__ == "__main__":
    app = Tablero()
    app.mainloop()
