---
permalink: /Probability/Coin_Tossing_Sequence
menubar: leftnav
---
# Coin Tossing Sequence Problem

### Fair Coin Sequence

Suppose we are tossing a fair coin. What is the expected number of steps until
we get the coin sequence `HHTHH`?

#### Solution:

Consider a betting game where a gambler bets on whether the next coin toss will
be heads or tails. The gambler either loses all bet or doubles it with each
correct prediction.

Suppose in the $i$-th round of the game, gambler $i$ starts with only 1 dollar.
They bet all their money in the current and subsequent rounds, following the
target coin sequence. A gambler stops betting either when they win the full
sequence or lose all their money.

Let $X_n^i$ represent the money gambler $i$ has after round $n$. Define:

$$ S_n = \sum_{i=1}^n X_n^i $$

as the total money of all gamblers after round $n$, with $S_0 = 0$. It can be
shown that $S_n - n$ is a martingale with respect to the natural filtration.

Define the stopping time $T$ as the first time a gambler wins the entire
sequence. We can show that $\mathbb{E}[T] < \infty$. By the **Optional Stopping
Theorem** (or **Wald's Identity**), we have:

$$ \mathbb{E}[S_T - T] = \mathbb{E}[S_0 - 0] = 0. $$

Thus:

$$ \mathbb{E}[T] = \mathbb{E}[S_T]. $$

In this game, when a "lucky" gambler wins the full sequence, all gamblers who
started betting before this winner lose all their money, or they would be the "
lucky" gambler. The lucky gambler accumulates a total of $2^5 = 32$ dollars upon
winning the sequence.

After this, the next gamblers betting on `HHTH` (the first 4 letters of `HHTHH`)
lose to the actual sequence `HTHH` (the last 4 letters of `HHTHH`). Similarly:

- The next gambler betting `HHT` loses to `THH`.
- The next gambler betting `HH` wins, accumulating $1 \cdot 2 \cdot 2 = 4$
  dollars.
- Finally, the last gambler betting `H` wins $1 \cdot 2 = 2$ dollars.

Summing up:

$$\mathbb{E}[T] = \mathbb{E}[S_T] = 32 + 4 + 2 = 40.$$

---

### Fair Dice Sequence

Suppose we are tossing a fair dice. What is the expected number of tosses until
we get the dice sequence `111`?

#### Solution

We use a similar strategy as in the previous problem. However, the key
difference is that a gambler now only has a $1/6$ chance to win in a given
round. Consequently, $$S_n - n$$ is no longer a martingale.

To address this, we modify the game rules so that the gambler receives **6 times
their bet** if they win. Specifically, the dynamics are given by:

$$
X_{n+1}^i =
\begin{cases}
6 X_n^i & \text{ if the gambler wins the game,} \\
0 & \text{ if the gambler loses the game.}
\end{cases}
$$

With this adjustment, we see
that $\mathbb{E}[X_{n+1}^i \mid \mathcal{F}_n] = X_n^i$, which implies
that $X_n^i$ is a martingale with initial value $1$. Consequently, $S_n - n$
becomes a martingale centered at zero.

Using this framework, we calculate the expected number of tosses until a gambler
wins the sequence `111`:

$$
\mathbb{E}[T] = \mathbb{E}[S_T] = 6^3 + 6^2 + 6 = 258.
$$

---

### Unfair Coin Sequence

Suppose that we are tossing an unfair coin with probability $p = 0.2$ to toss a 
head.
What is the expected number of tosses until we get the coin sequence `HTH`?

#### Solution

We follow the same strategy to construct a martingale. We consider the betting
game with dynamics given by 

$$
X_{n+1} =
\begin{cases}
\frac{1}{p} X_n & \text{if the gambler wins on head} \\
\frac{1}{1-p} X_n & \text{if the gambler wins on tail} \\
0 & \text{if the gambler lose}
\end{cases}
$$

With this adjustment, we see
that $\mathbb{E}[X_{n+1} \mid \mathcal{F}_n] = X_n$, and consequently, $S_n-n$
is again a martingale.

Then, we calculate that 

$$\mathbb{E}[T] = \mathbb{E}[S_T] = 5 \cdot 1.25 \cdot 5 + 5 = 36.25$$