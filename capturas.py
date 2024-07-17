class Capturas:
    def __init__(self, tablero):
        self.tablero = tablero

    def realizar(self, current_row, current_col, new_row, new_col, color):
        enemy_row = (current_row + new_row) // 2
        enemy_col = (current_col + new_col) // 2

        for ficha in self.tablero.fichas:
            if ficha.row == enemy_row and ficha.col == enemy_col and ficha.color != color:
                self.tablero.tablero.delete(ficha.canvas_id)
                self.tablero.fichas.remove(ficha)
                break
