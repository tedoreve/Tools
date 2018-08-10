import time, threading
import numpy as np

# 假定这是你的银行存款:
start = time.time()
x = 128
balance = np.zeros([x,x,x])

def change_it(i,j,k):
    # 先存后取，结果应该为0:
    global balance
    balance[i,j,k] = i*25+j*5+k
#    balance = balance - n

def run_thread(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
                change_it(i,j,k)

#t1 = threading.Thread(target=run_thread, args=(x,))
#t1.start()
#t1.join()

run_thread(x)
print(balance)
end = time.time()
print(end-start)
#from multiprocessing import Pool
#import os, time, random
#
#
#
#def long_time_task(i,j,k):
#    return i*25+j*5+k
#
#if __name__=='__main__':
#    print('Parent process %s.' % os.getpid())
##    index = []
#    xx = []
#    p = Pool(4)
#    for i in range(5):
#        for j in range(5):
#            for k in range(5):
#                r = p.apply_async(long_time_task, args=(i,j,k))
#                xx.append([i,j,k,r])
##        index.append(i)
#    
#    print('Waiting for all subprocesses done...')
##    p.close()
##    p.join(1)
#
#    print('All subprocesses done.')
#    flux = np.zeros([5,5,5])
#    
##    a = np.asarray(xx)
##    flux[a[:,0],a[:,1],a[:,2]] = a[:,3]
#    for n in xx:
#        flux[n[0],n[1],n[2]] = n[3].get()
        
 

