import tkinter as tk
import random
import winsound  # For Windows sound

# Game settings
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 15
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 15

class BouncingBallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball Multiplier Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        # Score
        self.score = 1
        self.score_text = self.canvas.create_text(50, 20, text=f"Score: {self.score}", fill="white", font=("Arial", 16))
        
        # Paddle
        self.paddle = self.canvas.create_rectangle(WIDTH//2 - 50, HEIGHT - 20,
                                                   WIDTH//2 + 50, HEIGHT - 10, fill="blue")
        
        # Balls
        self.balls = []
        for _ in range(1):  # Start with 1 ball
            self.create_ball()
        
        # Obstacles
        self.obstacles = []
        for _ in range(3):
            self.create_obstacle()
        
        # Paddle movement
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        # Game loop
        self.update_game()
    
    def create_ball(self):
        x = random.randint(100, WIDTH-100)
        y = random.randint(50, HEIGHT//2)
        dx = random.choice([-3,3])
        dy = random.choice([-3,3])
        ball = {"id": self.canvas.create_oval(x-BALL_RADIUS, y-BALL_RADIUS, x+BALL_RADIUS, y+BALL_RADIUS, fill="red"),
                "dx": dx, "dy": dy}
        self.balls.append(ball)
    
    def create_obstacle(self):
        x = random.randint(50, WIDTH-50)
        y = random.randint(50, HEIGHT-150)
        obstacle = self.canvas.create_rectangle(x, y, x+OBSTACLE_WIDTH, y+OBSTACLE_HEIGHT, fill="green")
        self.obstacles.append(obstacle)
    
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
            if (x2 >= paddle_coords[0] and x1 <= paddle_coords[2]) and (y2 >= paddle_coords[1] and y2 <= paddle_coords[3]):
                ball["dy"] *= -1
                self.multiply_score()
                winsound.Beep(1200, 50)
            
            # Obstacle collision
            for obs in self.obstacles:
                ox1, oy1, ox2, oy2 = self.canvas.coords(obs)
                if (x2 >= ox1 and x1 <= ox2) and (y2 >= oy1 and y1 <= oy2):
                    ball["dy"] *= -1
                    self.multiply_score()
                    winsound.Beep(1500, 50)
            
            # Game over
            if y2 >= HEIGHT:
                self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))
                return
        
        self.root.after(20, self.update_game)
    
    def multiply_score(self):
        self.score *= 2
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

if __name__ == "__main__":
    root = tk.Tk()
    game = BouncingBallGame(root)
    root.mainloop()
