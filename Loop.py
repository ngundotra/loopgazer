from threading import Thread
import urllib
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from utils import base_url, post_progress, validate_usr, get_progress


class Loop(object):
    """
    Wraps any object which has a len method & iter method
    """
    password = None
    username = None

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
                handleloop = Thread(target=self.handle_loop, daemon=True)
                handleloop.start()
            except Exception:
                print("Could not start new thread")
        return self.iterable.__next__()

    def print_curr(self):
        """
        prints a number of bars according to the self.curr thing
        Mostly just meant to be a debugger/example method
        """
        num_bars = int(self.curr / self.len * self.ncols)
        print("x"*num_bars, end='\r')

    def handle_loop(self):
        """
        Called for each n iterations. Usually performed asynchronously
        """
        ext = '/progress'
        url = base_url + ext
        try:
            progress = self.curr / self.len
            message = post_progress(Loop.username, Loop.password, progress).read()
            if message.decode() != 'Success!':
                print(message)
                print("Failed :,(")
        except urllib.error.URLError:
            print("Could not find URL. Please check your internet connection.")

    @staticmethod
    def config(filename):
        """
        Takes username & password (eventually auth token) from a filename.
        Sets up the Loop library.
        """
        ext = '/validate'
        url = base_url + ext

        username, password = Loop.user_info_from(filename)
        response = validate_usr(username, password)
        message = response.read()
        if message.decode() != 'True':
            print(message)
            raise ValueError("User/pwd combo incorrect")

        Loop.username = username
        Loop.password = password

    @staticmethod
    def user_info_from(filename):
        """
        Parses plaintext file :/
        (I could do custom encoding/decoding scheme, but... maybe already tried/true way?)
        """
        with open(filename, 'rb') as usr_f:
            user, pwd = usr_f.readline(), usr_f.readline()
            user = user.strip()
            pwd = pwd.strip()
        return user, pwd

    @staticmethod
    def watch_loop_progress(timeout=20, num_cols=20):
        """
        Spawns thread to watch the user's loop progress.
        Prints to terminal.
        Watches for `timeout` seconds. User may or may not have an active
        loop.
        """
        if not Loop.username or not Loop.password:
            raise ValueError("Please run Loop.config(cred_file) before.")

        # Spawn print thread
        def print_loop():
            response = get_progress(Loop.username, Loop.password)
            progress = int(response.read())
            print("{}:".format(Loop.username) + '#' * int(num_cols * progress), end='\r')

        def printer_target():
            while True:
                print_loop()

        printer_thread = Thread(target=printer_target)
        printer_thread.start()

        if timeout:
            printer_thread.join(timeout=timeout)
        else:
            printer_thread.join()

