# Catalan Number

### Equivalent Definitions of the Catalan Number

The Catalan number $C_n$ can be defined in several equivalent ways:

- **Parentheses Matching**: $C_n$ is the number of valid ways to form $n$ pairs of parentheses such that they are properly matched (e.g., `(()())` or `(())()` for $n = 3$).
- **Dyck Paths**: $C_n$ is the number of lattice paths from $(0,0)$ to $(2n,0)$ in the integer plane that:
  - Use $n$ steps of $(1,1)$ (up) and $n$ steps of $(1,-1)$ (down),
  - Never dip below the $x$-axis at any point.
- **Triangulations of a Polygon**: $C_n$ is the number of ways to triangulate a convex polygon with $n+2$ vertices.
- **Binary Trees**: $C_n$ is the number of distinct binary trees with $n$ nodes.

### Calculation of $C_n$

The $n$-th Catalan number is given by:

$$
C_n = \frac{1}{n+1} \binom{2n}{n}.
$$

#### Proof Using Reflection Principle

1. Consider a lattice path from $(0,0)$ to $(2n,0)$. The total number of such paths, without any restrictions, is $\binom{2n}{n}$, as we need to choose $n$ upward steps (or equivalently, downward steps) from $2n$ total steps.

2. Some of these paths dip below the $x$-axis. Reflect any such path at the first point where it touches $y = -1$. The reflected portion creates a path from $(0,0)$ to $(2n,-2)$ with $n-1$ up steps and $n+1$ down steps. 

3. The number of such "invalid" paths is $\binom{2n}{n-1}$, as we are choosing $n-1$ upward steps from $2n$ total steps.

4. Subtracting these invalid paths from the total gives:

$$
C_n = \binom{2n}{n} - \binom{2n}{n-1}.
$$

Using the identity $\binom{2n}{n-1} = \frac{n}{n+1} \binom{2n}{n}$, we simplify:

$$
C_n = \binom{2n}{n} - \frac{n}{n+1} \binom{2n}{n} = \frac{1}{n+1} \binom{2n}{n}.
$$

### Example Applications

#### Ticket Line Problem

**Scenario**: At a theater, $2n$ people are waiting to buy tickets. $n$ of them have only \$5 bills, and the other $n$ have only \$10 bills. Each ticket costs \$5, and the ticket seller has no change initially. What is the probability that all people can buy their tickets without anyone needing to change their position in line?

**Solution**:  
- Model this situation as a lattice path problem where:
  - A person with a \$5 bill corresponds to an upward step $(1,1)$,
  - A person with a \$10 bill corresponds to a downward step $(1,-1)$.
- The requirement that no one needs to change positions translates to ensuring that the lattice path never dips below the $x$-axis.

The number of valid paths is $C_n = \frac{1}{n+1} \binom{2n}{n}$, and the total number of paths (without restrictions) is $\binom{2n}{n}$. Thus, the probability is:

$$
p = \frac{\text{Valid paths}}{\text{Total paths}} = \frac{C_n}{\binom{2n}{n}} = \frac{1}{n+1}.
$$

