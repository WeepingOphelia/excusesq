import requests
import time
from excuse import *
from libber import *
# from god import *

user = ("Gwynnhwyfar", "Captain")

def main():
    # excuse = get_excuse()
    # print(excuse)
    test_excuse = DefaultExcuse()
    print(adlibber(test_excuse))
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

# greeting()
main()