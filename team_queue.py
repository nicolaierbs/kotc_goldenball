import random


class TeamQueue:

    def __init__(self, length):
        self.queue = list(range(length))
        random.shuffle(self.queue)

    def order(self):
        return self.queue

    def active(self):
        return self.queue[0]

    def sideout(self, success):
        if success:
            self.queue = [self.queue[0]] + self.queue[2:] + [self.queue[1]]
        else:
            self.queue = [self.queue[1]] + self.queue[2:] + [self.queue[0]]
