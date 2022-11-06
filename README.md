# Georgetown Quants - Monte Carlo Demonstration
Sang Doan & Joe Kleban. November 6th, 2022.

## Simulation Premise
Mr. Wong has 2 children, at least one of them is a boy. 
1. What's the probability that both of them are boys?
2. If the oldest child is a boy, what will that probability be?

We will sample as many Wongs as possible, and approximate
the ratio of the Wongs that have 2 boys to all the Wongs we sample.

## Implementation
- `main.py` contains the program client.
- `sequential.py` contains the core classes: `SampleNormalWongs` and `SampleOldestWong`.
- `parallel.py` provides the parallelized versions of the sequential classes.

## Exercise

### 0. Try running the code!

Note: The default classes used for simulation are the sequential classes. You don't need to change anything.

0. From terminal, run `python3 main.py`.
1. Enter number of samples and the kind of Wong (normal or oldest).
2. Repeat, or terminate the program by pressing `Ctrl + C`.

### 1. Inspect the codes

0. Vim `sequential.py` or open it in your favorite IDE.
1. How are the classes structured? What is inheritance doing here?
2. Why are there 2 different `sample_2_children` methods? Why is it different for 2 classes?
3. What is a `dataclass`? 
4. What is `__post_init__`? What is `__str__`? (They are called magic methods or dunder methods in Python.)
5. What is an `f`-string?

### 2. Performance Problems & Multiprocessing

Python is notoriously slow. Try it for yourself! 

First, simulate 1_000_000 samples. How long does it take? (You can use cmd `time` to precisely time the program.) Extrapolate the result for 1_000_000_000 samples.

0. Inspect `parallel.py`.
1. What is `Pool()`? What is it doing here?
2. Why do we need to rewrite the sampling method for both classes?
3. Why do we need to sum the results at the end of `__post_init__`?
4. Uncomment the `parallel` imports in `main.py` and comment the `sequential` imports.
5. Simulate 1_000_000 samples again. What is your CPU utilization while the program is running? How long does it take now?
6. Simulate 1_000_000_000 samples. You can see that the time taken is not linear. Why? What component of the code remains serial (i.e. not concurrent)?

***
