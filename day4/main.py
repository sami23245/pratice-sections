
import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 400
BALL_RADIUS = 15
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SPEED_X = 3
BALL_SPEED_Y = -3

class BallGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Ball Bounce Game")
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        # Create paddle
        self.paddle = self.canvas.create_rectangle(WIDTH//2 - PADDLE_WIDTH//2, HEIGHT - 30,
                                                   WIDTH//2 + PADDLE_WIDTH//2, HEIGHT - 20, fill="blue")
        
        # Create ball
        self.ball = self.canvas.create_oval(WIDTH//2 - BALL_RADIUS, HEIGHT//2 - BALL_RADIUS,
                                            WIDTH//2 + BALL_RADIUS, HEIGHT//2 + BALL_RADIUS, fill="red")
        
        # Ball movement
        self.ball_dx = BALL_SPEED_X
        self.ball_dy = BALL_SPEED_Y
        
        # Score
        self.score = 0
        self.score_text = self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 14))
        
        # Bind paddle movement
        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        
        # Start game loop
        self.update_game()
        
    def move_left(self, event):
        self.canvas.move(self.paddle, -20, 0)
        if self.canvas.coords(self.paddle)[0] < 0:
            self.canvas.move(self.paddle, -self.canvas.coords(self.paddle)[0], 0)
    
    def move_right(self, event):
        self.canvas.move(self.paddle, 20, 0)
        if self.canvas.coords(self.paddle)[2] > WIDTH:
            self.canvas.move(self.paddle, WIDTH - self.canvas.coords(self.paddle)[2], 0)
    
    def update_game(self):
        # Move the ball
        self.canvas.move(self.ball, self.ball_dx, self.ball_dy)
        ball_coords = self.canvas.coords(self.ball)
        
        # Bounce on walls
        if ball_coords[0] <= 0 or ball_coords[2] >= WIDTH:
            self.ball_dx *= -1
        if ball_coords[1] <= 0:
            self.ball_dy *= -1
        
        # Bounce on paddle
        paddle_coords = self.canvas.coords(self.paddle)
        if (ball_coords[2] >= paddle_coords[0] and ball_coords[0] <= paddle_coords[2]) and \
           (ball_coords[3] >= paddle_coords[1] and ball_coords[3] <= paddle_coords[3]):
            self.ball_dy *= -1
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
        
        # Game over
        if ball_coords[3] >= HEIGHT:
            self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))
            return
        
        # Continue the game loop
        self.root.after(20, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = BallGame(root)
    root.mainloop()
