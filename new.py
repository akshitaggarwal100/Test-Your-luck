import pygame
from random import randint, choice
from time import sleep
from math import ceil

pygame.init()
pygame.mixer.init()

# game window diemensions
width = 900
length = 900

gameWindow = pygame.display.set_mode((width,length))
pygame.display.set_caption("Test Your Luck")

# fonts
font = pygame.font.SysFont('Corbel', 35)
font2 = pygame.font.SysFont('Gotham', 55)
font3 = pygame.font.SysFont('Corbel', 15)
font4 = pygame.font.SysFont('Gotham', 70)
font5 = pygame.font.Font('HeadlinerNo.45 DEMO.ttf', 120)

# colors
white =  (241, 250, 238)
blue = (29, 53, 87)
red = (230, 57, 70)
green = (167, 201, 87)
pink = (255, 112, 150)

# function for loading image
def imgloader(image):
    img = pygame.image.load(f'{image}.png').convert_alpha()
    return pygame.transform.smoothscale(img, (500, 500))

# images
placeholder = pygame.image.load('placeholder.png')
trophy = pygame.image.load('trophy.png').convert_alpha()
trophy = pygame.transform.smoothscale(trophy, (40, 40))
gl = imgloader("gl")
gl1 = imgloader("gl1")
gl2 = imgloader("gl2")
# gl3 = imgloader("gl3") # very good score above 14
gl3 = pygame.image.load("gl3.png").convert_alpha()
gl3 = pygame.transform.smoothscale(gl3, (width, ceil(0.6997259335 * width)))
gl4 = imgloader("gl4")
gl5 = imgloader("gl5")
gli = [gl, gl1, gl2, gl4, gl5]
dl = imgloader("dl")
dl1 = imgloader("dl1")
dl2 = imgloader("dl2")
dl3 = imgloader("dl3")
dli = [dl, dl1, dl2, dl3]

# sounds
wbs = pygame.mixer.Sound("wbs.mp3")
start = pygame.mixer.Sound("start.mp3")
r1 = pygame.mixer.Sound("r1.mp3")
r2 = pygame.mixer.Sound("r2.mp3")
r3 = pygame.mixer.Sound("r3.mp3")
tpng = pygame.mixer.Sound("tpng.mp3")
bksp = pygame.mixer.Sound("bksp.mp3")
submit = pygame.mixer.Sound("submit.mp3")
b1 = pygame.mixer.Sound("laugh.mp3")
# b1 = pygame.mixer.Sound("go.mp3")
b2 = pygame.mixer.Sound("badscr.mp3")
# b2 = pygame.mixer.Sound("go1.mp3")
b3 = pygame.mixer.Sound("badscr1.mp3")
# b3 = pygame.mixer.Sound("go2.mp3")
bs = [b1, b2, b3]
g1 = pygame.mixer.Sound("gscr.mp3")
g2 = pygame.mixer.Sound("gscr1.mp3")
g3 = pygame.mixer.Sound("gscr2.mp3")
g4 = pygame.mixer.Sound("gscr3.mp3")
g5 = pygame.mixer.Sound("gscr4.mp3")
gs = [g1, g2, g3, g4, g5]

name = ""

