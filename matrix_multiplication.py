import numpy as np
import sys
import time
import matplotlib.pyplot as plt

def main(n=500,steps = 25):
    """Computes the multiplication of growing matrices until size n in a given number of steps"""
    print("Computation started")
    time_list = []

    for i in range(0,n,int(n/steps)):
        time_start = time.time()
        matrix_a = np.random.rand(i,i)
        matrix_b = np.random.rand(i,i)
        result = matrix_a * matrix_b
        time_end = time.time()
        total_time = time_end - time_start
        time_list.append(total_time)
    print("Computation ended")
    plt.plot(range(0,n,int(n/steps)),time_list)
    plt.show()
main(10000)