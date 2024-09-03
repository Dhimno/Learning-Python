import tkinter as tk
import random

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 20
CELL_SIZE = 30
DELAY = 500  # milliseconds

# Tetromino shapes
TETROMINOS = {
    'I': [[1, 1, 1, 1]],
    'O': [[1, 1], [1, 1]],
    'T': [[0, 1, 0], [1, 1, 1]],
    'S': [[0, 1, 1], [1, 1, 0]],
    'Z': [[1, 1, 0], [0, 1, 1]],
    'J': [[1, 0, 0], [1, 1, 1]],
    'L': [[0, 0, 1], [1, 1, 1]],
}

# Colors
COLORS = {
    'I': 'cyan',
    'O': 'yellow',
    'T': 'purple',
    'S': 'green',
    'Z': 'red',
    'J': 'blue',
    'L': 'orange',
}

class TetrisGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris")
        self.canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
        self.canvas.pack()

        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.current_tetromino = self.create_new_tetromino()
        self.game_over = False

        self.root.bind("<Key>", self.key_pressed)
        self.update()

    def create_new_tetromino(self):
        shape = random.choice(list(TETROMINOS.keys()))
        tetromino = {
            'shape': TETROMINOS[shape],
            'color': COLORS[shape],
            'x': GRID_WIDTH // 2 - len(TETROMINOS[shape][0]) // 2,
            'y': 0,
        }
        return tetromino

    def draw_grid(self):
        self.canvas.delete("all")
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.grid[y][x]:
                    self.canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                                 (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                                 fill=self.grid[y][x])

    def draw_tetromino(self, tetromino):
        for y, row in enumerate(tetromino['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.canvas.create_rectangle((tetromino['x'] + x) * CELL_SIZE,
                                                 (tetromino['y'] + y) * CELL_SIZE,
                                                 (tetromino['x'] + x + 1) * CELL_SIZE,
                                                 (tetromino['y'] + y + 1) * CELL_SIZE,
                                                 fill=tetromino['color'])

    def move_tetromino(self, dx, dy):
        self.current_tetromino['x'] += dx
        self.current_tetromino['y'] += dy
        if self.check_collision():
            self.current_tetromino['x'] -= dx
            self.current_tetromino['y'] -= dy
            return False
        return True

    def rotate_tetromino(self):
        self.current_tetromino['shape'] = [list(row) for row in zip(*self.current_tetromino['shape'][::-1])]
        if self.check_collision():
            self.current_tetromino['shape'] = [list(row) for row in zip(*self.current_tetromino['shape'])][::-1]

    def check_collision(self):
        for y, row in enumerate(self.current_tetromino['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_tetromino['x'] + x
                    new_y = self.current_tetromino['y'] + y
                    if new_x < 0 or new_x >= GRID_WIDTH or new_y >= GRID_HEIGHT or self.grid[new_y][new_x]:
                        return True
        return False

    def place_tetromino(self):
        for y, row in enumerate(self.current_tetromino['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_tetromino['y'] + y][self.current_tetromino['x'] + x] = self.current_tetromino['color']
        self.clear_lines()
        self.current_tetromino = self.create_new_tetromino()
        if self.check_collision():
            self.game_over = True

    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = GRID_HEIGHT - len(new_grid)
        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(lines_cleared)] + new_grid

    def update(self):
        if not self.game_over:
            if not self.move_tetromino(0, 1):
                self.place_tetromino()
            self.draw_grid()
            self.draw_tetromino(self.current_tetromino)
            self.root.after(DELAY, self.update)
        else:
            self.canvas.create_text(GRID_WIDTH * CELL_SIZE // 2, GRID_HEIGHT * CELL_SIZE // 2,
                                    text="Game Over", fill="red", font=('Arial', 24))

    def key_pressed(self, event):
        if event.keysym == 'Left':
            self.move_tetromino(-1, 0)
        elif event.keysym == 'Right':
            self.move_tetromino(1, 0)
        elif event.keysym == 'Down':
            self.move_tetromino(0, 1)
        elif event.keysym == 'Up':
            self.rotate_tetromino()
        self.draw_grid()
        self.draw_tetromino(self.current_tetromino)

# Run the game
root = tk.Tk()
game = TetrisGame(root)
root.mainloop()
