---
permalink: /Finance/utiliy_and_risk_preference
menubar: leftnav
---
# Risk Preference, Utility Function Convexity, and Jensen's Inequality

### Risk Preference and the Utility Function

In expected utility theory, an individual's preferences over uncertain 
outcomes are represented by a non-decreasing **utility function** $u(x)$, 
where $x$ typically represents wealth. An important concept here is 
**marginal utility**, which is the additional utility obtained from a small 
increase in $x$. Formally, marginal utility is defined as the derivative $u'
(x)$. It measures how much utility increases when wealth increases by one 
unit. For instance, if $u'(x)$ is high, an extra dollar provides a 
significant increase in utility; if it is low, the extra dollar contributes 
only a little additional utility.

- **Risk-averse** individuals prefer a certain outcome to a risky one with 
  the same expected value. Their utility functions are **concave**, which 
  also implies decreasing marginal utility. This means that as wealth 
  increases, the additional satisfaction gained from each extra unit of 
  wealth decreases.
- **Risk-neutral** individuals are indifferent between certain and 
  uncertain outcomes with the same expected value. Their utility functions 
  are **linear**, implying constant marginal utility.
- **Risk-seeking** individuals prefer risky outcomes over certain ones with 
  the same expected value. Their utility functions are **convex**, meaning 
  that the marginal utility is increasing.

For a risk-averse person, the concavity of the utility function implies 
decreasing marginal utility. In other words, for any increment $\Delta > 0$:

$$
u(x+\Delta) - u(x) < u(x) - u(x-\Delta)
$$

This inequality captures the intuition that the additional satisfaction (or 
utility) from gaining an extra $\Delta$ dollars is less than the loss in 
satisfaction from losing $\Delta$ dollars.

### Relation with Jensen's Inequality

For a concave function $u$ (which represents risk aversion) and a random 
variable $X$ representing uncertain wealth, Jensen's inequality states:

$$
u\big(\mathbb{E}[X]\big) \geq \mathbb{E}[u(X)]
$$

**Interpretation:**
- The utility of the expected wealth, $u\big(\mathbb{E}[X]\big)$, is 
  greater than or equal to the expected utility of the wealth $\mathbb{E}[u(X)]$.
- This inequality explains risk aversion: even though the risky prospect 
  $X$ and the certain amount $\mathbb{E}[X]$ have the same expected 
  monetary value, the risk-averse individual prefers the certainty of $\mathbb{E}[X]$.

### Risk Premium

The **certainty equivalent** $C$ of a random wealth $X$ is defined as the 
amount of wealth that, if received with certainty, provides the same level 
of utility as the uncertain prospect:

$$
u(C) = \mathbb{E}[u(X)]
$$

The **risk premium** $\pi$ is the extra expected return that a risk-averse 
individual requires to be indifferent between a risky prospect and a 
certain outcome. It is defined as the difference between the expected value 
of the risky prospect and its certainty equivalent:

$$
\pi = \mathbb{E}[X] - C
$$

### Expanded Discussion on the Risk Premium

For a risk-averse investor, accepting a risky asset means facing 
uncertainty about the outcome. To compensate for this uncertainty, the 
investor demands a **risk premium**—an additional expected return over the 
certainty equivalent.

Key points regarding the risk premium include:

1. **Compensation for Risk:**
   - The risk premium represents the compensation required for bearing risk.
     A higher risk premium indicates that the investor requires more 
     additional expected return to be willing to accept the uncertainty 
     associated with the risky asset.

2. **Relationship with Utility Curvature:**
   - The magnitude of the risk premium is related to the curvature 
     (concavity) of the utility function. More risk-averse individuals 
     (with a higher degree of concavity) will have a larger risk premium.
   - The Arrow-Pratt measure of absolute risk aversion, defined as $-\frac
     {u''(x)}{u'(x)}$, quantitatively links the curvature of the utility 
     function to the risk premium. A larger value indicates greater risk 
     aversion and typically a higher risk premium.

3. **Economic Interpretation:**
   - In a financial context, the risk premium can be viewed as the excess 
     return that an investor expects to earn from holding a risky asset 
     rather than a risk-free asset. This concept is central to asset 
     pricing models and helps explain phenomena such as the equity premium.

4. **Certainty Equivalence:**
   - The certainty equivalent $C$ is always less than the expected value 
     $\mathbb{E}[X]$ for a risk-averse individual. The difference $\pi = 
     \mathbb{E}[X] - C$ quantifies the investor's dislike for risk.
   - If the investor were risk-neutral, the certainty equivalent would 
     equal the expected value (i.e., $C = \mathbb{E}[X]$) and the risk 
     premium would be zero.

 
