# multi_servo_gpio
Control multi servo motors.

## How to run

```sh
# Install required packages
sudo apt update
sudo apt upgrade
sudo apt install python3-pip python3-dev gcc git
sudo pip install -r requirements.txt

# Run script
sudo python3 main.py
# You need to run as root to avoid the error:
# RuntimeError: No access to /dev/mem. Try running as root!
```

## Reference
- https://github.com/bioerrorlog/snake-servo-pi
