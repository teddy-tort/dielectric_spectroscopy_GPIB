"""
Code that can be used to raise exceptions when something takes too long.
"""
import signal
import time


def test_request(arg=None):
    """Your http request."""
    time.sleep(2)
    return arg


class Timeout():
    """Timeout class using ALARM signal."""

    class Timeout(Exception):
        pass

    def __init__(self, sec):
        self.sec = sec

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.raise_timeout)
        signal.alarm(self.sec)

    def __exit__(self, *args):
        signal.alarm(0)  # disable alarm

    def raise_timeout(self, *args):
        raise Timeout.Timeout()


def main():
    # Run block of code with timeouts
    try:
        with Timeout(3):
            print test_request("Request 1")
        with Timeout(1):
            print test_request("Request 2")
    except Timeout.Timeout:
        print "Timeout"


if __name__ == "__main__":
    main()