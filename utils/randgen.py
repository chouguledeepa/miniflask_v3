import random


import random


class ProduceChars:
    """generator class to produce random numbers in a given range"""

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        current = self.start
        while current < 3:
            yield random.randrange(self.start, self.stop)
            current += 1
