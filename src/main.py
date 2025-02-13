import requests
import time
from excuse import *
from libber import *
# from god import *

user = ("Gwynnhwyfar", "Captain")
affirm = ["y", "yes"]
deny = ["n", "no"]

def main():
    user_input = input("Would you like an excuse? [Y/N]: ")
    if user_input.lower() in affirm:     
        test_excuse = DefaultExcuse()
        print("My sincere apologies,") 
        print(adlibber(test_excuse))
        main()
    if user_input.lower() in deny:
        quit()
    else:
        print("Invalid command")
        main()
    return

def greeting():
    # user = (input("Your preferred name: "), input("Your preferred address (eg Sir, Madam, Consulate, Emir): "))

    cur_time = time.localtime()
    hr = cur_time.tm_hour
    if 1 < hr < 12:
        tod = "morning"
    if 11 < hr < 17:
        tod = "afternoon"
    if hr <2 or hr > 16:
        tod = "evening"
    
    print(f"Good {tod}, {user[1]} {user[0]}")
    print(time.strftime("The time is: %H%M", cur_time))

greeting()
main()