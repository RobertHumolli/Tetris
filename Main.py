import pygame,sys

from grid import Grid    #An OOP principle that allows us to call a class from a different file

pygame.init()
dark_blue = (44, 44, 127)


screen = pygame.display.set_mode((300,600)) #This sets the display for the game
pygame.display.set_caption("Tetris")

clock = pygame.time.Clock()

game_grid = Grid()    #This uses the class and allows us to use the Grid on the Display
game_grid.print_grid()

while True:         #This is the main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()               #This will exit the display once the game is finished
            sys.exit()

    screen.fill(dark_blue) #Colour can be updated

    pygame.display.update()         #This will update the display
    clock.tick(60)                  #This sets the ticks for the game, which I will be running it at 60 frames per second

