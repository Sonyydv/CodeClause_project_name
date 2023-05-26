import string
import random
length=int (input("Enter the length of password: "))
print('''Choose the characters set for password from the following : 
      1.Digits
      2.Letters
      3.Special characters
      4.Exit''')
character_list= " "
flag=True
while flag:
    choice=int(input("Enter the choices: "))
    if(choice==1):
     character_list += string.ascii_letters
    elif(choice==2):
     character_list += string.digits
    elif(choice==3):
     character_list += string.punctuation
    elif(choice==4):
     break
    else:
     print("Please pick a valid choice !")
password= []
for i in range(length):
    randomchar = random.choice(character_list)
    password.append(randomchar)
print("The random password is " + "".join(password))
