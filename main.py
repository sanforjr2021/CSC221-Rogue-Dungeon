# By Jacob Sanford & Alec Barker
# Date: 10/1/19
# Description: Load the basic Code

def main():
    window = createWindow()
			
def createWindow():
    pygame.init()
    # load and set the logo
    pygame.display.set_caption("UMU Rogue Dungeon")

    # create a surface on screen that has the size of 1080 x 720
    screen = pygame.display.set_mode((1080, 720))

    # define a variable to control the main loop
    running = True

    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False


if __name__ == '__main__':
    try:
        import pygame
    except ImportError:
        print("Error: pygame not installed")
        print("Type this to install pygame on a windows machine: py -m pip install -U pygame --user")
        quit()
    main()
