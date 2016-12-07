import sys
from PIL import Image
import random
from random import randint

class ImageEdit(object):
    def __init__(self,image):
        self.width =  image.size[0]
        self.height = image.size[1]
        self.image = image
        
    def glassEffect(self,image,distance=5,imageout=None):
        i = randint(0,self.width)
        nums = [x for x in range(i - distance, i + distance) if 0 <= x <= self.width]
        
        for h in range(0,self.width):
            for w in range(0, self.height):
                choice = random.choice(nums)
                xPos = h
                yPos = w              
                newX = (xPos - choice) + (xPos + choice)
                newY = (yPos - choice) + (yPos + choice)
                color = image.getpixel((h,w))
                image.putpixel((newX,newY),color)
           
    
    def flip(self,image,imageout=None):
        for h in range(0, self.width):
          for w in range(0, self.height):
            opposite = (self.height - w)
            color = image.getpixel((h,opposite))
            image.putpixel((h,opposite),color)


        
    def blur(self,image,blur_lvl = 5,imageout=None):
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


    def posterize(self,image,snap_val,imageout=None):
        for h in range(0,self.width):
            for w in range(0, self.height):
                r, g, b = image.getpixel((h,w))

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
                image.putpixel((h,w), color)
   
    def solarize(self,image,intensity=1,imageout=None):
        for h in range(0,self.width):
            for w in range(0, self.height):
                r, g, b = image.getpixel((h,w))

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
                image.putpixel((h,w), color)
        
    def warhol(self,image,imageout=None):
        print("poslering")
    

        
print(sys.argv)

flags = ['-i','-o','-x','-h']

commands = {}

for i in range(1,len(sys.argv),2):
    commands[sys.argv[i]] = sys.argv[i+1]

commands['-x'] = commands['-x'].split(',')
print(commands)
ie = ImageEdit()

if '-i' in commands.keys():
    input_file = commands['-i']
    
if '-o' in commands.keys():
    output_file = commands['-o']
else:
    output_file = commands['-i']

if commands['-x'][0] == 'flip':
    ie.flip(input_file,output_file) 
