import requests
import time
from excuse import *
from libber import *
# from god import *

user = ("Gwynnhwyfar", "Captain")
test = ["t", "test"]
affirm = ["y", "yes"]
deny = ["n", "no"]

def main():
    user_input = input("Would you like an excuse? [Y/N]: ")
    if user_input.lower() in affirm:
        get_excuse()
    if user_input.lower() in deny:
        quit()
    if user_input.lower() in test:
        get_excuse_test()
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

def get_excuse_test():
    test_excuse = DefaultExcuse()
    print("My sincere apologies,") 
    print(dadlibber(test_excuse))
    main()

def get_excuse():
    excuse = Excuse()
    print("My sincere apologies,") 
    print(chadlibber(excuse))
    main()


greeting()
main()