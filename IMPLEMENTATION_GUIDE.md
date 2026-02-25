# Formative 3 Implementation Guide

## Overview

This guide explains the module structure and what each team member needs to implement.

## Module Structure

All implementation code goes in the `formative3_utils/` package. The notebook (`Formative3_Notebook.ipynb`) is a **template** that calls your functions and displays results.

```
Formative3/
├── formative3_utils/
│   ├── __init__.py              # Package initialization
│   ├── distribution.py          # James Mukunzi
│   ├── bayesian.py              # Favor
│   ├── manual_calculator.py     # Chinemerem (Lead) + All
│   ├── gradient_descent.py      # Ryan
│   ├── data_loading.py          # James & Favor (shared)
│   └── visualization.py         # James & Ryan (shared)
├── manual_calculations/
│   └── Part3_Manual_Gradient_Descent.pdf  # Handwritten work
├── Formative3_Notebook.ipynb    # Main notebook (template)
└── IMPLEMENTATION_GUIDE.md      # This file
```

## What Each Person Implements

### James Mukunzi (Part 1: Probability Distributions)

**File: `formative3_utils/distribution.py`**

1. `compute_bivariate_pdf(x, y, mu_x, mu_y, sigma_x, sigma_y, rho)`
   - Calculate bivariate normal PDF values
   - Use the formula: f(x,y) = ...
   - Return: array of PDF values

2. `create_contour_plot(x, y, pdf_values, title)`
   - Create contour plot of the distribution
   - Show data points overlaid
   - Return: matplotlib figure

3. `create_3d_plot(x, y, pdf_values, title)`
   - Create 3D surface plot
   - Return: matplotlib figure

4. `compute_distribution_parameters(data_x, data_y)`
   - Compute means, std devs, correlation from data
   - Return: dict with parameters

**File: `formative3_utils/data_loading.py` (shared)**

5. `load_education_data(filepath)`
   - Load Education in Africa dataset
   - Handle missing values
   - Return: pandas DataFrame

### Favor (Part 2: Bayesian Probability)

**File: `formative3_utils/bayesian.py`**

1. `calculate_prior(data, sentiment)`
   - Calculate P(positive) or P(negative)
   - Return: float probability

2. `calculate_likelihood(data, keyword, sentiment)`
   - Calculate P(keyword | sentiment)
   - Return: float probability

3. `calculate_marginal(likelihood_pos, prior_pos, likelihood_neg, prior_neg)`
   - Calculate P(keyword)
   - Return: float probability

4. `calculate_posterior(likelihood, prior, marginal)`
   - Apply Bayes' Theorem
   - Return: float probability

5. `analyze_keywords(reviews_data, keywords_list)`
   - Complete analysis pipeline
   - Return: dict of results

**File: `formative3_utils/data_loading.py` (shared)**

6. `load_imdb_data(filepath)`
   - Load IMDb reviews dataset
   - Preprocess text
   - Return: pandas DataFrame

### Chinemerem (Lead) + All Team Members (Part 3: Manual Calculations)

**File: `formative3_utils/manual_calculator.py`**

1. `verify_gradient_calculation(func, grad_func, x0, epsilon)`
   - Verify analytical gradient vs numerical
   - Compare manual calculations with code
   - Return: dict with comparison results

**File: `manual_calculations/Part3_Manual_Gradient_Descent.pdf`**

2. **Handwritten calculations** (scan and save as PDF):
   - Choose initial point and learning rate
   - Perform 3+ iterations of gradient descent by hand
   - Show all work: gradients, updates, function values
   - Apply chain rule where needed
   - **This is required!**

### Ryan (Part 4: Gradient Descent in Code)

**File: `formative3_utils/gradient_descent.py`**

1. `gradient_descent(func, grad_func, x0, learning_rate, max_iterations, tolerance)`
   - Implement gradient descent from scratch
   - Track path and values at each iteration
   - Return: dict with results and history

2. `scipy_optimize(func, grad_func, x0, method)`
   - Wrapper for scipy.optimize.minimize
   - Return: dict with results

3. `compare_with_manual(manual_result, scipy_result)`
   - Compare two optimization results
   - Return: dict with comparison metrics

**File: `formative3_utils/visualization.py` (shared)**

