## guess
This project is a game called Guess that I made just for fun. In the game, you guess numbers that are randomly generated by the program. The closer your guesses are to the correct answer, the higher your score. The objective is to accumulate as many points as possible before running out of lives.

## How to play

Go to http://guessgame.pythonanywhere.com to play.

Here are the rules for the game. The rules are also provided on the website's home page.
* Each round, the computer will generate a random number between 1 and 30, and you have to predict what that number is. Enter your prediction into the text box and click "Guess".
* After each guess, the closer your guess is to the answer, the more your score increases. To determine how much your score increases, the game will calculate the difference between your guess and the randomly generated number. Let's call this difference the Offset. Now subtract the Offset from 30. Your score will increase by the number that results from this subtraction.
    * For example, if you guess 25 but the correct answer is 17, the Offset will be 25 - 17 = 8. Your score will increase by 22, since 30 - 8 = 22.
* At the beginning of the game, you get a total of 10 lives. You lose one each time your guess is off by 8 or more from the correct answer. You gain a life each time your answer is off by 2 or less from the answer. This means that yes, it is possible to have more than 10 lives at certain points in the game.
* The game ends when you run out of lives.

## Tech used
* Built with Django
