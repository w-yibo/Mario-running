import pygame
from source import tools
from state import main_menu,load,play
def main():
    state_dict={
        'main_menu':main_menu.main_menu(),
        'load':load.load(),
        'play':play.play(),
        'gameover':load.gameover(),
        'win':load.win()
    }
    game=tools.Game(state_dict,'main_menu')
    game.start()

if __name__ == '__main__':
    main() 
