### Monte Carlo Simulation for $\pi$

Let $X, Y \sim U[-1,1]$ be independent uniform random variables. Then, we have  
$$P(X^2 + Y^2 \leq 1) = \frac{\pi}{4}.$$  

This result follows from the fact that the probability of a randomly chosen point $(X, Y)$ falling inside the unit circle is proportional to the area of the quarter-circle in the square $[-1,1] \times [-1,1]$.  

Thus, we can estimate $\pi$ using Monte Carlo simulation by generating $n$ random points $(x_1, y_1), \dots, (x_n, y_n)$ and computing the proportion of points that lie inside the unit circle.

```python
import numpy as np

def pi_simulate(n_estimates):
    x = np.random.uniform(-1, 1, n_estimates)
    y = np.random.uniform(-1, 1, n_estimates)
    count = np.sum(x**2 + y**2 <= 1)
    return 4 * count / n_estimates

print(f"The estimated value of π is {pi_simulate(100000)}.")
```
---
### Monte Carlo Simulation for $e$

Let $X_1, X_2, \dots \sim U[0,1]$ be independent uniform random variables. 
Define $N$ as the smallest positive integer such that $\sum_{i=1}^{N} X_i \geq 1$.

We can show that  
$$P(N > n) = P\left(\sum_{i=1}^{n} X_i < 1\right) = \frac{1}{n!}.$$  

Using the tail sum formula for expectation, we derive  
$$\mathbb{E}[N] = \sum_{n=0}^{\infty} P(N > n) = \sum_{n=0}^{\infty} \frac{1}{n!} = e.$$  

Thus, we can estimate $e$ by repeatedly simulating the process and computing the average stopping time.

```python
import random

def estimate_e(n_estimates):
    total_counts = 0
    for _ in range(n_estimates):
        sum_uniforms = 0
        count = 0
        # Keep adding uniform random numbers until the sum exceeds 1
        while sum_uniforms <= 1:
            sum_uniforms += random.uniform(0, 1)
            count += 1
        total_counts += count

    return total_counts / n_estimates

# Run the simulation
print(f"Estimated value of e: {estimate_e(100000)}.")
```
