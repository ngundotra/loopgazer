
from Loop import Loop

def test_loop():
    bar = range(5)
    for i in Loop(bar):
        print(i)


if __name__ == '__main__':
    test_loop()