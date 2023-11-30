import pigpio

from time import sleep


pi = pigpio.pi() 
pin_plate = 12
pin_pillar = 13

deg_0 = 660 # position anti-clockwise
deg_90 = 1500 # middle
deg_180 = 2340 # position clockwise

    
def rotate(cls):
    rotate_pillar(cls)
    rotate_plate() 

def deg_to_pw(deg):
    return 600 + 10 * deg
    
def rotate_pillar(cls):
    
    pi.set_servo_pulsewidth(pin_pillar, deg_0)
    sleep(1)
    
    if cls == 'can':
        return
    elif cls == 'glass':
        pi.set_servo_pulsewidth(pin_pillar, deg_90)
        sleep(1)
        pi.set_servo_pulsewidth(pin_pillar, deg_0)
        sleep(1)
        
    elif cls == 'plastic':
        pi.set_servo_pulsewidth(pin_pillar, deg_180)
        sleep(1)
        pi.set_servo_pulsewidth(pin_pillar, deg_0)
        sleep(1)
    elif cls == 'pet_clean':
        pi.set_servo_pulsewidth(pin_pillar, deg_90)
        sleep(1)
        
    else:
        print("no trash to rotate")
    
def rotate_plate():
    pi.set_servo_pulsewidth(pin_pillar, deg_90)
    sleep(1)
    pi.set_servo_pulsewidth(pin_pillar, deg_0)
    sleep(1)




if __name__ == '__main__':
    while True:
        # pi.set_servo_pulsewidth(pin_plate, deg_0) # position anti-clockwise
        # sleep(1)
        # pi.set_servo_pulsewidth(pin_pillar, deg_0) # position anti-clockwise
        # sleep(1)
        
        pi.set_servo_pulsewidth(pin_plate, deg_90) # middle
        sleep(1)
        # pi.set_servo_pulsewidth(pin_pillar, deg_90) # middle
        # sleep(1)
    
        # pi.set_servo_pulsewidth(pin_plate, deg_180) # position clockwise
        # sleep(1)
        # pi.set_servo_pulsewidth(pin_pillar, deg_180) # position clockwise
        # sleep(1)
        
        # pi.set_servo_pulsewidth(pin_plate, deg_90) # middle
        # sleep(1)
        # pi.set_servo_pulsewidth(pin_pillar, deg_90) # middle
        # sleep(1)