4. `plot_convergence(history, title)`
   - Plot function value vs iteration
   - Show convergence behavior
   - Return: matplotlib figure

5. `compare_methods(manual_history, scipy_result, title)`
   - Side-by-side comparison visualization
   - Return: matplotlib figure

## Workflow

### Step 1: Implement Your Functions

Each person implements their assigned functions in the appropriate module file. All function stubs are already created with:
- Clear docstrings
- Parameter descriptions
- Return value descriptions
- TODO comments with your name

### Step 2: Test Independently

Test your functions separately before running the notebook:

```python
# Example: Test James's functions
from formative3_utils.distribution import compute_bivariate_pdf
import numpy as np

x = np.linspace(-3, 3, 50)
y = np.linspace(-3, 3, 50)
X, Y = np.meshgrid(x, y)

pdf = compute_bivariate_pdf(X, Y, 0, 0, 1, 1, 0)
print(f"PDF computed: {pdf.shape}")
```

### Step 3: Run the Notebook

Once your functions are implemented, run `Formative3_Notebook.ipynb`. The notebook will:
- Import your functions
- Call them with appropriate data
- Display results
- Provide structure for analysis

### Step 4: Add Analysis

Fill in the "TODO" sections in the notebook with your interpretations and insights.

## Tips

### For Everyone

- **Read the docstrings carefully** - they explain what each function should do
- **Test incrementally** - don't wait until everything is done
- **Use print statements** - debug by printing intermediate values
- **Check data types** - make sure you're returning the right type (array, dict, figure, etc.)

### For James (Distribution)

- The bivariate normal PDF formula is in the notebook
- Use `np.meshgrid` for creating coordinate grids
- `matplotlib.pyplot.contour()` for contour plots
- `mpl_toolkits.mplot3d.Axes3D` for 3D plots

### For Favor (Bayesian)

- Prior = count / total
- Likelihood = conditional count / condition total
- Marginal = sum of (likelihood × prior) for all cases
- Posterior = (likelihood × prior) / marginal
- Use `.str.contains()` for keyword detection

### For Chinemerem/All (Manual)

- **Handwritten work is required!**
- Show every step clearly
- Use the same initial values in code verification
- Numerical differentiation: (f(x+ε) - f(x-ε)) / (2ε)

### For Ryan (Gradient Descent)

- Store path: `path.append(current_point.copy())`
- Convergence check: `if np.linalg.norm(gradient) < tolerance: break`
- Learning rate is critical - too large = divergence, too small = slow
- For scipy: `scipy.optimize.minimize(func, x0, jac=grad_func, method='BFGS')`

## Common Issues

### Import Errors

If you get `ModuleNotFoundError`, make sure:
1. You're running from the `Formative3/` directory
2. The `formative3_utils/` folder exists
3. `__init__.py` exists in `formative3_utils/`

### NotImplementedError

This means the function stub hasn't been implemented yet. Replace `raise NotImplementedError(...)` with your actual implementation.

### Data Loading Issues

Make sure your data files are in the correct location:
- `data/education_africa.csv`
- `data/imdb_reviews.csv`

## Collaboration

### Shared Files

**`data_loading.py`** (James & Favor):
- James implements `load_education_data()`
- Favor implements `load_imdb_data()`
- Don't modify each other's functions

**`visualization.py`** (James & Ryan):
- James may add distribution-specific plots
- Ryan implements convergence plots
- Keep functions separate

### Communication

- Coordinate on shared files to avoid conflicts
- Test your functions before committing
- Document any changes to function signatures
- Help each other debug!

## Questions?

If you're unsure about:
- **What to implement**: Check the function docstring
- **How to implement**: Look at the notebook to see how it's called
- **Expected output**: Check the return type in the docstring
- **Testing**: Create a simple test case with known output

## Final Checklist

Before submission, ensure:

- [ ] All functions implemented (no `NotImplementedError`)
- [ ] Functions return correct types (array, dict, figure, etc.)
- [ ] Notebook runs without errors
- [ ] All cells show output
- [ ] Analysis sections filled in (TODO items)
- [ ] Manual calculations PDF created and saved
- [ ] Code matches manual calculations (Part 3 vs Part 4)
- [ ] Visualizations display correctly
- [ ] Team member names in docstrings

Good luck! 🚀
