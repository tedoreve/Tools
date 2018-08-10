import numpy as np
from mpi4py import MPI
import time

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

#a = np.zeros([10,10])
#b = np.zeros([10,10])
n = 3
#perrank = b//size
summ = np.zeros([n,n,n])

comm.Barrier()
start_time = time.time()

def long_time_task(i,j,k):
    return i+j+k

    

for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i,j,k)
            summ[i,j,k] = long_time_task(i,j,k)


if rank == 0:
    total = np.zeros([n,n,n])
else:
    total = None

comm.Barrier()
#collect the partial results and add to the total sum
comm.Reduce(summ, total, op=MPI.SUM, root=0)

stop_time = time.time()

if rank == 0:
    print ("The sum of numbers from 1 to 1 000 000: ", total)
    print ("time spent with ", size, " threads in milliseconds")
    print ("-----", (stop_time-start_time)*1000, "-----")