###########################################################
## File Name: fractals.py                                ##
## Description: Fractals assignement in Pygame           ##
###########################################################

# Import statements
import pygame, math, random, buttons
pygame.init()

#---------------------------------------#
# initialize global variables/constants #
#---------------------------------------#
W, H = 700, 480 
BLUE = (196, 242, 255)
PINK = (255, 190, 220)
BLACK = (0,0,0)
BROWN = (112, 90, 54)
WHITE = (255, 255, 255)
greens = [(61, 235, 75), (5, 153, 17), (32, 199, 45), (2, 191, 17), (11, 224, 28)]
titleFont = pygame.font.SysFont("centurygothic", 55)
subTitleFont = pygame.font.SysFont("centurygothic", 25)
txtFont = pygame.font.SysFont("yugothicyugothicuilight", 20)

#----------------------------------------#
# draws a tree with the given parameters #
#----------------------------------------#
def tree(x1,y1,angle,length,w,startCoords,y,winter):
    global BROWN
    if length > 5:
        # Creates new coordinates using trigonometry
        x2 = int(x1 + length * math.cos(angle))
        y2 = int(y1 + length * math.sin(angle))
        if (x1,y1) == startCoords:
            y = y2
        pygame.draw.line(win,BROWN,(x1,y1),(x2,y2),w)
        # Changes the colour of the tree
        r = BROWN[0] + 20
        if r > 192:
            r = 192
        BROWN = (r,90,54)
        if w > 1:
            w -= 1
        # Randomly changes the length
        newLen = random.randint(length-20,length-5)
        # Randomizes the leaves and draws them if it is not on the first branches and if it is not winter
        chanceOfLeaf = random.uniform(0,1)
        if chanceOfLeaf >= .5 and y1 < y and not winter: 
            leaf(x1,y1,15,12,6)
        # Randomly changes the angle
        change = random.randint(5,10)
        # Draws two new branches
        tree(x2,y2,angle+math.pi/change,newLen,w,startCoords,y,winter)
        tree(x2,y2,angle-math.pi/change,newLen,w,startCoords,y,winter)
    else:
        # Changes the colour of the tree
        r = BROWN[0] - 20
        if r < 112:
            r = 112
        BROWN = (r,90,54)
        # Randomizes the leaf and draws it
        chanceOfLeaf = random.uniform(0,1)
        if chanceOfLeaf >= .5 and not winter:
            leaf(x1,y1,15,12,6)
            
#----------------------------------------#
# draws a leaf with the given parameters #
#----------------------------------------#
def leaf(x,y,w,h,num):
    if num > 0:
        i = random.randint(0,4)
        pygame.draw.ellipse(win,greens[i],(x,y,w,h))
        # Draws multiple leaves around the initial leaf
        leaf(x+(w/4),y,w,h,num-1)
        leaf(x+(w/4),y+(h/2),w,h,num-1)
        leaf(x+(w/2),y+(h/4),w,h,num-1)
        leaf(x-(w/4),y+(h/4),w,h,num-1)

#------------------------------------------#
# draws a flower with the given parameters #
#------------------------------------------#
def flower(x1,y1,r,num,angle,minR):
    global PINK
    if r > minR:
        # Determines the circumference of the circle
        c = int(math.pi * 2 * r)
        # Determines the width of the petals based on the circumference
        w = c // num
        # Draws a circle so there are no gaps in between the petals
        if angle == 0:
            pygame.draw.circle(win,PINK,(x1,y1),r)
        # Determines the angle to draw the flowers at
        angle += 360 / (num-w)
        # Creates new coordinates for the flower petals
        x2 = int(x1 + r * math.cos(math.radians(angle)))
        y2 = int(y1 + r * math.sin(math.radians(angle)))
        # Randomizes the width of the petals
        if w > 2:
            w = random.randint(w-2,w+2)
        pygame.draw.circle(win,PINK,(x2,y2),w)
        # Changes the colour of the petals with each row of petals
        if angle >= 360: 
            g = PINK[1] - 20
            if g < 0:
                g = 0
            b = PINK[2] - 20
            if b < 0:
                b = 0
            PINK = (255, g, b)
            r -= w
            angle = 0
        # Draws another row of petals
        flower(x1,y1,r,num,angle,minR)      
    else:
        # Draws the center of the flower
        pygame.draw.circle(win,PINK,(x1,y1),minR+2)

