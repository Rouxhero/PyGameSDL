# 
###########################
#  oOoOo Author oOoOo
#  
#  Name: Rouxhero
#  Date: 2022-11-23
#  Version: 0.1
###########################
import pygame

class DisplayManager:

    def __init__(self,size:tuple=(800,600)):
        """
        Create a DisplayManager

        Args:
            size (tuple, optional): size of the screen . Defaults to (800,600).
        """
        self.__size = size
        self.__screen = pygame.display.set_mode(self.__size)
    
    def draw(self,element:pygame.Surface,position:tuple):
        """
        Draw an element on the screen

        Args:
            element (pygame.Surface): element to draw
            position (tuple): Position of the element
        """
        self.__screen.blit(element,position)

    def update(self):
        """
        Update the screen
        """
        pygame.display.update()
    
    def clear(self):
        """
        Clear the screen
        """
        self.__screen.fill((0,0,0))

    def set_fullscreen(self):
        """
        Set the screen in fullscreen
        """
        self.__screen = pygame.display.set_mode(self.__size,pygame.FULLSCREEN)
    
    def set_windowed(self):
        """
        Set the screen in windowed
        """
        self.__screen = pygame.display.set_mode(self.__size)
    
    def set_size(self,size:tuple):
        """
        Set the size of the screen

        Args:
            size (tuple): Size of the screen
        """
        self.__size = size
        self.__screen = pygame.display.set_mode(self.__size)    
    
    def get_size(self)->tuple:
        """
        Get the size of the screen

        Returns:
            tuple: size of the screen
        """
        return self.__size
    
    def get_screen(self)->pygame.Surface:
        """
        Get the screen

        Returns:
            pygame.Surface: screen
        """
        return self.__screen    