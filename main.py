from ult_wave import get_dist
from motor import rotate_pillar, rotate_plate
from time import sleep
import subprocess
import requests
import os

cls = -1

server_url = 'http://172.30.1.51:80/detect'
capture_interval = 1

def measure_capacity():
    """
    measure capacity for each trash can
    :return:
    """


if __name__ == "__main__":
    while True:
        image_path = 'image.jpg'
        subprocess.call(['fswebcam', image_path])

        with open(image_path, 'rb') as image_file:
            response = requests.post(server_url, files={'image': image_file})

        print(response.text)
        os.remove(image_path)

        time.sleep(capture_interval)
