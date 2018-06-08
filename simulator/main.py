import multiprocessing
NUM_NODES = 100


def node(inbox, id):
    for k, v in inbox.items():
        v.put('Hi %d, I am %d' % (k, id))


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    communal_inbox = dict((i, multiprocessing.Queue()) for i in range(NUM_NODES))
    jobs = [multiprocessing.Process(target=node, args=(communal_inbox, i)) for i in range(10)]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    for _ in range(10):
        print(communal_inbox[5].get())
