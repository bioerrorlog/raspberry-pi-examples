from picamera import PiCamera
import time


def main():
    camera = PiCamera()

    camera.start_preview()
    time.sleep(2)

    camera.capture("check.jpg")


if __name__ == '__main__':
    main()
