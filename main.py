from ult_wave import get_dist
from motor import rotate_pillar, rotate_plate
from time import sleep
import schedule
import datetime

framerate = 60
cls = -1


def measure_capacity():
    """
    measure capacity for each trash can
    :return:
    """

schedule.every().monday.do(measure_capacity)

if __name__ == "__main__":
    while cls < 0:
        print(f'detecting trash . . . ')
        # take a picture
        # send picture to server
        # get predict from DB
        cls = get_cls()

    while cls >= 0:
        rotate_pillar(cls)
        sleep(1)
        rotate_plate()
        sleep(1)
        print(f'detected dist:{get_dist()}')

    while True:
        schedule.run_pending()
        sleep(1)