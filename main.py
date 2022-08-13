import random

# rules
print("you are given the correct number of chances")
print("suppose correct number is 1 so you will be given 1 chance only")
print("number will be between 1-10")
print("there will be three rounds")
print("the number of guesses left in each round, if you guess the number, will be added to your luck score")


score = 0
for i in range(3):
    number = random.randint(1,10)
    print(number)
    for i in range(1,(number+1)):
        guess = int(input("\nguess the number:"))
        if guess==number:
            print("you won!")
            print("guesses taken:",(i))
            score += number - i
            break

        elif guess != number and i == number:
            print("game over")
            print("guess left:0")

        elif guess>number:
            print("correct number is smaller than",guess)

        elif guess<number:
            print("correct number is greater than",guess)

print("\nyour luck score for today: ",score)