import RPi.GPIO as GPIO
import time

servo_pin = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)  # 0.6ms


def rotate_plate():
    pwm.ChangeDutyCycle(7.5)  # 7.5 is the duty cycle for 45°
    time.sleep(1)
    pwm.ChangeDutyCycle(2.5)  # 2.5 is the duty cycle for 0°


if __name__ == "__main__":
    try:
        while True:
            print("Rotate: Plate")
            rotate_plate()
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        pwm.stop()
        GPIO.cleanup()
