

class Loop(object):
    """
    Wraps any object which has a len method & iter method
    """

    def __init__(self, iterable):
        self.len = len(iterable)
        self.curr = 0
        self.ncols = 10
        try:
            self.iterable = iter(iterable)
        except TypeError as te:
            print("Please pass an iterable.")
            raise te

    def __iter__(self):
        """This class is the iterable object"""
        return self

    def __next__(self):
        self.print_curr()
        self.curr += 1
        return self.iterable.__next__()

    def print_curr(self):
        """
        prints a number of bars according to the self.curr thing
        """
        num_bars = int(self.curr / self.len * self.ncols)
        print("x"*num_bars, end='\r')
