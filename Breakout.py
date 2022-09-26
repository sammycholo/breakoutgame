#GROUP MEMBERS#
# NAME : TAHA SHAHID | ROLL : 21-10558 #
# NAME : SAMUEL EMMANUEL | ROLL : 21-10756#

from tkinter import *

#-----------------------------------    

class Vector:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

#-----------------------------------    

class GameObject:
    
    def __init__(self, pos):
        self.position = Vector(pos[0], pos[1])
    
    def isCollidingWith(self, otherGameObject):  # Checks collosion between itself
        #############################            #   and another game object. Returns
        #   INSERT YOUR CODE HERE                #   True if they are colliding,
        pass                                     #   False otherwise.
        #############################
    
    def Draw(self):                    # This function MUST be overidden by all 
        raise                          #   sub-classes !!!
        

#-----------------------------------

class Background(GameObject):
    def __init__(self):
        #############################
        #   INSERT YOUR CODE HERE
        GameObject.__init__(self, [320, 240])
        self.img = PhotoImage(file = 'bg.gif')
        #############################
    
    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(self.position.x, self.position.y, image = self.img)
        #############################
        

#-----------------------------------
    
class Brick(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self,color,x,y):
        self.total_bricks = {}
        self.color = color
        self.x = x
        self.y = y
    def Draw(self):
        if self.color == "Green" :
            NormalBrick()
            NormalBrick.Draw()
        elif self.color == "Grey":
            MetalBrick()
            MetalBrick.Draw()
        elif self.color == "Red" :
            ExplodingBrick()
            ExplodingBrick.Draw()
        else :
            GlassBrick()
            GlassBrick.Draw()
	
	#self.width = None
	#self.height = None
    #############################


class NormalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        Brick. __init(self,color,x,y)
        self.img = PhotoImage(file = 'normalbrick.gif')
        self.density = 2
    #############################
    def Draw(self):
        Game.canvas.create_image(self.x, self.y, image = self.img)
        

    
class MetalBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        Brick. __init(self,color,x,y)
        self.img = PhotoImage(file = 'metalbrick.gif')
        self.density = 7
	#############################
    def Draw(self):
        Game.canvas.create_image(self.x, self.y, image = self.img)

    
class ExplodingBrick(Brick):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        Brick. __init(self,color,x,y)
        self.img = PhotoImage(file = 'explodingbrick.gif')
        self.density = 4
	#############################
    def Draw(self):
        Game.canvas.create_image(self.x, self.y, image = self.img)
	
class GlassBrick(Brick):
    def __init_(self):
        Brick. __init(self,color,x,y)
        self.img = PhotoImage(file = 'glassbrick.gif')
        self.density = 1
    def Draw(self):
        Game.canvas.create_image(self.x, self.y, image = self.img)

#-----------------------------------
    
class Ball(GameObject):
    def __init__(self):
        #############################
        #   INSERT YOUR CODE HERE
        GameObject.__init__(self, [300, 285])
        self.img = PhotoImage(file = 'ballBlue.png')
        #############################
    
    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(self.position.x, self.position.y, image = self.img)
        #############################

    
#-----------------------------------

class Powerup(GameObject):
    #############################
    #   INSERT YOUR CODE HERE
    #############################
    pass
    
class Life(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        self.image = PhotoImage(file = 'life.gif')
    #############################

    
class FastPaddle(Powerup):
    #############################
    #   INSERT YOUR CODE HERE
    def __init__(self):
        self.image = PhotoImage(file = 'fastpaddle.gif')
    #############################


class CrazyBall(Powerup):
    def __init__(self):
        self.image = PhotoImage(file = 'crazyball.gif')
    #############################
    #   INSERT YOUR CODE HERE
    
    #############################


#-----------------------------------

class Player(GameObject):
    def __init__(self, game, pos, vel):
        #############################
        #   INSERT YOUR CODE HERE
        GameObject.__init__(self, pos)
        self.velocity = vel
        self.img = PhotoImage(file = 'paddleBlu.gif')
        #############################


    def Draw(self):
        #############################
        #   INSERT YOUR CODE HERE
        Game.canvas.create_image(self.position.x, self.position.y, image = self.img)
        #############################

        
    
#-----------------------------------

class Game:
    canvas = None
    def __init__(self, canvas):
        Game.canvas = canvas           # Save canvas for future use
        self.gameObjects = [Background(), Ball(), Player(self, [330, 440], 2),Brick('blue',0,0)]          # A list of AL L game objects in the game
    
        #############################
        #   INSERT YOUR CODE HERE
        pass
        #############################

                
    def Draw(self):                    # This function draws ALL of the things
        Game.canvas.delete(ALL)        # First clear the screen
        for obj in self.gameObjects:   # Now the objects draw THEMSELVES one by one
            obj.Draw()            
       
            
    def LeftKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        print("Left key pressed")
        #############################

    
    def RightKeyPressed(self):        
        #############################
        #   INSERT YOUR CODE HERE
        print("Right key pressed")
        #############################

            
    def Update(self):                   # You can add all of your game logic here
        #############################   #   for example collision between game objects,
        #   INSERT YOUR CODE HERE       #   updating the state of the objects based
        pass                            #   on decisions or logic etc...
        #############################

        
            
#-----------------------------------


class GameWindow:
    def __init__(self):
        self.root = Tk()
        self.root.title("Project 2 -- Breakout Game")
        self.root.geometry('640x480')

        self.canvas = Canvas(self.root, width = 640, height = 480)
        self.canvas.grid(column=0, row=0)
        self.canvas.after(1, self.OneSecTimer)
        self.canvas.bind("<Key>", self.KeyPressed)
        self.canvas.focus_set()
        
        self.game = Game(self.canvas)    
        self.root.after(1, self.GameLoop)
        self.root.mainloop()
        self.colors = ["Grey", "Green", "Blue"]
        self.x = 30
        self.y = 20
        for color in self.colors:
            if color == "Grey" or "Green":
                
                for i in range(1,8):
                    b = Brick(color,self.x,self.y)
                    b.Draw()
                    
                    self.x+=30
                self.y+=20
            else :
                for i in range(1,8):
                    b = Brick(color,self.x,self.y)
                    b.Draw()
                    self.x+=20
                self.y+=20
    def KeyPressed(self, event):
        c = str(event.char)
        if c == 'a':
            self.game.LeftKeyPressed()
        if c == 'd':
            self.game.RightKeyPressed()

    
    def GameLoop(self):        
        self.game.Update()
        self.game.Draw()
        
        self.root.after(1000//60, self.GameLoop)

    def OneSecTimer(self):
        print("One second Tick")
        self.canvas.after(1000, self.OneSecTimer)
        
#-----------------------------------


game = GameWindow()

