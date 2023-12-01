import requests
from time import sleep

server_url = 'https://0411-119-200-89-54.ngrok-free.app'

def send_image(image_file):
    return requests.post(server_url + '/detect', files={'image': image_file})

def save_dist(dist, cls):
    return requests.get(server_url + '/ultwave', params={'dist': dist, 'cls': cls})

def ask_ecop():
    return requests.get(server_url + '/ecop')
    

if __name__ == "__main__":
    for _ in range(10):
        print("wait . . .")
        response = requests.get(server_url)
        
        print(response.text)
        
        sleep(1)
