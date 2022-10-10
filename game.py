import random

print("-----------------------------WELCOME TO WORD GUESS GAME-----------------------------")
name = input("Enter your name : ")
print("Hello !",name)

words = ["Microsoft","Meta","Facebook","Byjus","Dell","Amazon",
         "Apple","Netflix","Google","Accenture","Spotify","Visa",
         "Mastercard","Capgemini","Bosch","Cognizant","Samsung",
         "Civo","Wipro","Redington","Thoughtworks","Juspay","Paypal",
         "PhonePe","Freshworks","Jio"]
word = random.choice(words)

print("THE WORD IS ")
for i in range(0,len(word),1):
    print("_",end = " ")

print(" ")
print("\nSTART GUESSING")
turns = 5

storeword = ""
wordlength = len(word)

turns = 3
while(turns > 0):
    storeword = ""
    while(wordlength > 0):
        print("\n")
        ch = input("GUESS THE CHARACTER :")
        storeword = storeword + ch
        if(ch not in word):
            print("WRONG GUESS")
            if(turns > 1):
                print("ONE MORE CHANCE !")
            else:
                print("GAME FINISHED")
                print("NO MORE CHANCE !")    
            break
        else:
            for i in storeword:
                print(i,end = " ")
            for i in range(len(storeword),len(word),1):
                print("_",end = " ")    
            if(len(storeword) == len(word) and storeword == word):
                print("\n\nTHE WORD IS : ",word)
                print("CONGRATULATIONS ",name)
                print("WOHOO ! \nYOU GUESSED THE WORD CORRECTLY \n")
                print("GAME FINISHED")

        wordlength -= 1       
    turns -= 1    

        



