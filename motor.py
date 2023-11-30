from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import AngularServo
from time import sleep

pigpio_factory = PiGPIOFactory()

servo_pin_pillar = 13
servo_pillar = AngularServo(servo_pin_pillar, pin_factory=pigpio_factory, min_angle=-90, max_angle=90)
servo_pillar.angle = 0
sleep(3)
servo_pin_plate = 12
servo_plate = AngularServo(servo_pin_plate, pin_factory=pigpio_factory, min_angle=-90, max_angle=90)
servo_plate.angle = 0
sleep(3)

def rotate_pillar(cls, switch):
    """
    rotate pillar by class of trash
    :param cls: detected class of trash
    :param switch: direction of rotate, 1 = clockwise, -1 = counterclockwise
    :return:
    """
    if cls == 0:
        angle = 0
    elif cls == 1:
        angle = 90
    elif cls == 2:
        angle = 90  # 2번회전
    elif cls == 3:
        angle = -90
    
    servo_pillar.angle = angle
    sleep(1)


def rotate_plate():
    """
    #servo_plate.angle = 0
    rotate plate for drop trash
    :return:
    """
    servo_plate.angle = 45
    sleep(1)
    servo_plate.angle = -45


# 서보 모터 작동 테스트(python motor.py로 실행)
if __name__ == "__main__":
    print("rotate pillar1")
    servo_pillar.angle = 90
    sleep(3)
    print("rotate pillar2")
    servo_pillar.angle = -90
    sleep(3)
    print("rotate plate1")
    servo_plate.angle = 90
    sleep(3)
    print("rotate plate2")
    servo_plate.angle = -90
    sleep(3)
