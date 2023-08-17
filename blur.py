from operator import contains  
from check import *  
from pixelsquare import *  
from contiguous import *  
from multiset import *  
  
def blur(image, block_size):  
    """"" 
    blur(image, block_size) consumes an ADT PixelSquare image and 
        a positive integer block_size that mutates image by blurring 
        out the details of the image. 
    effect: mutates image by blurring out the details of the image. 
    requires: 0 < block_size 
    enlarge: PixelSquare Int -> PixelSquare 
    """  
    #inite constant value  
    size = image.size()  
    WHITE = "."  
    BLACK = "#"  
    GRAY = "-"  
    # loop for each non-overlapping squares of dimension block_size  
    for i in range(0, size, block_size):  
        for j in range(0, size, block_size):  
            # black_num is the number of black pixels in the square  
            black_num = 0  
            # white_num is the number of white pixels in the square  
            white_num = 0  
            # loop for each pixels in the square  
            for p in range(i, i + block_size):  
                for q in range(j, j + block_size):  
                    # check if the pixel is black or white and record the resilt  
                    if image.get_colour(p,q) == BLACK:  
                        black_num += 1  
                    elif image.get_colour(p,q) == WHITE:  
                        white_num += 1  
            # check the relationship of the numbers of white and black pixels  
            if white_num > black_num :  
                # if more white change all colours in the square to white   
                image.rectangle(i, j, block_size, block_size, WHITE)  
            elif white_num < black_num :  
                # if more black change all colours in the square to black   
                image.rectangle(i, j, block_size, block_size, BLACK)  
            else:  
                # if the same change all colours in the square to gray  
                image.rectangle(i, j, block_size, block_size, GRAY)              
    return image 
