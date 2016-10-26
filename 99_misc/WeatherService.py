__author__ = 'sgr'

import sched
import time


def do_something():
        print ("Doing stuff...")

"""
Main function
"""
if __name__ == "__main__":
    a = 0

    s = sched.scheduler(time.time, time.sleep)
    s.enter(5, 1, do_something)
    #s.enter(10, 1, do_something, (s,))
    s.run()