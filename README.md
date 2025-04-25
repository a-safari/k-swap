This repository provides the implementation of the randomized and naive k-swap algorithms as presented in the paper:

**"A k-swap Local Search for Makespan Scheduling"**  
*Lars Rohwedder, Ashkan Safari, and Tjark Vredeveld*  
[arXiv:2401.05956](https://arxiv.org/abs/2401.05956)


## Repository Structure

- **`main.py`**: Coordinates the execution of experiments, including loading instances, running the k-swap algorithms, and recording the results.

- **`KSwap.py`**: Contains the core implementations of the k-swap local search algorithms, including both the naive and randomized versions. It defines the logic for identifying and performing improving k-swap moves.

- **`scheduleStructure.py`**: Defines the data structures and functions related to job scheduling, such as representing schedules, calculating makespans, and applying job swaps.

**`Instances/` and `ConvertedInstances/`**: Directories containing the same problem instances in two different encoding formats.

- **`Computational Results/`**: Contains all the results of the experiments.

## Problem Instances

The `Instances/` directory includes **9 classes of instances**, each consisting of **50 files**, for a total of 450 unique problem instances. These classes vary in the number of machines and jobs.
In each file, the first and second lines specify the number of machines and jobs, respectively. The subsequent lines list the processing times of the jobs.
Each instance file is named according to the format M<i>_N<j>U<min>_<max>, where
- `i` is the number of machines,
- `j` is the number of jobs,
- `U<min>_<max>` indicates that the job processing times are uniformly drawn from the range [`min`, `max`].

## Computational Results
