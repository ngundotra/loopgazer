
import urllib.request
import _thread

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
        if self.curr % 1 == 0:
            try:
                _thread.start_new_thread(self.handle_loop, ())
            except Exception:
                print("Could not start new thread")
        return self.iterable.__next__()

    def print_curr(self):
        """
        prints a number of bars according to the self.curr thing
        """
        num_bars = int(self.curr / self.len * self.ncols)
        print("x"*num_bars, end='\r')

    def handle_loop(self):
        """
        Called for each n iterations.
        """
        try:
            result = urllib.request.urlopen("https://docs.python.org/3/library/urllib.request.html")
            print(result.info())
        except urllib.error.URLError:
            print("Could not find URL. Please check your internet connection.", end='\r')
        """type is http.client.HTTPMessage"""