# 1. Magic 8 ball
# A program that should work like a magic 8 ball. The program should ask the user a yes/no question and then print a random answer.

# Requires use of the random module
# Requires use of the input function
# Requires use of list


#-------------------------------------------------------------------------------#

import random
# https://docs.python.org/3/library/random.html

class Magic8Ball:
    def __init__(self):
        self.answers = ["It is certain", "It is decidedly so", "Without a doubt", 
                        "Yes – definitely", "You may rely on it", "As I see it, yes", 
                        "Most likely", "Outlook good", "Yes", "Signs point to yes", 
                        "Reply hazy, try again", "Ask again later", "Better not tell you now", 
                        "Cannot predict now", "Concentrate and ask again", "Don't count on it", 
                        "My reply is no", "My sources say no", "Outlook not so good", 
                        "Very doubtful"]

    def ask_question(self):
        question = input("What is your yes/no question? ")
        print(random.choice(self.answers))

magic8ball = Magic8Ball()
magic8ball.ask_question()