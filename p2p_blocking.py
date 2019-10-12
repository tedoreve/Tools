# send_recv_timing.pu

import time
import numpy as np
from mpi4py import MPI

def f(x, y):
    return x+y, y


flux_vol = np.zeros([4,4,4,2])

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

per = flux_vol.shape[2]//size

print(rank)

comm.Barrier()
start_time = time.time()

for i in range(per * rank, per * (rank+1)):
    for j in range(flux_vol.shape[1]):
        for k in range(flux_vol.shape[0]):
            # for l in range(2):
                flux_vol[i,j,k,:] = f(i*j*k, i-j-k)


if rank == 0:
    total = np.zeros([flux_vol.shape[2],flux_vol.shape[1],flux_vol.shape[0],2])
else:
    total = None

comm.Barrier()
#collect the partial results and add to the total sum
comm.Reduce(flux_vol, total, op=MPI.SUM, root=0)

stop_time = time.time()

if rank == 0:
    print ("-----", (stop_time-start_time)*1000, "-----")
    total.tofile("a.bin")
