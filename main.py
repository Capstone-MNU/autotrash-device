from ult_wave import get_dist
from motor import rotate
from time import sleep
import subprocess
import request
import os

classes = [
    'can',
    'glass',
    'plastic',
    'pet_clean'
    # 'pet_label'
]

cls = -1

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
            response = request.send_image()

        print(response.text)
        
        cls = response.text
        if cls in classes:
            rotate(cls)
            request.ask_ecop()
            

        os.remove(image_path)

        sleep(capture_interval)
        
