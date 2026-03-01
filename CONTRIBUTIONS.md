# Team Contributions - Formative 3

This document outlines the responsibilities and contributions of each team member for Formative 3: Probability Distributions, Bayesian Probability, and Gradient Descent.

---

## Team Members & Responsibilities

### James Mukunzi - Part 1: Probability Distributions (Bivariate Normal Distribution)

**Branch:** `james/part1-probability-distributions`

**Dataset:** Education in Africa  
Source: https://www.kaggle.com/datasets/lydia70/education-in-africa?select=Education+in+General.csv

**Responsibilities:**
- Implement `distribution.py` module with bivariate normal distribution functions
- Compute PDF (Probability Density Function) values from scratch without using `scipy.stats`
- Select two continuous variables from the Education in Africa dataset
- Calculate mean vector and covariance matrix
- Create visualizations:
  - Contour plot showing probability density
  - 3D surface plot of the bivariate normal distribution
- Document mathematical formulas and implementation details

**Key Deliverables:**
- `distribution.py` with manual PDF computation
- Visualization functions for contour and 3D plots
- Analysis of the bivariate relationship between selected variables

---

### Favor - Part 2: Bayesian Probability

**Branch:** `favor/part2-bayesian-probability`

**Dataset:** IMDb Movie Reviews

**Responsibilities:**
- Implement `bayesian.py` module for Bayesian probability calculations
- Select relevant keywords from movie reviews (e.g., "excellent", "terrible", "boring")
- Compute prior probabilities P(positive) and P(negative)
- Calculate likelihoods P(keyword | positive) and P(keyword | negative)
- Apply Bayes' Theorem to compute posterior probabilities
- Analyze how keyword presence affects sentiment classification

**Key Deliverables:**
- `bayesian.py` with Bayes' Theorem implementation
- Keyword selection and probability calculations
- Analysis of posterior probabilities for sentiment prediction

---

### Chinemerem (Lead) - Part 3: Gradient Descent Manual Calculation

**Branch:** `chinemerem/part3-manual-gradient-descent`

**Note:** All team members contribute to this part

**Responsibilities:**
- Lead the manual gradient descent calculation (handwritten component)
- Implement `manual_calculator.py` module to verify handwritten calculations
- Define a simple loss function (e.g., Mean Squared Error)
- Show explicit chain rule steps for gradient computation
- Perform manual gradient descent iterations (at least 3 steps)
- Document each calculation step clearly

**Key Deliverables:**
- Handwritten gradient descent calculations (scanned/photographed)
- Clear documentation of chain rule application
- Step-by-step gradient descent iterations

**Team Collaboration:**
- All members should review and understand the manual calculations
- Each member contributes to verifying the mathematical steps

---

### Ryan - Part 4: Gradient Descent in Code

**Branch:** `ryan/part4-coded-gradient-descent`

**Responsibilities:**
- Implement `gradient_descent.py` module with automated gradient descent
- Use SciPy's optimization functions (e.g., `scipy.optimize.minimize`)
- Implement gradient descent from scratch for comparison
- Create convergence visualizations:
  - Loss vs. iteration plot
  - Parameter trajectory visualization
- Compare manual implementation with SciPy's optimized version
- Document performance and convergence behavior

**Key Deliverables:**
- `gradient_descent.py` with both manual and SciPy implementations
- Convergence visualizations
- Performance comparison analysis

---

## Shared Responsibilities

### Utility Modules

**`data_loading.py`**
- Owner: Whoever needs it first (likely James or Favor)
- Load and preprocess datasets
- Handle missing values and data cleaning
- Provide consistent data access interface

**`visualization.py`**
- Owner: Whoever needs it first (likely James)
- Shared visualization utilities
- Consistent plotting style across all parts
- Helper functions for common plot types

### Final Integration

**Jupyter Notebook Integration**
- Responsibility: All team members
- Integrate all four parts into a cohesive notebook
- Ensure smooth narrative flow between sections
- Add markdown explanations and interpretations
- Review and test the complete notebook

**Code Review**
- All members review each other's pull requests
- Ensure code quality and consistency
- Verify mathematical correctness
- Test functionality before merging

---

## Git Workflow

1. Each member works on their designated branch
2. Commit regularly with clear, descriptive messages
3. Create pull requests when ready for review
4. At least one other team member reviews before merging
5. Merge to `main` branch after approval
6. Pull latest changes before starting new work

---

## Communication

- Regular check-ins to discuss progress
- Share challenges and solutions
- Coordinate on shared modules
- Review each other's work for learning and quality assurance

---

## Timeline Expectations

- Complete individual parts before integration
- Allow time for code review and revisions
- Schedule final integration session with all members
- Test complete notebook before submission