# function for displaying text on gamewindow
def text_screen(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

# function for asking username
def username():
    global name
    menu = True
    start.play()
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.lower() == "akshit":
                    menu = False
                    name = "Grandmaster " + name

                elif event.key == pygame.K_RETURN:
                    submit.play()
                    menu = False

                elif event.key == pygame.K_BACKSPACE:
                    name = name[0:-1]
                    bksp.play()

                elif event.key != pygame.K_BACKSPACE:
                    name += event.unicode
                    tpng.play()

        gameWindow.fill(white)

        text_screen("test your luck".upper(), font5, red, width//2 - 242, 150)

        text_screen('Enter Name', font, blue, width//2 - 70, length//2 - 100)
        gameWindow.blit(placeholder, (width//2 - 190, length//2 - 70))
        text_screen(name, font, white, width//2 - 170, length//2 - 40)

        pygame.display.update()

    return rules(name)

# function for displaying rules
def rules(name):
    score = 0
    disp = True
    if name == "Grandmaster akshit":
        wbs.play()

    while disp:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    r1.play()
                    disp = False
        
        gameWindow.fill(white)

        text_screen(f"Username: {name}", font, blue, 30, 30)

        gameWindow.blit(trophy, [width - 120, 20])
        text_screen(str(score), font2, blue, width - 60, 23)

        if name == "Grandmaster akshit":

            text_screen("You made the rules Grandmaster", font2, blue, width//2 - 300, 400)
            text_screen("Rules don't apply to You Sir", font2, blue, width//2 - 250, 500)

        else:
            text_screen("Instructions to play:-", font2, blue, 30, 100)
            text_screen("-> The computer will choose a number between 1-10 (3 times)", font, blue, 30, 160)
            text_screen("-> Suppose, the number is 4", font, blue, 30, 205)
            text_screen("-> So, you will be given 4 number of chances to guess it", font, blue, 30, 250)
            text_screen("-> If you guess the number correctly then,", font, blue, 30, 295)
            text_screen("-> The no. of left chances left will be added to your score", font, blue, 30, 340)
            text_screen("-> Don't press ENTER until you want to submit your guess", font, blue, 30, 385)
            text_screen("press spacebar to play".upper(), font2, blue, width//2 - 255, 600)

        pygame.display.update()

    return playgame(name)

# function for playing game
def playgame(name):
    score = 0
    playing = True
    round = 1
    chance = 1
    guess = -1
    temp = ""
    message = ""

    while playing:
        while round <= 3:
            number = randint(0, 10)
            # number = 9
            while chance <= number:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            if len(temp) == 0 or int(temp) < 1 or int(temp) > 10:
                                message = "Enter a number from 1-10"
                            else:
                                submit.play()
                                guess = int(temp)
                                if number != guess and chance == number and round == 3:
                                    choice(bs).play()
                                    message = f"The correct number was {number}"
                                    chance = number + 1
                                    round += 1
                                    playing = False
                                    sleep(3)
                                    break

                                elif number == guess and round == 3:
                                    score += number - chance
                                    choice(gs).play()
                                    message = "You guessed the number"
                                    chance = number + 1
                                    round += 1
                                    playing = False
                                    sleep(1)
                                    break

                                elif number != guess and chance == number:
                                    choice(bs).play()
                                    message = f"The correct number was {number}"
                                    round += 1
                                    sleep(3)

                                elif number < guess:
                                    message = f"Correct number is smaller than {guess}"

                                elif number > guess:
                                    message = f"Correct number is greater than {guess}"

                                elif number == guess:
                                    choice(gs).play()
                                    message = "You guessed the number"
                                    score += number - chance
                                    round += 1
                                    chance = number + 1
                                    sleep(1)
                                    break

                                chance += 1

                        elif event.key == pygame.K_BACKSPACE:
                            temp = temp[:-1]
                            bksp.play()

                        elif event.unicode in [str(x) for x in range(0, 10)]:
                            temp += event.unicode
                            tpng.play()


                gameWindow.fill(white)

                text_screen(f"Username: {name}", font, blue, 30, 30)

                gameWindow.blit(trophy, [width - 120, 20])
                text_screen(str(score), font2, blue, width - 60, 23)

                if name == "Grandmaster akshit":
                    text_screen(str(number), font3, blue, 0, 0)

                text_screen(f"ROUND {round}" if round <= 3 else f"ROUND {round - 1}", font2, red, width//2 - 65, 200)

                text_screen('Enter Number', font, blue, width//2 - 87, length//2 - 100)
                gameWindow.blit(placeholder, (width//2 - 190, length//2 - 70))
                text_screen(temp, font, white, width//2 - 170, length//2 - 40)

                if len(message) > 25:
                    text_screen(message, font2, red, width//2 - 290, 600)
                else:
                    text_screen(message, font2, red, width//2 - 215, 600)

                pygame.display.update()

            if round == 2:
                r2.play()
            elif round == 3:
                r3.play()
            chance = 1
            temp = ""

    return result(name, score)

# function for showing the final score and remarks accordingly
def result(name, score):
    review = True
    if score <= 5:
        choice(bs).play()
        img = choice(dli)
    elif score > 5:
        choice(gs).play()
        img = choice(gli)
        if score > 14:
            img = gl3
    while review:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    r1.play()
                    review = False

            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameWindow.fill(white)

        if score < 15:
            text_screen(f"Username: {name}", font2, blue, width//2 - 175 if len(name) < 18 else width//2 - 285, 100)
            text_screen(f"Luck Score: {score}", font2, red if score <= 5 else green, width//2 - 130, 200)    
        else:
            text_screen(f"Username: {name}", font2, blue, width//2 - 175 if len(name) < 18 else width//2 - 285, 50)
            text_screen(f"Luck Score: {score}", font2, red if score <= 5 else green, width//2 - 130, 150)

        gameWindow.blit(img, [width//2 - 250, 275] if score < 15 else [0, length - ceil(0.6997259335 * width)])

        if score > 14:
            text_screen("You are Immortal", font4, pink, width//2 - 200, 250)

        if score < 15:
            text_screen("Press SPACEBAR to play again", font2, green, width//2 - 280, 800)

        pygame.display.update()

    return playgame(name)


username()