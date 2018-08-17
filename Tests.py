
from Loop import Loop
from time import sleep

def test_loop():
    bar = range(5)
    print("running loop")
    for i in Loop(bar):
        sleep(0.1)
        pass


if __name__ == '__main__':
    test_loop()
