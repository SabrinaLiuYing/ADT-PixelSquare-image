from operator import contains  
from check import *  
from pixelsquare import *  
from contiguous import *  
from multiset import *  
  
def censor(image, forbidden):  
    """"" 
    censor(image, forbidden) consumes an ADT PixelSquare image and 
        an ADT Multiset forbidden that mutates image by replacing  
        any colour in forbidden with the colour "x" 
    effect: mutates image by replacing any colour in forbidden  
        with the colour "x" 
    censor: PixelSquare Multiset -> PixelSquare 
    """  
    size = image.size()  
    # loop for each pixel in image  
    for i in range(size):  
        for j in range(size):  
            # get the colour of the pixel from image  
            color_for_image = image.get_colour(i,j)  
            # check if the colour is in forbidden multiset  
            if contains(forbidden,color_for_image):  
                # change the colour in forbidden with the colour "x"  
                image.set_colour(i,j,"x")      
    return image  
