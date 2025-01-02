from pygame import *
from random import choice
import sys
# We create a class for our game
class PongGame:
    # Game mai jo bhi constants use horhe unhe declare 
    WIDTH, HEIGHT = 800, 600
    BLACK = (0,0,0)
    WHITE = (255,255,255)
    PADDLE_WIDTH = 15
    PADDLE_HEIGHT = 100
    BALL_RADIUS = 15
    BALL_SPEED_X = 5
    BALL_SPEED_Y = 5
    
    
    