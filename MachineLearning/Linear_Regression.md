# Linear Regression

### Simple Linear Regression

Given data points $(x_1, y_1), \ldots, (x_n, y_n)$, We need to find a line: 
$Y = \hat{\beta}_0 + \hat{\beta}_1 X$ that best fit the data.

We define the following terminologies:
- **Residual**: $e_i = y_i - (\hat{\beta}_0 + \hat{\beta}_1 x_i)$
- **Residual sum of squares (RSS)**: $RSS = \sum_{i=1}^n e_i^2.$
- **Mean squared error (MSE)**: $MSE = \frac{1}{n} \sum_{i=1}^n e_i^2  = 
  \frac{1}{n}RSS$

We need to find $\hat{\beta}_0, \hat{\beta}_1$ that minimize the MSE.
  
#### Least Squares Estimators

The above problem has an analytic solution. The **least squares estimates** for 
$\beta_0$ and 
$\beta_1$ are:

$$
\hat{\beta}_1 = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1 \bar{x},
$$

where $\bar{x}$ and $\bar{y}$ are the means of $x_i$ and $y_i$.

---

### Model Interpretation

Assume the true relationship is:

$$
Y = \beta_0 + \beta_1 X + \epsilon,
$$

where $\epsilon$ is random noise with mean zero, independent of $X$. 
The least squares estimators $\hat{\beta}_0$ and $\hat{\beta}_1$ are 
unbiased estimators for $\beta_0,\beta_1$. It means $\mathbb{E}[\hat{\beta}
_j] = \beta_j$.

#### Standard Errors

The standard errors quantify the variability of the estimators:

$$
SE(\hat{\beta}_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n (x_i - \bar{x})^2}, \quad SE(\hat{\beta}_0)^2 = \sigma^2 \left( \frac{1}{n} + \frac{\bar{x}^2}{\sum_{i=1}^n (x_i - \bar{x})^2} \right),
$$

where $\sigma^2$ is the variance of the error $\epsilon$. In practice, 
$\sigma$ is unknown and estimated by the **residual standard error (RSE)**: 
$RSE = \sqrt{\frac{RSS}{n-2}}$.

#### Confidence Intervals and Hypothesis Testing

- The 95% confidence intervals for $\beta_0$ and $\beta_1$ are:

$$
\hat{\beta}_0 \pm 2 \cdot SE(\hat{\beta}_0), \quad \hat{\beta}_1 \pm 2 \cdot SE(\hat{\beta}_1).
$$

- To test the null hypothesis $H_0: \beta_1 = 0$ (no relationship between $X$ and $Y$), use the t-statistic:

$$
t = \frac{\hat{\beta}_1}{SE(\hat{\beta}_1)}.
$$

---

### Model Assessment

#### Residual Standard Error (RSE)

RSE is an unbiased estimator for the standard deviation of the error 
$\epsilon$, representing the average deviation of observed values from the 
regression line. It is calculated as:

$$
RSE = \sqrt{\frac{RSS}{n-2}}.
$$

While RSE measures the model's lack of fit, its interpretation depends on the scale of $Y$.

#### $R^2$ Statistic

The $R^2$ statistic measures the proportion of variance in $Y$ explained by $X$:

$$
R^2 = 1 - \frac{RSS}{TSS},
$$

where $TSS = \sum_{i=1}^n (y_i - \bar{y})^2$ is the total sum of squares. It satisfies:

- $0 \leq R^2 \leq 1$, with higher values indicating better fit.
- $R^2 \approx 1$ suggests that most variability in $Y$ is explained by $X$.

$R^2$ also estimates $1 - \frac{\text{Var}(\epsilon)}{\text{Var}(Y)}$, 
further reinforcing its interpretation as the proportion of variance explained.

---

### Multilinear Regression

Suppose that we have **predictors** $X_1, \ldots, X_p$. Then, a multilinear 
regression model is:

$$
Y = \beta_0 + \beta_1 X_1 + \cdots + \beta_p X_p + \epsilon.
$$

**Remarks:**
1. In simple linear regression of $Y$ with $X_1$, we might find $\hat{\beta}
   _1 \neq 0$ (indicating high marginal dependence). However, in 
   multilinear regression, $\hat{\beta}_1 = 0$ could occur due to 
   correlations between $X_1$ and other predictors.
2. The RSE for multilinear regression is computed as:

$$
RSE = \sqrt{\frac{RSS}{n - p - 1}}.
$$

---

### Collinearity of Predictors and Ridge Regression

When predictors are correlated, e.g., $X_1$ and $X_2$, the data matrix $X$ 
becomes nearly singular. In this case:
- The least square estimators $\hat{\beta}_1$ and $\hat{\beta}_2$ become 
  highly sensitive to the observed data.
- The estimators will have large standard errors, leading to a lack of 
  robustness in the model.

**Solution:** Ridge Regression. By adding $\alpha \|\beta\|_2^2$ (a scaled 
$L^2$ norm of the coefficients) to the loss function, the model penalizes 
large coefficients, reducing variance and increasing stability.

---

### Effect of Doubling the Data

If the data is accidentally doubled, the regression coefficients remain 
unchanged. However:
- The residuals $\epsilon_i$ become correlated.
- With $2n$ samples, the standard errors of the coefficients are 
  underestimated by a factor of $\sqrt{2}$, leading to falsely narrowed 
  confidence intervals.

In general, when residuals are correlated, the computed standard errors 
underestimate their true values, creating a false sense of confidence in the model.




