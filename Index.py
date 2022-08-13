import pygame
from random import randint

pygame.init()
pygame.mixer.init()

width = 900
length = 900

gameWindow = pygame.display.set_mode((width,length))
pygame.display.set_caption("what's your luck")

# fonts
font = pygame.font.SysFont('Corbel', 35)
font2 = pygame.font.SysFont('Gotham', 55)
# devil = pygame.image.load('devil.png').convert_alpha()
# devil = pygame.transform.smoothscale(devil,(900, 900))

# girl = pygame.image.load('devil2.png').convert_alpha()
# girl = pygame.transform.smoothscale(girl,(900, 900))
# pygame.mixer.music.load("hd.mp3")

# robot = pygame.image.load('robot.png').convert_alpha()
# robot = pygame.transform.smoothscale(robot,(441, 510))

# images
placeholder = pygame.image.load('placeholder.png')
trophy = pygame.image.load('trophy.png').convert_alpha()
trophy = pygame.transform.smoothscale(trophy, (40, 40))

# sounds
wbs = pygame.mixer.Sound("wbs.mp3")

# colors
red = (217, 4, 41)
white =  (241, 250, 238)
blue = (29, 53, 87)

score = 0
name = "$"

startGame = False
menu = True
play = False

def text_screen(text, font, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def startScreen():
    global startGame,menu,name
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and name.lower() == "$akshit":
                    menu = False
                    startGame = True
                    name = "Grandmaster " + name[1:]
                    wbs.play()
                    rulescreen()
                elif event.key == pygame.K_RETURN:
                    menu = False
                    startGame = True
                    name = name[1:]
                    rulescreen()
                elif event.key == pygame.K_BACKSPACE and len(name) != 1:
                    name = name[0:-1]
                elif event.key != pygame.K_BACKSPACE:
                    name += event.unicode

        gameWindow.fill(white)
        text_screen('Enter Name', font, blue, width//2 - 75, length//2 - 100)
        gameWindow.blit(placeholder, (width//2 - 190, length//2 - 70))
        text_screen(name, font, white, width//2 - 170, length//2 - 40)
        pygame.display.update()

def rulescreen():
    global name, startGame, play
    while startGame:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # pass
                    startGame = False
                    play = True
                    gamescreen(name)
            elif event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameWindow.fill(white)
        text_screen(f"Username: {name}", font, blue, 30, 30)
        gameWindow.blit(trophy, [width - 120, 20])
        text_screen(str(score), font2, blue, width - 60, 23)

        # displaying the instructions
        text_screen("instructions to play:-", font2, blue, 30, 100)
        text_screen("-> the computer will choose a number between 1-10 (3 times)", font, blue, 30, 160)
        text_screen("-> suppose, the number is 4", font, blue, 30, 205)
        text_screen("-> So, you will be given 4 number of chances to guess it", font, blue, 30, 250)
        text_screen("-> if you guess the number correctly then,", font, blue, 30, 295)
        text_screen("-> the no. of left chances left will be added to your score", font, blue, 30, 340)
        text_screen("press spacebar to play".upper(), font2, blue, width//2 - 255, 600)
        pygame.display.update()
        # if name == "$Akshit":
        #     for event in pygame.event.get():
        #         pygame.mixer.music.play(0)
        #         gameWindow.fill(red)
        #         gameWindow.blit(girl, (0, 100))
        #         pygame.display.update()
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
        # elif name.lower() == "$akshit":
        #     for event in pygame.event.get():
        #         gameWindow.fill(white)
        #         gameWindow.blit(robot, (width//2 - 220, length//2 - 90))
        #         pygame.display.update()
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
        # else:
        #     for event in pygame.event.get():
        #         gameWindow.fill(red)
        #         gameWindow.blit(devil, (0, 0))
        #         pygame.display.update()
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             quit()
def gamescreen(name):
    global score, startGame
    guess = -1
    temp = "0"
    while play:
        for round in range(1, 4):
            gameWindow.fill(white)
            text_screen(f"Username: {name}", font, blue, 30, 30)
            gameWindow.blit(trophy, [width - 120, 20])
            text_screen(str(score), font2, blue, width - 60, 23)
            text_screen('Enter Number', font, blue, width//2 - 90, length//2 - 100)
            gameWindow.blit(placeholder, (width//2 - 190, length//2 - 70))
            number = randint(1, 10)
            for gs in range(1, number + 1):
                text_screen(temp, font, white, width//2 - 170, length//2 - 40)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            guess = int(temp)
                            if guess == number:
                                score += number - gs
                                break
                            elif number < guess:
                                text_screen(f"correct number is smaller than {guess}", font, blue, width//2 - 100, length//2 + 50)
                                break
                            elif number > guess:
                                text_screen(f"correct number is greater than {guess}", font, blue, width//2 - 100, length//2 + 50)
                                break
                        elif event.key == pygame.K_BACKSPACE:
                            temp = temp[0:-1]
                        else:
                            temp += event.unicode
                    elif event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    pygame.display.update()
        

    # if name.lower() == "$akshit":
        
startScreen()