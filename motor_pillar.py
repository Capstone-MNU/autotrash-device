import RPi.GPIO as GPIO
import time

servo_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)
pwm.start(2.5)  # 0.6ms



if __name__ == "__main__":
    try:
        while True:
            print("Rotate: Pillar")
            rotate_plate()
            time.sleep(0.5)

    except KeyboardInterrupt:
        print("Measurement stopped by user")
        pwm.stop()
        GPIO.cleanup()
