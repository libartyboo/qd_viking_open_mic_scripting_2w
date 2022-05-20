import random
import time
from halo import Halo
from datetime import datetime
from colorama import init, Fore, Style

participants = {899: "Test_1",
                912: "Test_2",
                935: "Test_3",
                29: "Test_4",
                84: "Test_5",
                152: "Test_6",
                362: "Test_7",
                704: "Test_8",
                720: "Test_9"}


def file_name():
    today = datetime.today()
    date_marker = today.strftime("%Y%m%d_%H%M%S")
    return f"log_{date_marker}.txt"


log_file = file_name()


@Halo(spinner='dots')
def select_winner():
    i = 0
    winner = False
    while not winner:
        for key in participants.keys():
            ran = get_random_num()
            if winner:
                break
            elif key == ran:
                winner = True
                return participants.get(key), ran
            else:
                execute_log(log_file, f"attempt#{i} - [{ran}]\n")
                i += 1
                continue


def get_random_num():
    return random.randint(1, 1000)


def execute_log(file, text):
    file = open(file, "a+")
    file.write(text)
    file.close()
    time.sleep(0.00001)


if __name__ == '__main__':
    winner = select_winner()
    init()
    print(Fore.BLUE + Style.BRIGHT + f"WINNER: {winner[0]} [{winner[1]}]")
