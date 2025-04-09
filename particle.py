import grid
import random
import colorsys

#sand color
MUSTARD = (255,191,0)

#rock color
LIGHT_GREY = (128,128,128)


class SandParticle:
    def __init__(self):
        self.color = self.color_randomizer()

    def color_randomizer(self):
        hue = random.uniform(0.1,0.13)
        saturation = random.uniform(0.5,0.7)
        value = random.uniform(0.6,0.8)

        r,g,b = colorsys.hsv_to_rgb(hue,saturation,value)
        return int(r*255),int(g*255),int(b*255)
    
    def update(self,grid,row,column):
        if grid.is_empty(row+1,column): # check if cell directly below is empty
            return row+1,column
        elif grid.is_empty(row+1,column+1): #check if right bottom cell is empty
            return row+1,column+1
        elif grid.is_empty(row+1,column-1): #check if left bottom cell is empty
            return row+1,column-1
        elif grid.is_empty(row+1,column+1) and grid.is_empty(row+1,column-1):
            choice = random.randint(0,1)
            if(choice == 0):
                return row+1,column+1
            else:
                return row+1,column-1
        else:
            return row,column
    

class RockParticle:
    def __init__(self):
        self.color = self.color_randomizer()

    def color_randomizer(self):
        hue = random.uniform(0.0,0.1)
        saturation = random.uniform(0.1,0.3)
        value = random.uniform(0.3,0.5)

        r,g,b = colorsys.hsv_to_rgb(hue,saturation,value)
        return int(r*255),int(g*255),int(b*255)
    
    # def update(self,row,column):
