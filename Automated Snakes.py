######### IMPORTING PACKAGES ##########
from graphics import *
import random
import time


def mapupdate(mapp, window, snake, direc):
      mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()/100))
      mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()/100))
      mapp[mapx][mapy] = direc
      return mapp, mapx, mapy


def eaten(mapp, snakebody, food, length, direction, window):
      xypoint = snakebody[0].getCenter()
      head = snakebody[0]
      p2 = head.getP1()
      p1 = head.getP2()

      if direction == 'l':
            prep1 = snakebody[0].getP1().getX() - window.getWidth()//100
            prep2 = snakebody[0].getP2().getX() - window.getWidth()//100
            if prep1 < window.getWidth() and prep1 > 0 and prep2< window.getWidth() and prep2 > 0:
                  mapp, mapx, mapy = mapupdate(mapp, window, snake, 'l')
                  snakebody[0].move(-window.getWidth()//100, 0)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'l'
                  
            else:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake, 'd')
                  snakebody[0].move(0, window.getHeight()//100)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  
                  direction = 'd'
      elif direction =='r':
            prep1 = snakebody[0].getP1().getX() + window.getWidth()//100
            prep2 = snakebody[0].getP2().getX() + window.getWidth()//100
            if prep1 < window.getWidth() and prep1 > 0 and prep2< window.getWidth() and prep2 > 0:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake, 'r')
                  snakebody[0].move(window.getWidth()//100, 0)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  
                  direction = 'r'
            else:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake,'u')
                  snakebody[0].move(0, -window.getHeight()//100)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'u'
      elif direction =='u':
            prep1 = snakebody[0].getP1().getY() - window.getHeight()//100
            prep2 = snakebody[0].getP2().getY() - window.getHeight()//100
            if prep1 < window.getHeight() and prep1 > 0 and prep2< window.getHeight() and prep2 > 0:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake,'u')
                  snakebody[0].move(0, -window.getHeight()/100)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'u'
            else:
                  mapp, mapx, mapy = mapupdate(mapp, window, snake, 'l')
                  snakebody[0].move(-window.getHeight()//100, 0)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'l'
      else:
            prep1 = snakebody[0].getP1().getY() + window.getHeight()//100
            prep2 = snakebody[0].getP2().getY() + window.getHeight()//100
            if prep1 < window.getHeight() and prep1 > 0 and prep2< window.getHeight() and prep2 > 0:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake,'d')
                  snakebody[0].move(0, window.getHeight()/100)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'd'
      
            else:
                  mapp,mapx, mapy = mapupdate(mapp, window, snake,'r')
                  snakebody[0].move(window.getWidth()//100, 0)
                  newspot = Rectangle(p1, p2)
                  newspot.setFill('red')
                  newspot.draw(window)
                  snakebody.insert(1, newspot)
                  direction = 'r'

      #New food
      foodrep = True
      xypoint = food.getCenter()
      foodpoint = [xypoint.getX(),xypoint.getY()]
      while foodrep:
            x = random.randint(0,50)
            y = random.randint(0,50)
            direcx = random.randint(0,1)
            direcy = random.randint(0,1)
            if direcx == 0:
                  direcx = 1
            else:
                  direcx = -1
            if direcy == 0:
                  direcy = 1
            else:
                  direcy = -1
            xchange = x*(window.getWidth()//100)*direcx
            ychange = y*(window.getHeight()//100)*direcy
            if ((foodpoint[0] + xchange) < window.getWidth()) and ((foodpoint[0] + xchange) > 0) and ((foodpoint[1] + ychange) < window.getHeight()) and ((foodpoint[1] + ychange) > 0):
                  food.move(xchange,ychange)
                  foodrep = False
      xypoint = food.getCenter()
      foodpoint = [xypoint.getX(),xypoint.getY()]
      
      return direction, snakebody, foodpoint


def cube_overlap(cube1, cube2, xdiff, ydiff):

      next_x = cube1.getCenter().getX() + xdiff
      next_y = cube1.getCenter().getY() + ydiff

      return cube2.getP1().getX() > next_x > cube2.getP2().getX() and cube2.getP1().getY() > next_y > cube2.getP2().getY()


def bodycheck(mapp, direction, snakebody):
      move = True
      for bodypart in snakebody:
            if direction == 'u':
                  if cube_overlap(snakebody[0], bodypart, 0, -window.getHeight()//100):
                        move = False
                        direction = 'l'
                        print('MOVE DENIED')
            elif direction =='d':
                  if cube_overlap(snakebody[0], bodypart, 0, window.getHeight() // 100):
                  # if snakebody[0].getCenter().getY() + window.getHeight()//100 == bodypart.getCenter().getY():
                        move = False
                        direction = 'r'
                        print('MOVE DENIED')
            elif direction == 'l':
                  if cube_overlap(snakebody[0], bodypart, -window.getWidth()//100, 0):
                  #if snakebody[0].getCenter().getX() - window.getWidth()//100 == bodypart.getCenter().getX():
                        move = False
                        direction = 'd'
                        print('MOVE DENIED')
            else:
                  if cube_overlap(snakebody[0], bodypart, window.getWidth()//100, 0):
                  #if snakebody[0].getCenter().getX() + window.getWidth()//100 == bodypart.getCenter().getX():
                        move = False
                        direction = 'u'
                        print('MOVE DENIED')
      return move, direction



def bodymove(window, snakebody, direction):
      if len(snakebody) > 0:
            for i in range(1, len(snakebody)):
                  x = int(snakebody[i].getCenter().getX()//(window.getWidth()/100))
                  y = int(snakebody[i].getCenter().getY()//(window.getHeight()/100))
                  if mapp[x][y] == 0:
                        direction = direction
                  else:
                        direction = mapp[x][y]
                  if direction == 'l':
                        snakebody[i].move(-window.getWidth()//100, 0)
                  elif direction =='r':
                        snakebody[i].move(window.getWidth()//100, 0)
                  elif direction == 'u':
                        snakebody[i].move(0, -window.getHeight()//100)
                  else:
                        snakebody[i].move(0, window.getHeight()//100)
      return snakebody, window
##MAP
slot = []
mapp = []
for i in range(100):
      mapp.append(slot.copy())
for i in range(100):
      for v in range(100):
            mapp[i].append(0)
x = random.randint(1,99)
y = random.randint(1,99)
window = GraphWin('Snake Game', 500,500)
## SNAKE
snakebody = []


###
snake = Rectangle(Point((x*window.getWidth()//100),(y*window.getWidth()//100)), Point((x*window.getWidth()//100) + window.getWidth()//100,(y*window.getWidth()//100) + window.getHeight()//100))
color = 'red'
snake.setFill(color)
snake.draw(window)
mapp[x][y] = '0'
xypoint = snake.getCenter()
snakepoint = [xypoint.getX(),xypoint.getY()]
snakebody.append(snake)
## FOOD
x = random.randint(0,99)
y = random.randint(0,99)
food = Rectangle(Point((x*window.getWidth()//100),(y*window.getWidth()//100)), Point((x*window.getWidth()//100) + window.getWidth()//100,(y*window.getWidth()//100) + window.getHeight()//100))
food.setFill('green')
food.draw(window)
mapp[x][y] = 'X'
xypoint = food.getCenter()
foodpoint = [xypoint.getX(),xypoint.getY()]
length = 0
run = True
direction = 'o'
times = 0.00004
while run:
      xypoint = snakebody[0].getCenter()
      snakepoint = [xypoint.getX(),xypoint.getY()]
      while foodpoint[0] != snakepoint[0]:
            move, direction = bodycheck(mapp, direction, snakebody)
            time.sleep(times)
            if foodpoint[0] < snakepoint[0] and direction != 'r':
                  direction = 'l'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(-window.getWidth()//100, 0)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
            elif foodpoint[0] > snakepoint[0] and direction != 'l':
                  direction = 'r'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(window.getWidth()//100, 0)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
            else:
                  direction = 'u'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(0, -window.getHeight()//100)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
      while foodpoint[1] !=snakepoint[1] :
            move, direction = bodycheck(mapp, direction, snakebody)
            time.sleep(times)
            if foodpoint[1] < snakepoint[1] and direction != 'd':
                  direction = 'u'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(0, -window.getHeight()//100)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
            elif foodpoint[1] > snakepoint[1] and direction != 'u':
                  direction = 'd'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(0, window.getHeight()//100)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
            else:
                  direction = 'r'
                  mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
                  mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
                  mapp[mapx][mapy] = direction
                  snakebody[0].move(window.getWidth()//100, 0)
                  xypoint = snakebody[0].getCenter()
                  snakepoint = [xypoint.getX(),xypoint.getY()]
                  snakebody, window = bodymove(window, snakebody, direction)
      direction, snakebody, foodpoint= eaten(mapp, snakebody, food, length,direction, window)
      mapx = int(snakebody[0].getCenter().getX()//(window.getWidth()//100))
      mapy = int(snakebody[0].getCenter().getY()//(window.getHeight()//100))
      mapp[mapx][mapy] = direction
for v in range(len(mapp)):
      print(mapp[v])
      




            
