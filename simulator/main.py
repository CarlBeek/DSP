from multiprocessing import Process, Queue
from node import Node


NUM_NODES = 100

if __name__ == '__main__':
    communal_inbox = dict((i, Queue()) for i in range(NUM_NODES))
    jobs = [Process(target=Node, args=(communal_inbox, i)) for i in range(NUM_NODES)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()