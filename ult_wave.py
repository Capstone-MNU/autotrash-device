import RPi.GPIO as GPIO
import time

# GPIO 핀 설정
TRIG = 23  # Trigger Pin
ECHO = 24  # Echo Pin

# GPIO 설정
GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_dist():
    # 초음파 발사 (10us 펄스)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # ECHO 핀으로 들어오는 펄스 시간 측정
    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    # 소리의 속도는 343m/s 이므로, 거리 = 속도 * 시간 / 2
    # 여기서 /2 는 왕복 시간이기 때문
    # cm 단위 결과를 위해 속도에 100을 곱함
    distance = (end - start) * (343 * 100) / 2

    return distance


if __name__ == "__main__":
    while True:
        print(f'Distance: {get_dist()}cm')
