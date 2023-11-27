from gpiozero import Servo
from time import sleep

servo_pin_pillar = 18
servo_pillar = Servo(servo_pin_pillar)

servo_pin_plate = 17
servo_plate = Servo(servo_pin_plate)


def rotate_pillar(cls):
    """
    rotate pillar by class of trash
    :param cls: detected class of trash
    :return:
    """
    angle = cls * 90
    servo_pillar.angle = angle
    sleep(1)


def rotate_plate():
    """
    rotate plate for drop trash
    :return:
    """
    servo_plate.angle = 45
    sleep(1)


# 서보 모터 작동 테스트(python motor.py로 실행)
if __name__ == "__main__":
    servo_pillar.angle = -90
    sleep(1)
    servo_pillar.angle = -45
    sleep(1)
    servo_pillar.angle = 0
    sleep(1)
    servo_pillar.angle = 45
    sleep(1)
    servo_pillar.angle = 90
    sleep(1)

    servo_plate.angle = -90
    sleep(1)
    servo_plate.angle = -45
    sleep(1)
    servo_plate.angle = 0
    sleep(1)
    servo_plate.angle = 45
    sleep(1)
    servo_plate.angle = 90
    sleep(1)
