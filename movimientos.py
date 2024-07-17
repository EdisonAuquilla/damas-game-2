class Movimientos:
    def __init__(self, tablero):
        self.tablero = tablero

    def mover(self, event):
        x, y = event.x, event.y
        row = y // 100
        col = x // 100

        if self.tablero.ficha_seleccionada:
            ficha = self.tablero.ficha_seleccionada
            color = ficha.color
            current_row, current_col = ficha.row, ficha.col

            if self.tablero.validar_movimiento(current_row, current_col, row, col, color):
                self.tablero.fichas.remove(ficha)
                ficha.row, ficha.col = row, col
                self.tablero.fichas.append(ficha)
                self.tablero.tablero.coords(ficha.canvas_id, col * 100 + 10, row * 100 + 10, (col + 1) * 100 - 10, (row + 1) * 100 - 10)
                self.tablero.realizar_captura(current_row, current_col, row, col, color)
                self.tablero.cambiar_turno()

    def validar(self, current_row, current_col, new_row, new_col, color):
        if 0 <= new_row < 6 and 0 <= new_col < 6:
            if color == "negro":
                if new_row == current_row + 1 and abs(new_col - current_col) == 1:
                    return self.tablero.casilla_libre(new_row, new_col)
                elif new_row == current_row + 2 and abs(new_col - current_col) == 2:
                    return self.tablero.casilla_libre(new_row, new_col) and self.tablero.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
            elif color == "blanco":
                if new_row == current_row - 1 and abs(new_col - current_col) == 1:
                    return self.tablero.casilla_libre(new_row, new_col)
                elif new_row == current_row - 2 and abs(new_col - current_col) == 2:
                    return self.tablero.casilla_libre(new_row, new_col) and self.tablero.casilla_ocupada_por_enemigo((current_row + new_row) // 2, (current_col + new_col) // 2, color)
        return False
