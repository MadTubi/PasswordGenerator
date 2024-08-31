# #Password Generator:

# Description: Develop a program that generates random, secure passwords of complexity.
# Skills: String manipulation, random number generation.

import random as rand

def createPassword(sNum,eNum,word):

    fPartWord = word[:len(word)//2]#divide the word in half
    sPartWord = word[len(word)//2:]#seocnd part of half word
    newFPart = fPartWord[::-1]#get the half word reversed

    number = rand.randint(sNum,eNum)
    number = str(number)
    Password = newFPart + number + sPartWord
    newPassword = Password.replace("e","3")

    print(newPassword)
  

def main():
    print("-Welcome to the Password Generator-\n")

    startNum = int(input("Enter the starting number to pick a random number: "))
    endNum = int(input("Enter the ending number to pick a random number: "))
    word = input("Enter a word to form a password: ")

    #call method
    createPassword(startNum,endNum,word)
    

main()