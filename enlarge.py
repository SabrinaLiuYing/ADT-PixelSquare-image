from tabnanny import check  
from check import *  
from pixelsquare import *  
  
def enlarge(image, scale):  
    """"" 
    enlarge(image,scale) consumes an ADT PixelSquare image and 
        a positive integer scale that produces an ADT PixelSquare 
        that inlarge each pixel in image to a scale * scale block 
        of pixels of the same colour as the original pixel. 
    requires: 0 < scale 
    enlarge: PixelSquare Int -> PixelSquare 
    """  
    size = image.size()  
    # create a new PixelSquare  
    new_image = PixelSquare(size * scale)  
    # loop for each pixel in image  
    for i in range(size):  
        for j in range(size):  
            # get the colour of the pixel from image  
            color_for_image = image.get_colour(i,j)  
            # change the new_image to inlarge the pixels to scale*scale size  
            new_image.rectangle(i * scale, j * scale, scale, scale, color_for_image)  
    return new_image  
