import pygame as pg 
import sys 
import time 
from pygame.locals import *


game_board = [
  [None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None],
  [None,None,None,None,None,None,None]
]
player_turn = 'x' 
winner = None
tie = None 


width = 700
height = 600

# init pg
pg.init()
CLOCK = pg.time.Clock()
fps = 30 

screen = pg.display.set_mode((width, height+100), 0, 32)
pg.display.set_caption("Connect Four")





def reset_game():
  global game_board, player_turn, winner, tie
  game_board = [
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None],
    [None,None,None,None,None,None,None]
  ]
  player_turn = 'x' 
  winner = None
  tie = None 



def print_game():
  s=""
  for i in range(len(game_board)):
      s+="|"
      for j in range(len(game_board[i])):
        if game_board[i][j] == None:
          s+=" "
        else:
          s+=game_board[i][j]
        s+="|"
      s+="\n"
  s+="---------------"
  print(s)


def check_win():
  global winner, tie 
  for col in range(len(game_board[0])):
      row = 0
      for row in range(0,3):
        if game_board[row][col] is not None and game_board[row][col] == game_board[row+1][col] and game_board[row+1][col] == game_board[row+2][col] and game_board[row+2][col] == game_board[row+3][col]:
          winner = game_board[row][col]
          return True 

  ### check for 4 in a row across 
  for row in range(len(game_board)):
    col = 0 
    for col in range(0,4):
      if game_board[row][col] is not None and game_board[row][col] == game_board[row][col+1] and game_board[row][col+1] == game_board[row][col+2] and game_board[row][col+2] == game_board[row][col+3]:
          winner = game_board[row][col]
          return True 
  # check diagonals
  for row in reversed(range(3,6)):
    for col in range(len(game_board[row])):
      if col <=3:
        #check by going up-right
        if game_board[row][col] is not None and game_board[row][col] == game_board[row-1][col+1] and game_board[row][col] == game_board[row-2][col+2] and game_board[row][col] == game_board[row-3][col+3]:
          winner = game_board[row][col]
          return True
      if col>=3:
        #check by going up-left
        if game_board[row][col] is not None and game_board[row][col] == game_board[row-1][col-1] and game_board[row][col] == game_board[row-2][col-2] and game_board[row][col] == game_board[row-3][col-3]:
          winner = game_board[row][col]
          return True
  return False 




def game_init_window():
  pg.display.update() 
  time.sleep(1)
  screen.fill((0,255,255))
  # pg.draw.line(screen, line_color, )
  line_color = (0, 0, 255)
  pg.draw.line(screen, line_color, (width/3,0), (width/3,height), 5)
  pg.draw.line(screen, line_color, (width*2/3,0), (width*2/3,height), 5)
  pg.draw.line(screen, line_color, (0,height/3), (width, height/3), 5)
  pg.draw.line(screen, line_color, (0, height*2/3), (width,height*2/3), 5)

  line_color = (0,0,0)
  pg.draw.line(screen, line_color, (0, height), (width, height), 5)
  # clear out existing events
  pg.event.get()

def show_status(text):

  # fill status bar.
  screen.fill((0,0,0), (0, height,width,100))
  font = pg.font.Font(None, 30)
  text_obj = font.render(text, 1, (255,255,255))
  text_rect = text_obj.get_rect()
  text_rect.center =(width/2,height+50) 
  screen.blit(text_obj, text_rect)
  pg.display.update() 
  
reset_game()
game_init_window()

# game loop
while(True):
  # pg.event.get() 
  # write text status 
  show_status("Player " + player_turn+"'s turn")
  for event in pg.event.get():
    if event.type is MOUSEBUTTONDOWN:
      click() 
      if check_win():
        reset_game()
        game_init_window()
      # write text status

  pg.display.update()
  CLOCK.tick(fps)
