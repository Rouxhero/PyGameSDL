# 
###########################
#  oOoOo Author oOoOo
#  
#  Name: Rouxhero
#  Date: 2022-11-23
#  Version: 0.1
###########################
import pygame
from util.color import *


def load_image(path:str,size:tuple=None)->pygame.Surface:
    """
    Load an image and resize it

    Args:
        path (str): Path of images
        size (tuple): size to resize

    Returns:
        pygame.Surface: loaded images
    """
    image = pygame.image.load(path)
    if size != None:
        image = pygame.transform.scale(image,size)
    return image



def create_text(text:str,color:tuple=BLACK,size:int=20,font:str="Arial")->pygame.Surface:
    """
    Create a text

    Args:
        text (str): text to create
        color (tuple, optional): color of text. Defaults to BLACK.
        size (int, optional): size of text. Defaults to 20.
        font (pygame.font, optional): font of text. Defaults to "Arial".

    Returns:
        pygame.Surface: text
    """
    font = pygame.font.SysFont(font,size)
    text = font.render(text,True,color)
    return text


