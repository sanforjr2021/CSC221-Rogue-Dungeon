# By Jacob Sanford & Alec Barker
# Date: 10/1/19
# Description: Load the basic Code

def main():
    try:
        import pygame
        print("PyGame is installed")
    except ImportError:
        print("Error: pygame not installed")
        print("py -m pip install -U pygame --user")
    print("Ain't this a great game!")


if __name__ == '__main__':
    main()
