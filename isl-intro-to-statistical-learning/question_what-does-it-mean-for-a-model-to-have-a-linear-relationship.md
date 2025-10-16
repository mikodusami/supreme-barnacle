When a **parametric method** in Machine Learning (ML) assumes a relationship is **linear**, it means the model is built upon the premise that the relationship between the independent variables (features, $X$) and the dependent variable (target, $Y$) can be accurately represented by a straight line or a hyperplane.

This is expressed mathematically as a **linear equation** with a fixed number of parameters (coefficients or weights) that are estimated from the data.

### Key Implications of the Linear Assumption

1.  **Fixed Functional Form**: The model pre-defines the shape of the relationship. For a simple linear regression, this form is:
    $$Y \approx \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \dots + \beta_p X_p$$
    * $Y$ is the target variable.
    * $X_1, X_2, \dots, X_p$ are the features.
    * $\beta_0, \beta_1, \dots, \beta_p$ are the **fixed parameters** (coefficients) of the model that must be learned from the data. This is why it's a *parametric* model.

2.  **Proportional Change**: The assumption dictates that a unit change in an independent variable ($X_i$) will result in a **constant and proportional** change in the dependent variable ($Y$), regardless of the current value of $X_i$ or other variables.

3.  **Model Simplicity and Interpretability**:
    * **Simplicity**: The model is computationally simple because it only needs to estimate a finite set of parameters.
    * **Interpretability**: The relationship is easy to understand. The coefficient $\beta_i$ directly quantifies the *strength and direction* of the effect of $X_i$ on $Y$.

4.  **Risk of Misspecification**: The main risk is that the **true relationship** in the data is actually non-linear (e.g., curved, exponential, or S-shaped). If you apply a linear model to non-linear data, the model will **underfit** the data, leading to biased parameter estimates and poor predictive performance.

### Example Parametric Methods

* **Linear Regression**: Assumes a direct linear relationship for predicting a continuous outcome.
* **Logistic Regression**: Assumes a linear relationship between the log-odds (a transformation of the probability) of the dependent variable and the independent variables for a classification task.

Parametric methods, like linear regression, are efficient and work very well when the linearity assumption holds. When it doesn't, other techniques—like **non-parametric methods** (e.g., Decision Trees, K-Nearest Neighbors), which do *not* assume a fixed functional form—or techniques like **polynomial regression** (which transforms the features to capture curves within a linear model framework) are often preferred. 
