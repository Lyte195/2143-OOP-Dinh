# Luong Dinh
Due: December 9.

```python
import sys
from PIL import Image
import random
from random import randint
"""
@Luong Dinh
@Class: ImageEdit
@Description:
    Represent an image with height and width
@Methods
    glassEffect - make image have glass effect
    flip - flip image vertical
    blur - make image blur
    posterize - posterize image
    solarize - solarize image
    warhol - make image have warhol effect
"""
class ImageEdit(object):
    def __init__(self,image):
        self.width =  image.size[0]
        self.height = image.size[1]

    """
    @Method: glassEffect
    @Description:
        Pick a random pixel
        Pick 2 nother pixel from 5 position up and down from pixel 1
        Then add those 2 together
        Then assign ^ this value to the first pixel picked
    """
        
    def glassEffect(self,image,distance = 5):
        i = randint(0,self.width)
        nums = [x for x in range(i - distance, i + distance) if x >= 0]
        
        for w in range(0,self.width):
            for h in range(0, self.height):
                choice = random.choice(nums)
                xPos = w
                yPos = h              
                newX = (xPos - choice) + (xPos + choice)
                newY = (yPos - choice) + (yPos + choice)
                color = image.getpixel((h,w))
                image.putpixel((newX,newY),color)

        return image
           
    """
    @Method: flip
    @Description:
        Flip the picture vertically by loop through entire image one row at a time:
        exchange current row with opposite row 
    """    
    def flip(self,image):
        for w in range(0, self.width):
          for h in range(0, self.height):
            opposite = (self.height - w)
            color = image.getpixel((h,opposite))
            image.putpixel((h,opposite),color)

        return image

    """
    @Method: blur
    @Description:
        Blur the image give, this function was given in 
        class.
    """
        
    def blur(self,image,blur_lvl = 5):
        r = 0
        g = 0
        b = 0
        d = 2*blur_lvl * 2*blur_lvl
        for x in range(blur_lvl,self.width - blur_lvl):
          for y in range(blur_lvl,self.height - blur_lvl):
            for i in range(-blur_lvl,blur_lvl):
              for j in range(-blur_lvl,blur_lvl):
                pix = image.getpixel((x+i,y+j))
                r += pix[0]
                g += pix[1]
                b += pix[2]
            image.putpixel((x,y),(int(r/d),int(g/d),int(b/d)))
            r = 0
            g = 0 
            b = 0
        
        return image

    """
    @Method: posterize
    @Description:
        Posterize an image using a snap value to test and 
        reducing the number of colors present in an image.
    """
    def posterize(self,image,snap_val):
        for w in range(0,self.width):
            for h in range(0, self.height):
                r, g, b = image.getpixel((w,h))

                newR = r % snap_val
                newG = g % snap_val
                newB = b % snap_val

                if newR < (snap_val // 2):
                    r -= newR
                else:
                    r += (snap_val - newR)

                if newG < (snap_val // 2):
                    g -= newG
                else:
                    g += (snap_val - newG)

                if newB < (snap_val // 2):
                    b -= newB
                else:
                    b += (snap_val - newB)

                color = (r,g,b)
                image.putpixel((w,h), color)

        return image

    """
    @Method: solarize
    @Description:
        Solarize and image by partial negation of the image
        using an intensity value to test each color value
        against the intensity the adjust the color occordingly.
    """
   
    def solarize(self,image,intensity=1):
        for w in range(0,self.width):
            for h in range(0, self.height):
                r, g, b = image.getpixel((w,h))

                if r < intensity:
                    r = intensity - r
                else:
                    r += intensity

                if g < intensity:
                    g = intensity - g
                else:
                    g += intensity

                if b < intensity:
                    b = intensity - b
                else:
                    b += intensity

                color = (r,g,b)
                image.putpixel((w,h), color)

        return image

    """
    @Method: warhol
    @Description:
        Given warhol effect to an image by making a coppy
        of the original image then gray scaling it.
        Then differnt color values were added in each pixel
        if the shade of red is at a certain threshold.
    """    
    def warhol(self,image):
      

        newImage = image.copy()
        orange = (255,165,0)
        green = (0,255,0)
        blue = (0,0,255)
        pink = (255,192,203)
        yellow = (255,255,0)

        for w in range(0,self.width):
            for h in range (0, self.height):
                r, g, b = image.getpixel((w, h))
                grayscale = int((r+g+b)//3)
                newImage.putpixel((w, h), (grayscale, grayscale, grayscale))
                pixel = newImage.getpixel((w,h))      

                if (r >0 and r <= 51):
                    newImage.setColor(pixel,blue)
                elif (r > 51 and r <= 102):
                    newImage.setColor(pixel,yellow)
                elif (r > 102 and r <= 153):
                    newImage.setColor(pixel,orange)      
                elif (r > 153 and r <= 204):
                    newImage.setColor(pixel,pink)
                else:
                    newImage.setColor(pixel,green)     

        return newImage
```
