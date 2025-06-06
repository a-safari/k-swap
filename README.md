This repository provides the implementation of the randomized and naive k-swap algorithms as presented in the paper:

**"A *k*-swap Local Search for Makespan Scheduling"**  
*Lars Rohwedder, Ashkan Safari, and Tjark Vredeveld*  
[arXiv:2401.05956](https://arxiv.org/abs/2401.05956)


## Repository Structure

- **`main.py`**: Coordinates the execution of experiments, including loading instances, running the randomized and naive *k*-swap algorithms, and recording the results.

- **`KSwap.py`**: Contains the core implementations of the *k*-swap local search algorithms, including both the naive and randomized versions. It defines the logic for identifying and performing improving *k*-swap moves.

- **`scheduleStructure.py`**: Defines the data structures and functions related to job scheduling, such as representing schedules, calculating makespan, and applying job swaps.

- **`Instances/` and `ConvertedInstances/`**: Directories containing the same problem instances in two different encoding formats.

- **`Computational Results/`**: Contains all the results of the experiments.

## Problem Instances

The `Instances/` directory includes **9 classes of instances**, each consisting of **50 files**, for a total of 450 unique problem instances. These classes vary in the number of machines and jobs.
In each file, the first and second lines specify the number of machines and jobs, respectively. The subsequent lines list the processing times of the jobs.
Each instance file is named according to the format `M<i>_N<j>_U<min>_<max>`, where
- `i` is the number of machines,
- `j` is the number of jobs,
- and `U<min>_<max>` indicates that the job processing times are uniformly drawn from the range [`min`, `max`].

## Computational Results

The `Computational Results/` directory contains the output of running the randomized and naive *k*-swap algorithms on all 450 instances.

It consists of two subdirectories:

### `excel/`

This subdirectory contains summarized results in `.xlsx` format for convenient inspection and comparison. In this subdirectory, there is one Excel file per **class of instances**. Each Excel file aggregates the computational results for **all 50 instances** in that class.

### `dat/`

For each class of instances `M<i>_N<j>_U1_1000000000`, we include the following `.dat` files. In each filename, `N` and `R` indicate results from the `Naive` and `Randomized` algorithms, respectively.

**All reported values are averaged over the 50 instances belonging to the corresponding class.**

- `M<i>_N<j>_U1_1000000000_<N/R>_TotalTime.dat`:  
  For each value of *k*, this file reports the average total running time (in seconds) required to converge to a *k*-swap optimal solution. Each row contains: *k* and the corresponding average time.

- `M<i>_N<j>_U1_1000000000_<N/R>_Time.dat`:  
  For each value of *k*, this file reports the average time (in seconds) taken to find an improving *k*-swap neighbor. Each row contains: *k* and the average time.

- `M<i>_N<j>_U1_1000000000_<N/R>_NumIterations.dat`:  
  For each value of *k*, this file reports the average number of iterations until convergence to a *k*-swap optimal solution. Each row contains: *k* and the average number of iterations.

- `M<i>_N<j>_U1_1000000000_<N/R>_MS.dat`:  
  For each value of *k*, this file reports the average relative makespan improvement (in percentage) of the *k*-swap optimal solution compared to the initial makespan. Each row contains: *k* and the average improvement.

- `M<i>_N<j>_U1_1000000000_k<l>_<N/R>_MSPerIteration.dat`:  
  For *k = l*, this file reports the average relative makespan improvement (in percentage) at each iteration *t*, compared to the initial makespan. Each row contains: iteration number *t* and the average improvement.

These files enable detailed analysis of performance and convergence across different values of *k* and algorithm variants.
