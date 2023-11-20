import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # frequency: 50
pwm.start(0)


def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    GPIO.output(servo_pin, False)
    pwm.ChangeDutyCycle(0)


def rotate_until(target_angle):
    rotations = target_angle // 180
    for _ in range(int(rotations)):
        # 180도로 회전
        set_angle(180)
        time.sleep(1)

    # 남은 각도로 회전
    remaining_angle = target_angle % 180
    set_angle(remaining_angle)


if __name__ == "__main__":
    try:
        while True:
            dest = float(input("Enter angle (greater than 180): "))
            rotate_until(dest)

    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
