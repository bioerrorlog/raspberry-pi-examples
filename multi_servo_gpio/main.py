import math
import time
from gpiozero import AngularServo


def main():
    servo_17 = AngularServo(17)
    servo_18 = AngularServo(18)
    servo_27 = AngularServo(27)

    t = 0
    max_angle = 60
    gap_angle = 30

    try:
        while True:
            servo_17.angle = math.sin(math.radians(t % 360)) * max_angle
            servo_18.angle = math.sin(math.radians((t % 360) + gap_angle)) * max_angle
            servo_27.angle = math.sin(math.radians((t % 360) + (gap_angle * 2))) * max_angle

            t += 2
            time.sleep(0.01)
    except KeyboardInterrupt:
        servo_17.angle = 0
        servo_18.angle = 0
        servo_27.angle = 0


if __name__ == '__main__':
    main()
