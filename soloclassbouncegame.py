from tkinter import *
import random
import time

class Game:
    def __init__(self):
        self.tk = Tk()  
        self.tk.title("Bounce Game") 
        self.tk.resizable(0, 0)  
        self.tk.wm_attributes("-topmost", 1)
        self.canvas = Canvas(
            self.tk, 
            width=500, 
            height=400, 
            bd=0, 
            highlightthickness=0,
            bg="black")
        self.canvas.pack() 
        self.tk.update()

    def mainloop(self):
        while True:
            if start_game.started and not ball.hit_bottom:
                ball.draw() 
                paddle.draw()
            if ball.hit_bottom == True:
                time.sleep(0.5)
                self.canvas.itemconfig(game_over_text, state="normal")
                time.sleep(0.5)
                self.canvas.itemconfig(retry_text, state="normal")
            self.tk.update_idletasks() 
            self.tk.update() 
            time.sleep(0.01)    


class Ball:
    def __init__(self, game, paddle, score, color):
        self.canvas = game.canvas
        self.paddle = paddle
        self.score = score
        self.ball = game.canvas.create_oval(
            10, 10, 25, 25, fill=color
            )
        self.canvas.move(self.ball, 245, 100)
        #Objective 1
        starts = [-3, -2, -1, 1, 2, 3] 
        random.shuffle(starts) 
        self.x = starts[0]
        self.y = -4
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        #Objective 5
        self.hit_bottom = False

    def hit_paddle(self, ball_pos):
        #Objective 4
        paddle_pos = self.canvas.coords(self.paddle.paddle)
        if ball_pos[2] >= paddle_pos[0] \
            and ball_pos[0] <= paddle_pos[2] \
            and ball_pos[3] >= paddle_pos[1] \
            and ball_pos[3] <= paddle_pos[3]:
                self.x += self.paddle.x
                self.score.hit()
                return True
        return False
                
    def draw(self):
        self.canvas.move(self.ball, self.x, self.y)
        ball_pos = self.canvas.coords(self.ball)
        if ball_pos[0] <= 0: 
            self.x = 3 
        if ball_pos[1] <= 0: 
            self.y = 3  
        if ball_pos[3] >= self.canvas_height: 
            self.hit_bottom = True
        if ball_pos[2] >= self.canvas_width: 
            self.x = -3
        #Objective 4
        if self.hit_paddle(ball_pos):
            self.y = -3

class Paddle: 
    def __init__(self, game, color):
        self.canvas = game.canvas
        self.paddle = game.canvas.create_rectangle(
            0, 0, 100, 10, fill=color) 
        self.canvas.move(self.paddle, 200, 300) 
        self.x = 0
        self.y = 0
        self.canvas.bind_all("<KeyPress-Left>", self.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
        self.canvas.bind_all("<KeyPress-Up>", self.turn_up)
        self.canvas.bind_all("<KeyPress-Down>", self.turn_down)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()

    def turn_left(self, evt): 
        self.x = -2
        
    def turn_right(self, evt): 
        self.x = 2 

    def turn_up(self, evt): 
        self.y = -2
        
    def turn_down(self, evt): 
        self.y = 2
        
    def draw(self):
        self.canvas.move(self.paddle, self.x, self.y)
        paddle_pos = self.canvas.coords(self.paddle) 
        if paddle_pos[0] <= 0: 
            self.x = 2 
        if paddle_pos[2] >= self.canvas_width: 
            self.x = -2
        if paddle_pos[1] <= 0: 
            self.y = 2  
        if paddle_pos[3] >= self.canvas_height: 
            self.y = -2

class Starting:
    def __init__(self, game):
        self.canvas = game.canvas
        self.canvas.bind_all("<space>", self.start_game)
        self.started = False
    
    def start_game(self, evt):
            self.started = True
            
class Score:
    def __init__(self, game, color):
        self.canvas = game.canvas
        self.record = 0
        self.scoreid = self.canvas.create_text(
            470, 20, text=self.record, fill=color, font=("Georgia",20)
            )

    def hit(self):
        self.record += 1
        self.canvas.itemconfig(self.scoreid, text=self.record)

class Reset:
    def __init__(self, game, ball, paddle, score):
        pass
    
g = Game()
start_game = Starting(g)
score = Score(g, 'white')
paddle = Paddle(g, 'white')
ball = Ball(g, paddle, score, 'white')
game_over_text = g.canvas.create_text(
    250, 200, text="Game Over", fill="white", 
    font=("Georgia",18,"bold"),state = "hidden")
retry_text = g.canvas.create_text(
    250, 230, text="Try Again? Press Space", fill="white", 
    font=("Georgia",18,"bold"),state = "hidden")    
g.mainloop()