import requests
from time import sleep

server_url = 'http://172.30.1.51:80/test'

if __name__ == "__main__":
    while True:
        # 이미지 파일 열기
        response = requests.post(server_url)

        print(response.text)

        sleep(1)