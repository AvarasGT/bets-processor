#importing create_bet method
from client_emul.create_bet import generate_bet

#importing Sleep method from Time Lib
from time import sleep

# importing datetime
import random

from datetime import datetime

# importing pytz module
import pytz

def get_current_time():
    # giving the format of datetime
    format = "%H:%M:%S"
    # getting the Moskow timezone
    timezone = pytz.timezone('Europe/Moscow')
    # Getting the current time in Moskow
    datetime_object = datetime.now(timezone)
    # Format the above datetime using the strftime()
    return datetime_object.strftime(format)

# getting how many bets are there in the current hour and day
def predict_bets(current_time = get_current_time()):
    date_index = (datetime.now(pytz.timezone('Europe/Moscow')).weekday())
    if '00:00:00' < current_time <= '10:00:00':
        lowest_counter = 25
        biggest_counter = 50
        if date_index == 5 or date_index == 6:
            lowest_counter *= 2
            biggest_counter *= 2
        else:
            pass
    elif '10:00:00' < current_time <= '17:00:00':
        lowest_counter = 40
        biggest_counter = 75
        if date_index == 5 or date_index == 6:
            lowest_counter *= 2
            biggest_counter *= 2
    elif '17:00:00' < current_time <= '20:00:00':
        lowest_counter = 70
        biggest_counter = 100
        if date_index == 5 or date_index == 6:
            lowest_counter *= 2
            biggest_counter *= 2
    elif '20:00:00' < current_time <= '24:00:00':
        lowest_counter = 135
        biggest_counter = 200
        if date_index == 5 or date_index == 6:
            lowest_counter *= 2
            biggest_counter *= 2
    bets_number = random.randint(lowest_counter,biggest_counter)
    return bets_number


def make_bet(bets_number=predict_bets()):
    seconds_in_hour = 60 #3600
    pause_time = seconds_in_hour // bets_number
    # потом удалить все что связано со временем
    format = "%H:%M:%S"
    timezone = pytz.timezone('Europe/Moscow')
    datetime_object = datetime.now(timezone)
    with open('betLog.txt', 'a') as f:
        f.write('Start time: ' + str(datetime_object.strftime(format)) + '\n')
    for bet in range(bets_number):
        print (generate_bet())
        with open('betLog2.txt', 'a') as f:
            f.write(str(bet) + ' ' + str(generate_bet()) + '\n')
        sleep(pause_time)
    with open('betLog.txt', 'a') as f:
        f.write('End time: ' + str(datetime_object.strftime(format)) + '\n')

if __name__ == "__main__":
    make_bet()

