

class Loop(object):
    """
    Wraps any iterable, and pushes updates to a server :)
    """

    def __init__(self, iterable):
        try:
            iterable = iter(iterable)
            self.iterable = iter(iterable)
        except TypeError as te:
            print("Please pass an iterable.")
            raise te

    def __iter__(self):
        """This class is the iterable object"""
        return self

    def __next__(self):
        return self.iterable.__next__()
