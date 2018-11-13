import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

from multiprocessing import Pool
#multiprocessing.freeze_support() # <- may be required on windows

def first_try(x, y):

    plt.scatter(x, y)
    plt.legend()
    plt.show()
    
def second_try(x, y):

    plt.scatter(x, y)
    plt.legend()
    plt.show()

def multiP():
    p = Pool(3)
    for i in range(3):
        p.apply_async(second_try, args=(i, i))
    p.close()
    p.join()

if __name__ == "__main__": 
    first_try(1,1)
    # input('Value: ') 
    multiP()