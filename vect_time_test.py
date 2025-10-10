import time
import random
import numpy as np
import vec_test as vt


# Create list to store random numbers
random_numbers = list()
for i in range(100000):
     random_numbers.append(random.random())
# Create the numpy array
start_time = time.perf_counter_ns()
npa = np.array(random_numbers)
stop_time = time.perf_counter_ns()
print("time taken to create numpy array", stop_time - start_time)
# Now sum the numpy array
start_time = time.perf_counter_ns()
sum1 = npa.sum()
stop_time = time.perf_counter_ns()
print("time taken numpy", stop_time - start_time)
# Create the vect_test vector
start_time = time.perf_counter_ns()
vect = vt.VecTest(random_numbers)
stop_time = time.perf_counter_ns()
print("time taken create vect_test", stop_time - start_time)
# Sum using std accumulate
start_time = time.perf_counter_ns()
sum2 = vect.SumV()
stop_time = time.perf_counter_ns()
print("Time taken SumV",  stop_time - start_time)
# Sum using loop
start_time = time.perf_counter_ns()
sum3 = vect.SumV2()
stop_time = time.perf_counter_ns()
print("Time taken SumV2",  stop_time - start_time)
# Sum using Python sum function
start_time = time.perf_counter_ns()
sum4 = sum(random_numbers) 
stop_time = time.perf_counter_ns()
print("Time taken sum(list)",  stop_time - start_time)
# Print out the the sums
print("sum1 = " , sum1)
print("sum2 = " , sum2)
print("sum3 = " , sum3)
print("sum4 = " , sum4)

