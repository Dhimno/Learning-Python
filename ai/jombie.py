import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 30
ZOMBIE_SIZE = 30
BULLET_SIZE = 5
ZOMBIE_SPEED = 2
BULLET_SPEED = 10
SPAWN_INTERVAL = 2000  # Milliseconds

class ZombieShooterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Zombie Shooter")
        self.canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black")
        self.canvas.pack()

        # Create player
        self.player = self.canvas.create_rectangle(WINDOW_WIDTH//2 - PLAYER_SIZE//2,
                                                   WINDOW_HEIGHT//2 - PLAYER_SIZE//2,
                                                   WINDOW_WIDTH//2 + PLAYER_SIZE//2,
                                                   WINDOW_HEIGHT//2 + PLAYER_SIZE//2,
                                                   fill="blue")

        # Set up lists for zombies and bullets
        self.zombies = []
        self.bullets = []

        # Bind keys
        self.root.bind("<KeyPress>", self.key_press)
        self.root.bind("<KeyRelease>", self.key_release)
        self.root.bind("<Button-1>", self.shoot)

        # Player movement
        self.dx = 0
        self.dy = 0

        # Game loop
        self.spawn_zombie()
        self.update()

    def key_press(self, event):
        if event.keysym == 'Left':
            self.dx = -5
        elif event.keysym == 'Right':
            self.dx = 5
        elif event.keysym == 'Up':
            self.dy = -5
        elif event.keysym == 'Down':
            self.dy = 5

    def key_release(self, event):
        if event.keysym in ['Left', 'Right']:
            self.dx = 0
        elif event.keysym in ['Up', 'Down']:
            self.dy = 0

    def shoot(self, event):
        x1, y1, x2, y2 = self.canvas.coords(self.player)
        bullet = self.canvas.create_oval((x1 + x2) // 2 - BULLET_SIZE,
                                         y1 - BULLET_SIZE,
                                         (x1 + x2) // 2 + BULLET_SIZE,
                                         y1 + BULLET_SIZE,
                                         fill="yellow")
        self.bullets.append((bullet, 0, -BULLET_SPEED))  # Shoot upwards

    def spawn_zombie(self):
        x = random.randint(0, WINDOW_WIDTH - ZOMBIE_SIZE)
        y = -ZOMBIE_SIZE
        zombie = self.canvas.create_rectangle(x, y, x + ZOMBIE_SIZE, y + ZOMBIE_SIZE, fill="green")
        self.zombies.append((zombie, ZOMBIE_SPEED))
        self.root.after(SPAWN_INTERVAL, self.spawn_zombie)

    def update(self):
        # Move player
        self.canvas.move(self.player, self.dx, self.dy)

        # Move bullets
        for bullet, dx, dy in self.bullets:
            self.canvas.move(bullet, dx, dy)

        # Move zombies
        for zombie, speed in self.zombies:
            self.canvas.move(zombie, 0, speed)

        # Check collisions
        self.check_collisions()

        # Remove off-screen bullets
        self.bullets = [bullet for bullet in self.bullets if self.canvas.coords(bullet[0])[1] > 0]

        # Check game over (if a zombie reaches the bottom)
        for zombie, _ in self.zombies:
            if self.canvas.coords(zombie)[3] >= WINDOW_HEIGHT:
                self.canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, text="Game Over", fill="red", font=('Arial', 30))
                return

        # Continue game loop
        self.root.after(30, self.update)

    def check_collisions(self):
        bullets_to_remove = []
        zombies_to_remove = []

        for bullet, _, _ in self.bullets:
            for zombie, _ in self.zombies:
                if self.is_collision(bullet, zombie):
                    bullets_to_remove.append(bullet)
                    zombies_to_remove.append(zombie)

        # Remove bullets and zombies that have collided
        for bullet in bullets_to_remove:
            self.canvas.delete(bullet)
            self.bullets.remove((bullet, 0, -BULLET_SPEED))

        for zombie in zombies_to_remove:
            self.canvas.delete(zombie)
            self.zombies.remove((zombie, ZOMBIE_SPEED))

    def is_collision(self, item1, item2):
        x1, y1, x2, y2 = self.canvas.coords(item1)
        x3, y3, x4, y4 = self.canvas.coords(item2)
        return not (x2 < x3 or x1 > x4 or y2 < y3 or y1 > y4)

# Run the game
root = tk.Tk()
game = ZombieShooterGame(root)
root.mainloop()
