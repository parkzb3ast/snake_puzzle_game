from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
import time
import random
import tkinter

from Character import Character
from Joystick import Joystick
from Enemy import Enemy
from Hit import Hit
   
state=0
def title():
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 255, 255, 100))
    
    while True:
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (170, 0, 136))
        
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        my_draw.multiline_text((40, 40), "Snake\nPuzzle:)", font=fnt, fill=(255, 255, 0))
        
        fnt= ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 20)
        my_draw.multiline_text((120, 150), "By Danny", font=fnt, fill=(255, 255, 0))
        
        joystick.disp.image(my_image)
        
        if not joystick.button_A.value:
            break


def main():
    global state
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    
    my_circle = Character(joystick.width, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 255, 255, 100))
    
    enemys_list=[]
    
    for i in range(num):
        x=random.randrange(10, 230, 5)
        y=random.randrange(10, 230, 5)
        food=Enemy((x,y))
        print(x,y)
        enemys_list.append(food)
        
    dots=[]
    intersect=[]
    
    while True:
        command = None
        if not joystick.button_U.value: 
            command = 'up_pressed'
            
            
        elif not joystick.button_D.value: 
            command = 'down_pressed'
            
        elif not joystick.button_L.value:  
            command = 'left_pressed'
            
        elif not joystick.button_R.value:  
            command = 'right_pressed'
            
        else:
            command = None

        my_circle.move(command)
        
        
        xdot=my_circle.position[0]
        ydot=my_circle.position[1]
        tup=(xdot,ydot)
        
        if tup not in intersect:
            intersect.append(tup)
        elif tup in intersect and tup!=(110,110):
            state=-1
            while True:
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
                fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
                my_draw.multiline_text((40, 40), "GAME\nOVER T.T", font=fnt, fill=(0, 0, 0))
                joystick.disp.image(my_image)
                if not joystick.button_A.value:
                    break
            break
        
        if (my_circle.position[0]<0 or my_circle.position[1]<0 or my_circle.position[2]>240 or my_circle.position[3]>240):
            state=-1
            while True:
                my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
                fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
                my_draw.multiline_text((40, 40), "GAME\nOVER T.T", font=fnt, fill=(0, 0, 0))
                joystick.disp.image(my_image)
                if not joystick.button_A.value:
                    break
            break
        
        hit=Hit(my_circle.position+5, command)
        dots.append(hit)
        
        hit.collision_check(enemys_list)
        
        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        
        my_draw.ellipse(tuple(my_circle.position), fill = (0, 0, 0))
        
        for enemy in enemys_list:
            if enemy.state != 'die':
                my_draw.rectangle(tuple(enemy.position), fill = (255, 0, 0))
          
        for hit in dots:
            my_draw.ellipse(tuple(hit.position), outline = hit.outline, fill = (0, 0, 0))
            
        if all(enemy.state=='die' for enemy in enemys_list):
            break
        
        joystick.disp.image(my_image)
        

if __name__ == '__main__':
    while True:   
        title()
        num=5
        state=0
        
        while state==0:
            main()
            num=num+1
            if state==-1:
                break
    
