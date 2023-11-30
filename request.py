import requests
from time import sleep

server_url = 'https://7d49-119-200-89-54.ngrok-free.app'

def send_image(image_file):
    return requests.post(server_url + '/detect', files={'image': image_file})

def save_dist(dist):
    requests.get(server_url + '/ultwave', dist={'dist': dist})

def ask_ecop():
    requests.get(server_url + '/ecop', dist={'dist': dist})
    

if __name__ == "__main__":
    for _ in range(10):
        print("wait . . .")
        response = requests.get(server_url)
        
        print(response.text)
        
        sleep(1)
