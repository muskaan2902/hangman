import random
words=["muskaan", "abhay", "umesh", "amruta","isha", "avick", "rakshit","nidharshana","yash"]
word=random.choice(words)

total_chances=5
guessed="-"*len(word)
while total_chances!=0:
    
    print(guessed)
    letter=input("enter a letter: ").upper()

    if letter in word:
      for i in range(len(word)):
        if word[i]==letter:
            #change the dash into the letter
            guessed=guessed[:i]+letter+guessed[i+1:]
            break
            print(guessed)
    if guessed==word:
        print("congo u won")
                                   
else:
    total_chances-=1
    print("incorrect guess")
    
print("GAME OVER")
        
            