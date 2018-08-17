
from Loop import Loop
from time import sleep
from Auth import config

def test_loop():
    bar = range(5)
    print("running loop")
    for i in Loop(bar):
        sleep(.5)
        pass


if __name__ == '__main__':
    config('Noah', '742')
