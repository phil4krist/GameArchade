# The Candy Monster Game Porgram
from tkinter import*
import random

# make window
window = Tk()
window.title('The Candy Monster Game')

#create a canvas to put objects on the screen
canvas = Canvas(window, width = 400, height = 400, bg = 'black')
canvas.pack()

#set up up welcome screen with title and directions
title = canvas.create_text(200, 200, text = 'The Candy Monster', \
fill = 'white', font = ('Helvetica',30))
directions = canvas.create_text(200, 300, text = 'Collect Candy \
but avoid the red ones', fill = 'white', font = ('Helvetica', 20))

#set up score display using label widget
score = 0
score_display = Label(window, text = "Score: " + str(score))
score.display.pack()

# set up level display using widget label
level = 1
level_display = Label(window, text = 'Level: ' + str(level))
level.diplay.pack()

#create an image object using the gif file
player_image_file = PhotoImage(file = "greenChar.gif")
#use image object to create a character at position 200, 360
mychar = canvas.creat_image(200, 360, image = player_image_file)

#variables and lists needed for managing candy (database)
candy_list = [] # list containing all candy created,  empty at start
bad_candy_list = [] # list containing all bad candy created,  empty at start
candy_speed = 2 # initial speed of falling candy
candy_color_list = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'white']

# function to make candy at random places e.g make_candy(), move_candy(),

def make_candy():
    #pick a random position
    xposition = random.randint(1,400)
    # pick a random color
    candy_color = random.choice(candy_color_list)
    # create a candy of size 30 at random position and color
    candy = candy.create_oval(xposition, xposition+30, 30, fill = candy_color)
    # add candy to list
    candy_list.append(candy)
    # if color of candy is red - add it to bad_candy_list
    if candy_color == 'red':
        bad_candy_list.append(candy)
        # schedule this function to make can dy again
        window.after(1000, make_candy)

# function moves candy downwards, and schedules call to move_candy
def move_candy():
    #loop through list of candy and change y position (for counter in 10: do this)
    for candy in candy_list:
        canvas.move(candy, 0, candy_speed) #move(candy, x,y)
        # check if end of screen - restart at random position
        if canvas.coords(candy)[1] > 400:
            xposition = random.randint(1,400)
            canvas.coords(candy, xposition, 0, xposition+30, 30)
            # schedule this function to move candy again
            window.after(50, move_candy)









        







        
    
    

















