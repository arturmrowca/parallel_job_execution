[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/PhilippMundhenk/IVNS/blob/master/LICENSE)

# Description
This implementation is a simple way to parallelize any function that has to be executed per input argument, producing outputs. I.e., it is a 
way to pass multiple jobs that are evaluated in parallel. In order to limit computational power, the maximum number of processes that are working
 at the same time can be limited, to a fixed number.

# Example
This example is given in file example.py. First, we define the function that we want to work on the workers.
```python
from multiprocessing import freeze_support
import time
import random
from parallel_job import parallelize_jobs

def func(x, y):
    print("Evaluating: %s + %s" % (x, y))
    time.sleep(1+random.random())
    return x + y
```

Next, we need to wrap the processing in a main method and set freeze_support(). This is necessary in order for 
multiprocessing to work properly.

```python
if __name__ == '__main__':
    # NEEDS TO BE SET
    freeze_support()
```
With this, we can create a number arguments that we want the workers to work off. Also, we define the 
number of processes that we want to maximally run in parallel. Here, 3 processes would run in parallel. 
I.e. if we have 10 jobs that we want to work of, first 3 processes with the first 3 arguments would be started. 
Once any of the processes finishes, the next process starts, such that at all time a maximum of 3 processes is running.
```python
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
```
Now we can start the method and read out the outputs, which are returned as list of results. Be careful about the order of the 
results. As data is processed in parallel the output list is not in the same order as the input list. 

```python
    # 3. process those arguments in parallel and store results to list of outputs
    job_outputs = parallelize_jobs(input_jobs, func, simultaneous_processes, disable_output=False)
    
    # 4. print results
    print("\nResults of computation: ")
    for output in job_outputs:
        print("Result: %s"%(str(output)))
```