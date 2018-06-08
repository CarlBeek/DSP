from multiprocessing import Process, Queue
from random import random
NUM_NODES = 100


class Node:
    def __init__(self, inbox, uid):
        self.inbox = inbox
        self.id = uid
        self.num_nodes = len(inbox)

    def _gossip(self, m, p=.5):
        for k, v in self.inbox.items():
            if random() < p and k != self.id:
                v.put(m)

    def _broadcast(self, m):
        for k, v in self.inbox.items():
            if k != self.id:
                v.put(m)

    def _send(self, m, dest):
        try:
            self.inbox[dest].put(m)
        except KeyError:
            print('Node doesnt exist')


if __name__ == '__main__':
    communal_inbox = dict((i, Queue()) for i in range(NUM_NODES))
    jobs = [Process(target=Node, args=(communal_inbox, i)) for i in range(NUM_NODES)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
