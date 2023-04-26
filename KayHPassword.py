import string
import random
from colorama import Fore
print (Fore.CYAN, """

    __ __               __  __   ____                                          __
   / //_/___ ___  __   / / / /  / __ \____ ____________      ______  _________/ /
  / ,< / __ `/ / / /  / /_/ /  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
 / /| / /_/ / /_/ /  / __  /  / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
/_/ |_\__,_/\__, /  /_/ /_/  /_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/   coded by KayH GNG
           /____/                                                                

""")
# Getting password length
length = int(input("Enter password length: "))
 
print('''Choose character set for password from these :
         1. Digits
         2. Letters
         3. Special characters
         4. Show''')
 
characterList = ""
 

while(True):
    choice = int(input("Choose one of these: "))
    if(choice == 1):
         
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif(choice == 2):
         
        # Adding digits to possible characters
        characterList += string.digits
    elif(choice == 3):
         
        # Adding special characters to possible
        # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    # Picking a random character from our
    # character list
    randomchar = random.choice(characterList)
     
    # appending a random character to password
    password.append(randomchar)
 

print("Generated Password is " + "".join(password))