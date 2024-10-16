import mysql.connector
import random
from collections import Counter
import datetime
connection = mysql.connector.connect(
    host = "localhost",  # Replace with your MySQL server host
    user =  "Your Username",  # Replace with your MySQL username
    password =  "Your Password",  # Replace with your MySQL password
    database =  "hangman"  # Replace with your MySQL database name)
    )
win = 0
loss = 0


someWords = '''france italy china cuba mexico india bangladesh indonesia kuwait iran iraq '''


someWords = someWords.split()
word = random.choice(someWords)
import datetime



current_datetime = datetime.datetime.now()


sql_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
name = input("Enter your name : ")




if __name__ == '__main__':
    print('Guess the word! HINT: The word is the name of country')


    for _ in word:
        print('_', end=' ')
    print()


    playing = True
    letterGuessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
            print("The number of guesses left : ",chances+1)


            try:
                guess = input('Enter a letter to guess: ')
            except:
                print('Enter only a letter!')
                continue


            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            if len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            if guess in letterGuessed:
                print('You have already guessed that letter')
                continue


            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess


            for char in word:
                if char in letterGuessed:
                    print(char, end=' ')
                    correct += 1
                else:
                    print('_', end=' ')


            if Counter(letterGuessed) == Counter(word):
                print('\nThe word is:', word)
                flag = 1
                win += 1
                print('Congratulations, You won!')
                insert = "INSERT INTO score(time,name,win,loss) VALUES(%s,%s,%s,%s)"
                val = (sql_datetime,name,win,loss)
                mydb = connection.cursor()
                mydb.execute(insert, val)
                connection.commit()
                break


        if chances <= 0 and Counter(letterGuessed) != Counter(word):
            loss += 1
            insert = "INSERT INTO score(time,name,win,loss) VALUES(%s,%s,%s,%s)"
            val = (sql_datetime,name,win,loss)
            mydb = connection.cursor()
            mydb.execute(insert,val)
            connection.commit()
            print()
            print('You lost! Try again..')
            print('The word was', word)


    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
