from ult_wave import get_dist
from motor import rotate
from time import sleep
import subprocess
import requests
import os

classes = [
    'can',
    'glass',
    'plastic',
    'pet_clean',
    'pet_label'
]

cls = -1

server_url = 'https://ce13-119-200-89-54.ngrok-free.app/detect'
capture_interval = 1

def measure_capacity():
    """
    measure capacity for each trash can
    :return:
    """


if __name__ == "__main__":
    while True:
        image_path = 'image.jpg'
        subprocess.call(['fswebcam', '-r', '640x640', '--no-banner', image_path])

        with open(image_path, 'rb') as image_file:
            response = requests.post(server_url, files={'image': image_file})

        print(response.text)
        
        cls = response.text
        if len(cls):
            rotate(cls)

        os.remove(image_path)

        sleep(capture_interval)
        
