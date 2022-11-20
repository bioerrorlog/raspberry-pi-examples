import cv2


def main():
    cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    ret, frame = cap.read()
    cv2.imwrite('check.jpg', frame)
    cap.release()


if __name__ == '__main__':
    main()
