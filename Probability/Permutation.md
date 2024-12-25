# Permutation Related Problems

### Derangement

Suppose $n$ exams are returned to $n$ students at random. What is the probability that no students receive their own exam as $n \to \infty$?

This problem is equivalent to finding the probability of picking a permutation $\sigma \in S_n$ with no fixed points.

#### Solution

The complement of this event is that at least one student receives their own exam. Let $E_i$ be the event that the $i$-th student receives their own exam. We have:

$$ P(E_i) = \frac{(n-1)!}{n!} = \frac{1}{n} $$

and 

$$ P(E_i \cap E_j) = \frac{(n-2)!}{n!}. $$

Let $E = \bigcup_{i=1}^n E_i$. Using the inclusion-exclusion principle, we compute:

$$
\begin{aligned}
P\left(\bigcup_{i=1}^n E_i\right) 
&= \sum_{i=1}^n P(E_i) - \sum_{i \neq j} P(E_i \cap E_j) + \cdots \\
&= n \frac{1}{n} - \binom{n}{2} \frac{(n-2)!}{n!} + \binom{n}{3} \frac{(n-3)!}{n!} \pm \cdots \\
&= 1 - \frac{1}{2!} + \frac{1}{3!} \pm \cdots \pm \frac{1}{n!}.
\end{aligned}
$$

Therefore, we have 

$$P(E^c) = \frac{1}{2!} - \frac{1}{3!}\pm\cdots \pm\frac{1}{n!}\rightarrow e^
{-1}$$

---

### Expected Number of Fixed Points

Suppose $n$ exams are returned to $n$ students at random. What is the expected number of students who receive their own exam?

#### Solution

Define an indicator random variable:

$$X_i = \begin{cases} 
1 & \text{if the $i$-th student receives their own exam} \\ 
0 & \text{otherwise}
\end{cases} $$

We compute that $ \mathbb{E}[X_i] = \frac{1}{n}$ since the probability of 
the $i$-th student receiving their own exam is $\frac{1}{n}$. Therefore, the expected number of fixed points is:

$$
\mathbb{E}\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n \mathbb{E}[X_i] =1. 
$$

---

### Expected Number of Cycles

Suppose we randomly pick a permutation $\sigma \in S_n$. What is the expected number of cycles in this permutation?

#### Solution

Let $X$ be the number of cycles, and $Y_i$ be the length of the cycle that 
includes the $i$-th element. Then, we can express $X$ as $ X = \sum_{i=1}^n 
\frac{1}{Y_i}$.

Observe that the random variables $Y_i$ are identically distributed, and so are the terms $\frac{1}{Y_i}$. Therefore, we have:

$$
\mathbb{E}[X] = \mathbb{E}\left[\sum_{i=1}^n \frac{1}{Y_i}\right] = n \mathbb{E}\left[\frac{1}{Y_i}\right].
$$

Now, let us compute the probability mass function of $Y_i$. For $k \in [1, n]$, the probability that $Y_i = k$ is:

$$
P(Y_i = k) = \frac{1}{n!} \binom{n-1}{k-1} \frac{k!}{k} (n-k)! = \frac{1}{n}.
$$

This formula is derived as follows:
- First, choose $k-1$ elements to be in the same cycle as the $i$-th element.
- Next, there are $\frac{k!}{k}$ ways to arrange these $k$ elements into a cycle.
- Finally, there are $(n-k)!$ ways to permute the remaining elements.

Using this result, we compute the expected value of $X$:

$$
\mathbb{E}[X] = n \mathbb{E}\left[\frac{1}{Y_i}\right] = n \sum_{k=1}^n \frac{1}{k} \cdot \frac{1}{n} = \sum_{k=1}^n \frac{1}{k}.
$$

#### Python Simulation

```python
import random

# This function will return the number of cycles in the permutation
def find_cycles(permutation: list[int]) -> int:
    visited = [False] * len(permutation)
    cycles = 0
    
    for start in range(len(permutation)):
        if not visited[start]:
            cycles += 1
            visited[start] = True
            i = start
            while not visited[i]:
                visited[i] = True
                i = permutation[i]
    return cycles

def simulate_cycles(n: int, num_simulations: int):
    total_cycles = 0
    
    for _ in range(num_simulations):
        permutation = list(range(n))
        random.shuffle(permutation)
        total_cycles += find_cycles(permutation)
        
    return total_cycles / num_simulations

def harmonic_number(n: int):
    return sum(1 / k for k in range(1, n+1))

# Sample use of the simulation program
n = 5
num_simulations = 1000

print(f"Simulated Expected Number of Cycles: {simulate_cycles(n, num_simulations):.4f}")
print(f"Analytical Expected Number of Cycles: {harmonic_number(n):.4f}")
```