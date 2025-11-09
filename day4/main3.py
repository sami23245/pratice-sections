import tkinter as tk
import random
import winsound

# Game settings
WIDTH = 700
HEIGHT = 500
BALL_RADIUS = 15
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
OBSTACLE_WIDTH = 80
OBSTACLE_HEIGHT = 15
POWERUP_SIZE = 20

class CrazyBounceGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Crazy Bouncing Balls")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        # Score
        self.score = 1
        self.score_text = self.canvas.create_text(70, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))
        
        # Paddle
        self.paddle = self.canvas.create_rectangle(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 20,
                                                   WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 10, fill="blue")
        
        # Balls
        self.balls = []
        for _ in range(3):  # Start with 3 balls
            self.create_ball()
        
        # Moving obstacles
        self.obstacles = []
        for _ in range(4):
            self.create_obstacle()
        
        # Power-ups
        self.powerups = []
        
        # Paddle movement
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        # Start game loop
        self.update_game()
        self.spawn_powerup()
    
    def create_ball(self):
        x = random.randint(100, WIDTH-100)
        y = random.randint(50, HEIGHT//2)
        dx = random.choice([-4, 4])
        dy = random.choice([-4, 4])
        ball = {"id": self.canvas.create_oval(x-BALL_RADIUS, y-BALL_RADIUS, x+BALL_RADIUS, y+BALL_RADIUS, fill="red"),
                "dx": dx, "dy": dy}
        self.balls.append(ball)
    
    def create_obstacle(self):
        x = random.randint(50, WIDTH-50)
        y = random.randint(50, HEIGHT-250)
        dx = random.choice([-2,2])  # moving obstacle
        obstacle = {"id": self.canvas.create_rectangle(x, y, x+OBSTACLE_WIDTH, y+OBSTACLE_HEIGHT, fill="green"),
                    "dx": dx}
        self.obstacles.append(obstacle)
    
    def spawn_powerup(self):
        x = random.randint(50, WIDTH-50)
        y = random.randint(50, HEIGHT-250)
        powerup = self.canvas.create_oval(x, y, x+POWERUP_SIZE, y+POWERUP_SIZE, fill="yellow")
        self.powerups.append(powerup)
        # Respawn another power-up after 5 seconds
        self.root.after(5000, self.spawn_powerup)
    
    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
        if self.canvas.coords(self.paddle)[0] < 0:
            self.canvas.move(self.paddle, -self.canvas.coords(self.paddle)[0], 0)
    
    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
        if self.canvas.coords(self.paddle)[2] > WIDTH:
            self.canvas.move(self.paddle, WIDTH - self.canvas.coords(self.paddle)[2], 0)
    
    def update_game(self):
        paddle_coords = self.canvas.coords(self.paddle)
        
        # Move obstacles
        for obs in self.obstacles:
            self.canvas.move(obs["id"], obs["dx"], 0)
            ox1, oy1, ox2, oy2 = self.canvas.coords(obs["id"])
            if ox1 <= 0 or ox2 >= WIDTH:
                obs["dx"] *= -1
        
        # Move balls
        for ball in self.balls:
            self.canvas.move(ball["id"], ball["dx"], ball["dy"])
            x1, y1, x2, y2 = self.canvas.coords(ball["id"])
            
            # Wall collisions
            if x1 <= 0 or x2 >= WIDTH:
                ball["dx"] *= -1
                self.multiply_score()
                winsound.Beep(800, 50)
            if y1 <= 0:
                ball["dy"] *= -1
                self.multiply_score()
                winsound.Beep(1000, 50)
            
            # Paddle collision
            if (x2 >= paddle_coords[0] and x1 <= paddle_coords[2]) and (y2 >= paddle_coords[1] and y1 <= paddle_coords[3]):
                ball["dy"] *= -1
                self.multiply_score()
                winsound.Beep(1200, 50)
            
            # Obstacle collision
            for obs in self.obstacles:
                ox1, oy1, ox2, oy2 = self.canvas.coords(obs["id"])
                if (x2 >= ox1 and x1 <= ox2) and (y2 >= oy1 and y1 <= oy2):
                    ball["dy"] *= -1
                    self.multiply_score()
                    winsound.Beep(1500, 50)
            
            # Power-up collision
            for powerup in self.powerups:
                px1, py1, px2, py2 = self.canvas.coords(powerup)
                if (x2 >= px1 and x1 <= px2) and (y2 >= py1 and y1 <= py2):
                    self.multiply_score()
                    winsound.Beep(1800, 80)
                    self.canvas.delete(powerup)
                    self.powerups.remove(powerup)
                    # Add a new ball as reward
                    self.create_ball()
            
            # Game over
            if y2 >= HEIGHT:
                self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))
                return
        
        # Continue game loop
        self.root.after(20, self.update_game)
    
    def multiply_score(self):
        self.score *= 2
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = CrazyBounceGame(root)
    root.mainloop()
