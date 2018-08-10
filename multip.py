from multiprocessing import Pool
import os, time, random
import numpy as np


def long_time_task(i,j,k):
    return i*25+j*5+k

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
#    index = []
    xx = []
    p = Pool(4)
    n = 125
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
                r = p.apply_async(long_time_task, args=(i,j,k))
                xx.append([i,j,k,r])
#        index.append(i)
    
    print('Waiting for all subprocesses done...')
#    p.close()
#    p.join(1)

    print('All subprocesses done.')
    flux = np.zeros([n,n,n])
    
#    a = np.asarray(xx)
#    flux[a[:,0],a[:,1],a[:,2]] = a[:,3]
    for nn in xx:
        print(nn[0],nn[1],nn[2])
        flux[nn[0],nn[1],nn[2]] = nn[3].get()
        
 
    flux.tofile("filename.bin")
    b = np.fromfile("filename.bin",dtype = 'float64')
    b.shape = (n,n,n)
