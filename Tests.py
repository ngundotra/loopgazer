
from Loop import Loop
from time import sleep


def test_loop(filename):
    Loop.config(filename)
    bar = range(5)
    print("running loop")
    for i in Loop(bar):
        sleep(.5)
        pass


if __name__ == '__main__':
    test_loop('ngundotra.txt')
