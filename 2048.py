import turtle
import random
import math
 
class theGame():
  def __init__(self):
    self.board_drawer = turtle.Turtle()
    self.writer = turtle.Turtle()
    self.screen_width = turtle.Screen().window_width()
    self.screen_height = turtle.Screen().window_height()
    self.setScale()
    self.square_size = self.box_size / 4
    self.total_squares = 16
    self.width = 1
    self.height = 1
    self.board_xcor = turtle.Screen().window_width() / -5.5
    self.board_ycor = turtle.Screen().window_height() / 2.5
    self.drawGrid()
    self.boardstate = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    self.changedSqs = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]
    self.addBlock()
    self.addBlock()
    self.display()
    self.scoreturtle = turtle.Turtle()
    self.scoreturtle.ht()
    self.trasht = turtle.Turtle()
    self.trasht.ht()
    self.registerShapes()
  
  def registerShapes(self):
    x = self.square_size / 2.0
    screen = turtle.Screen()
    screen.addshape("sq", ((x, x), (-x, x), (-x, -x), (x, -x)))
    
  def setScale(self):
    if self.screen_width < self.screen_height:
      self.box_size = self.screen_width / 1.5
    else:
      self.box_size = self.screen_height / 1.5
   
  def drawGrid(self):
    self.board_drawer.penup()
    self.board_drawer.ht()
    self.board_drawer.speed(0)
    self.board_drawer.setpos(self.board_xcor,
                             self.board_ycor)
    self.board_drawer.pendown()
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.right(90)
    self.board_drawer.pendown()
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width)
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.height)
    self.board_drawer.penup()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.square_size * self.width) 
    self.board_drawer.pendown()
    self.board_drawer.right(90)
    self.board_drawer.forward(self.box_size * self.width)
    self.board_drawer.penup()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.square_size * self.width) 
    self.board_drawer.pendown()
    self.board_drawer.left(90)
    self.board_drawer.forward(self.box_size * self.width) 
   
  def score(self):
    returnval = 0
    for x in range(0, 4):
      for y in range(0, 4):
        returnval += self.boardstate[x][y]
    return returnval
  
  def display(self):
    self.writer.clear()
    self.writer.penup()
    self.writer.speed(0)
    self.writer.ht()
    color = "purple"
    for x in range(0, 4):
      for y in range(0, 4):
        #b = turtle.Turtle()
        #b.speed(0)
        #b.shape("sq")
        #b.color(color)
        #b.penup()
        #b.setpos(self.board_xcor + (0.5 + y) * self.square_size,
        #                     self.board_ycor - (x - 0.5) * self.square_size)    
        self.writer.setpos(self.board_xcor + self.square_size / 8 + y * self.square_size,
                             self.board_ycor - self.square_size * 2 / 3 - x * self.square_size)    
        self.writer.write(str(self.boardstate[x][y]), False, font=("Arial", 14, "normal"))
  
  def emptySpaces(self):
    returnval = []
    for x in range(0, 4):
      for y in range(0, 4):
        if self.boardstate[x][y] == 0:
          returnval.append([x , y])
    return returnval
    
  def addBlock(self):
    x = random.randrange(1, 9)
    blockval = 2
    emptyspaces = self.emptySpaces()
    if x == 1:
      blockval = 4
    y = random.randrange(0, len(emptyspaces))
    insertblock = emptyspaces[y]
    self.boardstate[insertblock[0]][insertblock[1]] = blockval
    
  def canMerge(self, r_b1, c_b1, r_b2, c_b2):
    return ((self.boardstate[r_b1][c_b1] == self.boardstate[r_b2][c_b2]) and not (self.boardstate[r_b2][c_b2] == 0))

  def validCombineMove(self):
    for x in range(0, 4):
      for y in range(0, 4):
        if(self.validLoc(x-1, y) and self.canMerge(x, y, x-1, y)):
          return True
        if(self.validLoc(x+1, y) and self.canMerge(x, y, x+1, y)):
          return True
        if(self.validLoc(x, y-1) and self.canMerge(x, y, x, y-1)):
          return True
        if(self.validLoc(x, y+1) and self.canMerge(x, y, x, y+1)):
          return True
    return False
  
  def validDirMove(self, deg):
    for x in range(0, 4):
      for y in range(0, 4):
        if(deg == 270 and self.validLoc(x+1, y) and (self.canMerge(x, y, x+1, y) or ((not (self.boardstate[x][y] == 0)) and self.boardstate[x+1][y] == 0))):
          return True
        elif(deg == 90 and self.validLoc(x-1, y) and (self.canMerge(x, y, x-1, y) or ((not (self.boardstate[x][y] == 0)) and self.boardstate[x-1][y] == 0))):
          return True
        elif(deg == 180 and self.validLoc(x, y-1) and (self.canMerge(x, y, x, y-1) or ((not (self.boardstate[x][y] == 0)) and self.boardstate[x][y-1] == 0))):
          return True
        elif(deg == 0 and self.validLoc(x, y+1) and (self.canMerge(x, y, x, y+1) or ((not (self.boardstate[x][y] == 0)) and self.boardstate[x][y+1] == 0))):
          return True
    return False
  
  def gameOver(self):
    turtle.Screen().resetscreen()
    self.scoreturtle.speed(0)
    self.scoreturtle.ht()
    self.scoreturtle.penup()
    self.scoreturtle.setposition(0, self.screen_height / 6.5)
    self.scoreturtle.write("Final Score: " + str(self.score()), False, align="center", font=("Arial", 32, "normal"))
    self.scoreturtle.setposition(0, -self.screen_height / 6.5)
    self.scoreturtle.write("Game Over!", False, align="center", font=("Arial", 32, "normal"))
  
  def swap(self, r_b1, c_b1, r_b2, c_b2):
    temp = self.boardstate[r_b1][c_b1]
    self.boardstate[r_b1][c_b1] = self.boardstate[r_b2][c_b2]
    self.boardstate[r_b2][c_b2] = temp
    
  def validLoc(self, row, col):
    if((-1 < col and col < 4) and (-1 < row and row < 4)):
      return True
    else:
      return False
    
  def attemptMove(self, deg):
    if self.validDirMove(deg):
      self.makeMove(deg)
      self.addBlock()
      if not(self.validCombineMove()) and len(self.emptySpaces()) == 0:
        self.gameOver()
      else:
        self.changedSqs = [[False, False, False, False], [False, False, False, False], [False, False, False, False], [False, False, False, False]]     
        self.display()
    else:
      print("not a valid move!")
      
  def makeMove(self, deg):
    cond = True
    cAdj = 1
    rAdj = 1
    direction = 0 #1 = E/W movement, 2 = N/S
    start_c = 0
    end_c = 4
    start_r = 0
    end_r = 4
    
    if deg == 0:
      direction = 1
      start_c = 3
      end_c = -1
      
    if deg == 180:
      cAdj = -1
      direction = 1
      
    if deg == 90:
      rAdj = -1
      direction = 2
      
    if deg == 270:
      start_r = 3
      end_r = -1
      direction = 2
      
    if direction == 1:
      for r in range(0, 4):
        c = start_c
        while not c == end_c:
          cond = True
          if not(self.boardstate[r][c] == 0):
            cCur = c
            while cond and self.validLoc(r, cCur + cAdj) and not self.changedSqs[r][cCur]:
              if self.boardstate[r][cCur + cAdj] == 0:
                self.swap(r, cCur, r, cCur + cAdj)
              elif self.canMerge(r, cCur, r, cCur + cAdj):
                if not self.changedSqs[r][cCur + cAdj]:
                  self.boardstate[r][cCur + cAdj] *= 2
                  self.changedSqs[r][cCur + cAdj] = True
                  self.boardstate[r][cCur] = 0 
              else:
                cond = False
              cCur += cAdj
              self.doNothing()
          c -= cAdj
          self.doNothing()
            
    if direction == 2:
      for c in range(0, 4):
        r = start_r
        while not r == end_r:
          cond = True
          if not(self.boardstate[r][c] == 0):
            rCur = r
            while cond and self.validLoc(rCur + rAdj, c) and not self.changedSqs[rCur][c]:
              if self.boardstate[rCur + rAdj][c] == 0:
                self.swap(rCur, c, rCur + rAdj, c)
              elif self.canMerge(rCur, c, rCur + rAdj, c):
                if not self.changedSqs[rCur + rAdj][c]:
                  self.boardstate[rCur + rAdj][c] *= 2
                  self.changedSqs[rCur + rAdj][c] = True
                  self.boardstate[rCur][c] = 0 
              else:
                cond = False
              rCur += rAdj
              self.doNothing()
          r -= rAdj
          self.doNothing()
            
  def doNothing(self):
    self.trasht.ht()
    
game = theGame()
screen = turtle.Screen()

def upArrowPressed():
  game.attemptMove(90)

def downArrowPressed():
  game.attemptMove(270)
    
def leftArrowPressed():
  game.attemptMove(180)
    
def rightArrowPressed():
  game.attemptMove(0)
  
screen.onkey(upArrowPressed, "Up")
screen.onkey(downArrowPressed, "Down")
screen.onkey(leftArrowPressed, "Left")
screen.onkey(rightArrowPressed, "Right")
screen.listen()
