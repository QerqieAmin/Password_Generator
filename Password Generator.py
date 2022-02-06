import random2
import termcolor 
from pyfiglet import figlet_format


def PasswordGeneator() :
    print(termcolor.colored(figlet_format("Welcome to Password Genator") , "green"))
    charname = ["a","b","c","d","e","f","g","h","i","j",
                "k","l","m","n","o","p","q","r",
                "s","t","u","v","w","x","y","z","A","B"
                ,"C","D","E","F","G","H","I","J","K","L",
                "M","N","O","P","Q","R","S","T","U","W","V","X","Y"
                ,"Z","1","2","3","4","5","6","7","8","9","0" , "#" , "@" , "!"]
    letter = ""
    password = ""
    while True :
        if len(password) == 16 :
            break
        else :
            letter = random2.choice(charname)
            password += letter
            letter = ""
    print(termcolor.colored("Your Password " , "blue") , termcolor.colored(": " , "yellow") , termcolor.colored(password , "green"))
    

    
    
PasswordGeneator()