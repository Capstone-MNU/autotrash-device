import requests
from time import sleep

server_url = 'https://7d49-119-200-89-54.ngrok-free.app'

if __name__ == "__main__":
    for _ in range(10):
        print("wait . . .")
        response = requests.get(server_url)
        
        print(response.text)
        

        sleep(1)
