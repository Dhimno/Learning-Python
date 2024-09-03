import tkinter as tk

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
PLAYER_SIZE = 30
OBSTACLE_SIZE = 40
FINISH_SIZE = 50

class PlatformGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Platform Game")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="lightblue")
        self.canvas.pack()

        # Create ground
        self.ground = self.canvas.create_rectangle(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, WINDOW_HEIGHT, fill="green")

        # Create player
        self.player = self.canvas.create_rectangle(50, WINDOW_HEIGHT - 50 - PLAYER_SIZE, 
                                                   50 + PLAYER_SIZE, WINDOW_HEIGHT - 50, 
                                                   fill="blue")

        # Create obstacles
        self.obstacles = [
            self.canvas.create_rectangle(200, WINDOW_HEIGHT - 50 - OBSTACLE_SIZE, 
                                         200 + OBSTACLE_SIZE, WINDOW_HEIGHT - 50, fill="red"),
            self.canvas.create_rectangle(400, WINDOW_HEIGHT - 50 - OBSTACLE_SIZE, 
                                         400 + OBSTACLE_SIZE, WINDOW_HEIGHT - 50, fill="red"),
            self.canvas.create_rectangle(600, WINDOW_HEIGHT - 50 - OBSTACLE_SIZE, 
                                         600 + OBSTACLE_SIZE, WINDOW_HEIGHT - 50, fill="red"),
        ]

        # Create finish line
        self.finish = self.canvas.create_rectangle(WINDOW_WIDTH - FINISH_SIZE, WINDOW_HEIGHT - 50 - FINISH_SIZE, 
                                                   WINDOW_WIDTH, WINDOW_HEIGHT - 50, fill="yellow")

        # Bind keys
        self.root.bind("<KeyPress>", self.key_press)
        self.root.bind("<KeyRelease>", self.key_release)

        # Player movement
        self.dx = 0
        self.dy = 0
        self.gravity = 2
        self.jump_power = -20
        self.on_ground = False

        # Start the game loop
        self.update()

    def key_press(self, event):
        if event.keysym == 'Left':
            self.dx = -10
        elif event.keysym == 'Right':
            self.dx = 10
        elif event.keysym == 'space' and self.on_ground:
            self.dy = self.jump_power

    def key_release(self, event):
        if event.keysym in ['Left', 'Right']:
            self.dx = 0

    def check_collisions(self, x1, y1, x2, y2):
        # Check collision with obstacles
        for obstacle in self.obstacles:
            ox1, oy1, ox2, oy2 = self.canvas.coords(obstacle)
            if x1 < ox2 and x2 > ox1 and y1 < oy2 and y2 > oy1:
                return True

        # Check collision with ground
        if y2 >= WINDOW_HEIGHT - 50:
            self.on_ground = True
            return True

        self.on_ground = False
        return False

    def update(self):
        # Apply gravity
        if not self.on_ground:
            self.dy += self.gravity

        # Move player
        self.canvas.move(self.player, self.dx, self.dy)

        # Check for collisions
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        if self.check_collisions(x1, y1, x2, y2):
            # Undo movement if collision detected
            self.canvas.move(self.player, -self.dx, -self.dy)
            if not self.on_ground:
                self.dy = 0  # Stop falling when hitting ground or obstacle

        # Check for finish line
        fx1, fy1, fx2, fy2 = self.canvas.coords(self.finish)
        if x1 >= fx1 and y2 >= fy1:
            self.canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, text="You Win!", font=('Arial', 30), fill="black")
            return

        # Continue game loop
        self.root.after(30, self.update)

# Run the game
root = tk.Tk()
game = PlatformGame(root)
root.mainloop()
