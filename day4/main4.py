import tkinter as tk
import random

# Game settings
WIDTH = 500
HEIGHT = 400
SEG_SIZE = 20  # Size of each snake segment
UPDATE_DELAY = 100  # Time in ms between game updates

class SnakeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake Game")
        
        # Canvas setup
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()
        
        # Initialize snake
        self.snake = [(WIDTH//2, HEIGHT//2)]
        self.direction = "Right"
        self.running = True
        
        # Draw initial snake
        self.segments = [self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="green") for x, y in self.snake]
        
        # Food
        self.food = None
        self.place_food()
        
        # Score
        self.score = 0
        self.score_text = self.canvas.create_text(50, 10, text=f"Score: {self.score}", fill="white", font=("Arial", 14))
        
        # Bind keys
        self.root.bind("<Up>", self.go_up)
        self.root.bind("<Down>", self.go_down)
        self.root.bind("<Left>", self.go_left)
        self.root.bind("<Right>", self.go_right)
        
        # Start game loop
        self.update_game()
    
    def place_food(self):
        x = random.randint(0, (WIDTH-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
        y = random.randint(0, (HEIGHT-SEG_SIZE)//SEG_SIZE) * SEG_SIZE
        if self.food:
            self.canvas.delete(self.food)
        self.food = self.canvas.create_rectangle(x, y, x+SEG_SIZE, y+SEG_SIZE, fill="red")
        self.food_position = (x, y)
    
    def go_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"
    
    def go_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"
    
    def go_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"
    
    def go_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"
    
    def update_game(self):
        if not self.running:
            return
        
        # Move snake
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            head_y -= SEG_SIZE
        elif self.direction == "Down":
            head_y += SEG_SIZE
        elif self.direction == "Left":
            head_x -= SEG_SIZE
        elif self.direction == "Right":
            head_x += SEG_SIZE
        
        # Check collisions
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT or (head_x, head_y) in self.snake:
            self.game_over()
            return
        
        # Add new head
        self.snake.insert(0, (head_x, head_y))
        self.segments.insert(0, self.canvas.create_rectangle(head_x, head_y, head_x+SEG_SIZE, head_y+SEG_SIZE, fill="green"))
        
        # Check if food eaten
        if (head_x, head_y) == self.food_position:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            self.place_food()
        else:
            # Remove tail
            tail = self.snake.pop()
            self.canvas.delete(self.segments.pop())
        
        # Repeat
        self.root.after(UPDATE_DELAY, self.update_game)
    
    def game_over(self):
        self.running = False
        self.canvas.create_text(WIDTH//2, HEIGHT//2, text="GAME OVER", fill="red", font=("Arial", 30))

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()
