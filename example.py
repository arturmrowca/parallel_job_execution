
from multiprocessing import freeze_support
import time
import random
from parallel_job import parallelize_jobs

def func(x, y):
    print("Evaluating: %s + %s" % (x, y))
    time.sleep(1+random.random())
    return x + y

if __name__ == '__main__':
    # NEEDS TO BE SET
    freeze_support()
    
    # 1. Create Arguments (=input) for each  job
    input_jobs = [(1, 2)]
    input_jobs += [(8, 12)]
    input_jobs += [(11, 14)]
    input_jobs += [(7, 6)]
    input_jobs += [(17, 13)]
    input_jobs += [(14, 16)]
    input_jobs += [(132, 99)]
    input_jobs += [(123, 321)]
    input_jobs += [(1, 14)]
    input_jobs += [(11, 8)]
    
    # 2. number of processes that are allowed simultaneously
    simultaneous_processes = 3
    
    # 3. process those arguments in parallel and store results to list of outputs
    job_outputs = parallelize_jobs(input_jobs, func, simultaneous_processes, disable_output=False)
    
    # 4. print results
    print("\nResults of computation: ")
    for output in job_outputs:
        print("Result: %s"%(str(output)))