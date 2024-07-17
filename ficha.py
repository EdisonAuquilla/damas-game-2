class Ficha:
    def __init__(self, canvas, color, row, col):
        self.canvas = canvas
        self.color = color
        self.row = row
        self.col = col
        self.canvas_id = self.canvas.create_oval(col * 100 + 10, row * 100 + 10, (col + 1) * 100 - 10, (row + 1) * 100 - 10, fill=color)
        self.seleccionada = False

    def seleccionar(self):
        self.canvas.itemconfig(self.canvas_id, outline="blue")
        self.seleccionada = True

    def deseleccionar(self):
        self.canvas.itemconfig(self.canvas_id, outline="")
        self.seleccionada = False