#------------------#
# draws the window #
#------------------#
def drawWin():
    global PINK
    global BROWN
    win.fill(BLUE)
    # Draws the main screen
    if isMainScreen:
        BROWN = (64, 58, 42)
        PINK = (255, 190, 220)
        # Draws the tree on the main screen
        tree(W/2,H-100,-math.pi/2.0,80,6,(W/2,300),0,False)
        x = 100
        # Draws multiple flowers with stems across the main screen 
        for plant in range(6):
            pygame.draw.line(win,greens[0],(x,H-125),(x,H-100))
            flower(x,H-125,10,20,0,4)
            PINK = (255, 190, 220)
            x += 100
        pygame.draw.rect(win,greens[0],(0,H-100,W,100))
        # Draws the tree page button
        trees.draw(win)
        treetxt.draw(win,trees.rect)
        # Draws the flower page button
        flowers.draw(win)
        flowertxt.draw(win,flowers.rect)
    # Draws the tree screen
    if isTreeScreen:
        BROWN = (64, 58, 42)
        # Draws the tree on the tree screen
        tree(W/2,H-100,-math.pi/2.0,80,6,(W/2,300),0,winter)
        # Changes the scene if it is winter or not
        if not winter:
            pygame.draw.rect(win,greens[0],(0,H-100,W,100))
        else:
            pygame.draw.rect(win,WHITE,(0,H-100,W,100))
        # Draws the redraw button
        redraw.draw(win)
        redrawtxt.draw(win,redraw.rect)
        # Draws the season button
        season.draw(win)
        seasontxt.draw(win,season.rect)
        # Draws the button to go to the main page
        back.draw(win)
        backtxt.draw(win,back.rect)
    # Draws the flower screen
    if isFlowerScreen:
        PINK = (255, 190, 220)
        # Changes the size of the flower based on the button that was clicked
        if size == 1:
            flower(350,250,150,50,0,20)
        elif size == 2:
            flower(350,250,100,40,0,14)
        else:
            flower(350,250,50,30,0,10)
        # Draws the button to go to the main page
        back.draw(win)
        backtxt.draw(win,back.rect)
        # Draws the buttons to change the size of the flower
        big.draw(win)
        bigtxt.draw(win,big.rect)
        med.draw(win)
        medtxt.draw(win,med.rect)
        small.draw(win)
        smalltxt.draw(win,small.rect)
    pygame.display.update()

#-----------------------#
# initializes variables #
#-----------------------#
# Initializes the window
win = pygame.display.set_mode((W,H))
# Initializes the buttons
trees = buttons.Button((75,H-75,50,40))
treetxt = buttons.Label('Tree')
flowers = buttons.Button((W-150,H-75,60,40))
flowertxt = buttons.Label('Flower')
redraw = buttons.Button((75,H-50,60,40))
redrawtxt = buttons.Label('Redraw')
season = buttons.Button((W-170,H-50,120,40))
seasontxt = buttons.Label('Change Season')
back = buttons.Button((325,H-50,50,40))
backtxt = buttons.Label('Back')
big = buttons.Button((115,25,50,40))
bigtxt = buttons.Label('Big')
med = buttons.Button((315,25,70,40))
medtxt = buttons.Label('Medium')
small = buttons.Button((515,25,50,40))
smalltxt = buttons.Label('Small')
# Initializes the screens
isMainScreen = True
isTreeScreen = False
isFlowerScreen = False

size = 1
inPlay = True
winter = False
drawWin()

# Main program loop
while inPlay:
    for event in pygame.event.get():
        # Allows the user to leave the program
        if event.type == pygame.QUIT:
            inPlay = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False
        # Checks if the mouse has been clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            if isMainScreen:
                # Checks if the tree button has been clicked and draws the tree screen
                if trees.collide(mousePos) != -1:
                    isMainScreen = False
                    isTreeScreen = True
                    drawWin()
                # Checks if the flower button has been clicked and draws the flower screen
                if flowers.collide(mousePos) != -1:
                    isMainScreen = False
                    isFlowerScreen = True
                    drawWin()
            if isTreeScreen:
                # Checks if the redraw button has been clicked and draws the tree screen again
                if redraw.collide(mousePos) != -1:
                    drawWin()
                if season.collide(mousePos) != -1:
                    winter = not winter
                    drawWin()
                # Checks if the back button has been clicked and draws the main screen
                if back.collide(mousePos) != -1:
                    isTreeScreen = False
                    isMainScreen = True
                    drawWin()
            if isFlowerScreen:
                # Checks if the 'big' button has been clicked and draws a bigger flower
                if big.collide(mousePos) != -1:
                    size = 1
                    drawWin()
                # Checks if the 'medium' button has been clicked and draws a medium sized flower
                if med.collide(mousePos) != -1:
                    size = 2
                    drawWin()
                # Checks if the 'small' button has been clicked and draws a smaller flower
                if small.collide(mousePos) != -1:
                    size = 3
                    drawWin()
                # Checks if the back button has been clicked and draws the main screen
                if back.collide(mousePos) != -1:
                    isFlowerScreen = False
                    isMainScreen = True
                    drawWin()
    

#---------------------------------------#                                        
pygame.quit()                           #
