from mpi4py import MPI
import random
from time import sleep

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# connected_nodes_out = [random.choice(range(size)) for _ in range(6)]
connected_nodes_out = range(size)

for i in connected_nodes_out:
    if i != rank:
        comm.isend('Hi ' + str(i) + ' I am ' + str(rank), i)

#
# def is_new_messages(req):
#     # print(req.test())
#     return req.test()[1] is not None
#
#
# def get_new_msg(req):
#     msg = req.wait()
#     return msg
#
#
# def process_new_message(req):
#     print(get_new_msg(req))
#
#
# sleep(0.5)
# r = comm.irecv()
# # for _ in range(1000):
# while True:
#     if is_new_messages(r):
#         process_new_message(r)
#     else:
#         sleep(0.005)

while True:
    print(comm.recv())
    sleep(0.1)
