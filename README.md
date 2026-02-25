# Formative 3: Probability Distributions, Bayesian Probability, and Gradient Descent

A comprehensive exploration of probability theory and optimization techniques through practical implementation and analysis.

---

## Team Members

- **James Mukunzi** - Part 1: Probability Distributions (Bivariate Normal Distribution)
- **Favor** - Part 2: Bayesian Probability
- **Chinemerem** (Lead) - Part 3: Gradient Descent Manual Calculation
- **Ryan** - Part 4: Gradient Descent in Code

See [CONTRIBUTIONS.md](CONTRIBUTIONS.md) for detailed responsibilities.

---

## Quick Start Guide

**For Team Members:**

1. **Clone the repository** and create your feature branch
2. **Install dependencies:** `pip install -r requirements.txt`
3. **Implement your assigned functions** in `formative3_utils/`
4. **Test your functions** independently before integrating
5. **Update the notebook** to call your functions
6. **Run the notebook** to verify everything works
7. **Create a Pull Request** for review

**Your Implementation Checklist:**
- [ ] James: Implement `distribution.py` and education data loading
- [ ] Favor: Implement `bayesian.py` and IMDb data loading
- [ ] Chinemerem/All: Complete handwritten calculations and save PDF
- [ ] Ryan: Implement `gradient_descent.py` and visualization functions
- [ ] All: Test notebook runs without errors
- [ ] All: Generate `CONTRIBUTIONS.pdf`

---

## Project Overview

This project consists of four interconnected parts exploring fundamental concepts in probability and optimization:

1. **Bivariate Normal Distribution**: Analyze relationships between variables using probability density functions
2. **Bayesian Probability**: Apply Bayes' Theorem to sentiment analysis of movie reviews
3. **Manual Gradient Descent**: Perform gradient descent calculations by hand to understand the mathematics
4. **Coded Gradient Descent**: Implement and optimize gradient descent algorithms in Python

### Team Structure and Responsibilities

This is a **collaborative project** where each team member has specific responsibilities:

#### James Mukunzi - Part 1: Probability Distributions
**Implements in `formative3_utils/`:**
- `distribution.py` - Bivariate normal distribution functions
- `data_loading.py` (shared) - Education dataset loading
- `visualization.py` (shared) - Distribution visualization functions

**Deliverables:**
- Bivariate normal PDF computation (no scipy.stats)
- Contour and 3D visualizations
- Analysis of variable relationships

#### Favor - Part 2: Bayesian Probability
**Implements in `formative3_utils/`:**
- `bayesian.py` - Bayesian probability calculations
- `data_loading.py` (shared) - IMDb dataset loading

**Deliverables:**
- Prior, likelihood, marginal, and posterior probability calculations
- Keyword-based sentiment analysis
- Bayes' Theorem application (no sklearn/nltk)

#### Chinemerem (Lead) - Part 3: Manual Gradient Descent
**All team members contribute to this part**

**Implements in `formative3_utils/`:**
- `manual_calculator.py` - Verification functions

**Deliverables:**
- Handwritten gradient descent calculations (REQUIRED PDF)
- Chain rule application with all steps shown
- At least 3 iterations documented
- Code verification of manual calculations

#### Ryan - Part 4: Coded Gradient Descent
**Implements in `formative3_utils/`:**
- `gradient_descent.py` - Gradient descent implementations
- `visualization.py` (shared) - Convergence visualization functions

**Deliverables:**
- Manual gradient descent implementation
- SciPy optimization wrapper
- Convergence visualizations
- Comparison with manual calculations

#### Shared Responsibilities (All Team Members)
- `formative3_utils/__init__.py` - Package initialization
- Code review and testing
- Jupyter Notebook integration
- Documentation and README updates
- Final submission preparation

---

## Submission Artifacts

This project includes the following submission artifacts:

### Required Files for Submission

1. **GitHub Repository** - This repository with all code and documentation
2. **Jupyter Notebook** - `Formative3_Notebook.ipynb` (PRIMARY DELIVERABLE - must show all outputs)
3. **PDF: Handwritten Manual Calculations** - `manual_calculations/Part3_Manual_Gradient_Descent.pdf`
   - ⚠️ **MUST BE HANDWRITTEN** - Type or print the calculations, then write them by hand
   - Must show all steps for at least 3 iterations of gradient descent
   - Must include chain rule application with no skipped steps
   - Use initial conditions: m=-1, b=1, α=0.1, points (1,3) and (3,6)
   - Scan or photograph your work and save as PDF
4. **PDF: Team Contributions** - `CONTRIBUTIONS.pdf`
   - Shows what each team member contributed to the project
   - Can be generated from `CONTRIBUTIONS.md` using pandoc or online converters

---

## Directory Structure

```
Formative3/
├── README.md                      # This file - project documentation
├── CONTRIBUTIONS.md               # Team member responsibilities (source)
├── CONTRIBUTIONS.pdf              # ⚠️ REQUIRED: Team contributions PDF for submission
├── Formative3_Notebook.ipynb      # ⚠️ PRIMARY DELIVERABLE: Main Jupyter notebook
├── data/                          # Datasets
│   ├── education_africa.csv       # Education in Africa dataset (James)
│   └── imdb_reviews.csv           # IMDb movie reviews dataset (Favor)
├── formative3_utils/              # Core utility package (modular code)
│   ├── __init__.py                # Package initialization
│   ├── distribution.py            # Part 1: Bivariate normal distribution (James)
│   ├── bayesian.py                # Part 2: Bayesian probability (Favor)
│   ├── manual_calculator.py       # Part 3: Manual gradient descent verification (All)
│   ├── gradient_descent.py        # Part 4: Coded gradient descent (Ryan)
│   ├── data_loading.py            # Shared: Data loading utilities (James & Favor)
│   └── visualization.py           # Shared: Visualization utilities (James & Ryan)
├── manual_calculations/           # Handwritten work for Part 3
│   └── Part3_Manual_Gradient_Descent.pdf  # ⚠️ REQUIRED: Handwritten calculations
└── requirements.txt               # Python dependencies
```

### Important Notes on Directory Structure

- **formative3_utils/** - All team members implement their functions here (NOT in "modules/")
- **manual_calculations/** - Create this directory and place your handwritten PDF here
- **CONTRIBUTIONS.pdf** - Must be present in the root directory for submission

### How to Generate CONTRIBUTIONS.pdf

You can generate `CONTRIBUTIONS.pdf` from `CONTRIBUTIONS.md` using one of these methods:

**Option 1: Using Pandoc (Recommended)**
```bash
pandoc CONTRIBUTIONS.md -o CONTRIBUTIONS.pdf
```

**Option 2: Using Jupyter Notebook**
1. Open `CONTRIBUTIONS.md` in Jupyter
2. File → Download as → PDF

**Option 3: Online Converters**
- Use any markdown-to-PDF online converter
- Upload `CONTRIBUTIONS.md` and download the PDF

**Option 4: Print to PDF**
1. Open `CONTRIBUTIONS.md` in a markdown viewer
2. Use your browser's "Print to PDF" feature

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Git

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd Formative3
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download datasets:**
   - Education in Africa: https://www.kaggle.com/datasets/lydia70/education-in-africa
   - IMDb Movie Reviews: (add specific source)
   - Place datasets in the `data/` directory

---

## Dependencies

Key Python packages required:

- `numpy` - Numerical computations
- `pandas` - Data manipulation and analysis
- `matplotlib` - Plotting and visualization
- `scipy` - Scientific computing and optimization
- `jupyter` - Interactive notebook environment
- `seaborn` - Statistical data visualization

See `requirements.txt` for complete list with versions.

---

## Git Workflow

### Branch Structure

Each team member works on their own feature branch:

- `james/part1-probability-distributions`
- `favor/part2-bayesian-probability`
- `chinemerem/part3-manual-gradient-descent`
- `ryan/part4-coded-gradient-descent`

### Workflow Steps

1. **Clone and setup:**
   ```bash
   git clone <repository-url>
   cd Formative3
   ```

2. **Create your feature branch:**
   ```bash
   git checkout -b <your-branch-name>
   ```

3. **Make changes and commit regularly:**
   ```bash
   git add .
   git commit -m "Descriptive commit message"
   ```

4. **Push your branch:**
   ```bash
   git push origin <your-branch-name>
   ```

5. **Create a Pull Request (PR):**
   - Go to the repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Add description of changes
   - Request review from team members

6. **Code Review:**
   - At least one team member reviews the PR
   - Address any feedback or requested changes
   - Approve and merge when ready

7. **Keep your branch updated:**
   ```bash
   git checkout main
   git pull origin main
   git checkout <your-branch-name>
   git merge main
   ```

---

## How to Run

### Running the Jupyter Notebook

1. **Start Jupyter:**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook:**
   - Navigate to `Formative3_Notebook.ipynb`
   - Click to open

3. **Run all cells:**
   - Click "Cell" → "Run All"
   - Or run cells individually with Shift+Enter

**IMPORTANT:** Before submitting, make sure to run all cells and save the notebook with outputs displayed!

### Testing Individual Modules

Each team member can test their module independently:

```python
# Example: Testing James's distribution module
from formative3_utils.distribution import compute_bivariate_pdf
from formative3_utils.data_loading import load_education_data
import numpy as np

# Load data
data = load_education_data('data/education_africa.csv')

# Test PDF computation
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
mu_x, mu_y = 0, 0
sigma_x, sigma_y = 1, 1
rho = 0.5
pdf_values = compute_bivariate_pdf(x, y, mu_x, mu_y, sigma_x, sigma_y, rho)
print(f"PDF values: {pdf_values}")
```

```python
# Example: Testing Favor's Bayesian module
from formative3_utils.bayesian import calculate_prior, calculate_likelihood
from formative3_utils.data_loading import load_imdb_data

# Load data
imdb_data = load_imdb_data('data/imdb_reviews.csv')

# Test probability calculations
prior = calculate_prior(imdb_data, 'positive')
likelihood = calculate_likelihood(imdb_data, 'excellent', 'positive')
print(f"Prior: {prior}, Likelihood: {likelihood}")
```

```python
# Example: Testing Ryan's gradient descent module
from formative3_utils.gradient_descent import gradient_descent
import numpy as np

# Define a simple function
def f(params):
    x, y = params
    return x**2 + y**2

def grad_f(params):
    x, y = params
    return np.array([2*x, 2*y])

# Test gradient descent
result = gradient_descent(f, grad_f, np.array([5.0, 5.0]), 
                         learning_rate=0.1, max_iterations=100)
print(f"Final point: {result['final_point']}")
print(f"Final value: {result['final_value']}")
```

---

## Dataset Sources

### Education in Africa
- **Source:** Kaggle
- **URL:** https://www.kaggle.com/datasets/lydia70/education-in-africa
- **File:** `Education in General.csv`
- **Used in:** Part 1 (Bivariate Normal Distribution)
- **Description:** Educational statistics across African countries

### IMDb Movie Reviews
- **Used in:** Part 2 (Bayesian Probability)
- **Description:** Movie reviews with sentiment labels for Bayesian analysis

---

## Project Components

### Part 1: Bivariate Normal Distribution (James)

**Module:** `formative3_utils/distribution.py`

**Functions to implement:**
- `compute_bivariate_pdf(x, y, mu_x, mu_y, sigma_x, sigma_y, rho)` - Calculate PDF values using the bivariate normal formula (NO scipy.stats)
- `create_contour_plot(X_grid, Y_grid, Z, var1_name, var2_name, data)` - Generate contour plots
- `create_3d_plot(X_grid, Y_grid, Z, var1_name, var2_name)` - Generate 3D surface plots
- `compute_distribution_parameters(data)` - Calculate mean vector, covariance matrix, correlation

**Module:** `formative3_utils/data_loading.py` (shared)
- `load_education_data(filepath)` - Load and validate Education in Africa dataset

**Key Requirements:**
- Manual PDF computation without scipy.stats
- Proper parameter validation (σx > 0, σy > 0, |ρ| ≤ 1)
- Publication-quality visualizations with labels and titles

### Part 2: Bayesian Probability (Favor)

**Module:** `formative3_utils/bayesian.py`

**Functions to implement:**
- `calculate_prior(df, sentiment)` - Calculate P(positive) or P(negative)
- `calculate_likelihood(df, keyword, sentiment)` - Calculate P(keyword|sentiment)
- `calculate_marginal(df, keyword)` - Calculate P(keyword)
- `calculate_posterior(prior, likelihood, marginal)` - Apply Bayes' Theorem
- `analyze_keywords(df, positive_keywords, negative_keywords)` - Complete analysis for multiple keywords

**Module:** `formative3_utils/data_loading.py` (shared)
- `load_imdb_data(filepath)` - Load and validate IMDb movie reviews dataset

**Key Requirements:**
- Manual Bayes' Theorem implementation (NO sklearn/nltk)
- Case-insensitive keyword matching
- Return all four probability values for each keyword
- Handle edge cases (keyword not found, zero marginal probability)

### Part 3: Manual Gradient Descent (Chinemerem - Lead, All Contribute)

**Module:** `formative3_utils/manual_calculator.py`

**Functions to implement:**
- `verify_gradient_calculation(manual_results, x0, y0, learning_rate, f, grad_f)` - Compare manual calculations with code

**Key Requirements:**
- **HANDWRITTEN CALCULATIONS REQUIRED** - Must be scanned and saved as PDF
- Use assignment-specified values: m=-1, b=1, α=0.1, points (1,3) and (3,6)
- Show chain rule application explicitly with no skipped steps
- Perform at least 3 iterations
- Document all intermediate calculations
- Save as `manual_calculations/Part3_Manual_Gradient_Descent.pdf`

### Part 4: Coded Gradient Descent (Ryan)

**Module:** `formative3_utils/gradient_descent.py`

**Functions to implement:**
- `gradient_descent(f, grad_f, initial_point, learning_rate, max_iterations, tolerance)` - Manual gradient descent with path tracking
- `scipy_optimize(f, grad_f, initial_point, method)` - Wrapper for SciPy's optimization
- `compare_with_manual(scipy_results, manual_results, tolerance)` - Compare results

**Module:** `formative3_utils/visualization.py` (shared)
- `plot_convergence(result, title)` - Visualize parameter and error evolution
- `compare_methods(results_list, method_names)` - Compare different optimization methods

**Key Requirements:**
- Track parameter history (m, b, error) across all iterations
- Use same initial conditions as Part 3 for comparison
- Generate convergence plots (3 subplots: m vs iteration, b vs iteration, error vs iteration)
- Visualize optimization path on function surface

---

## Testing

Run tests to verify implementations:

```bash
# If tests are implemented
pytest tests/
```

---

## Contributing

1. Follow the Git workflow outlined above
2. Write clear, documented code
3. Add comments explaining complex logic
4. Test your code before creating a PR
5. Review other team members' PRs
6. Communicate regularly with the team

---

## Troubleshooting

### Common Issues

**Import errors:**
- Ensure virtual environment is activated
- Reinstall dependencies: `pip install -r requirements.txt`
- Make sure you're importing from `formative3_utils` not `modules`

**Dataset not found:**
- Verify datasets are in the `data/` directory
- Check file names match those in code

**Jupyter kernel issues:**
- Restart kernel: "Kernel" → "Restart"
- Clear output: "Cell" → "All Output" → "Clear"

---

## Submission Checklist

Before submitting, verify that you have completed all requirements:

### Code and Implementation
- [ ] All code is organized in the `formative3_utils/` package (NOT `modules/`)
- [ ] Code follows DRY principle (no duplication)
- [ ] All functions are properly documented with docstrings
- [ ] Code is tested and runs without errors

### Jupyter Notebook
- [ ] `Formative3_Notebook.ipynb` executes all cells without errors
- [ ] All outputs are displayed (run "Cell" → "Run All" before submitting)
- [ ] All visualizations are generated and visible
- [ ] Markdown cells include analysis and interpretation
- [ ] Each part clearly shows team member's work

### Part 1: Bivariate Normal Distribution (James)
- [ ] Dataset loaded and explored
- [ ] Distribution parameters computed
- [ ] PDF values calculated manually (no scipy.stats)
- [ ] Contour plot generated
- [ ] 3D surface plot generated
- [ ] Analysis and interpretation included

### Part 2: Bayesian Probability (Favor)
- [ ] IMDb dataset loaded
- [ ] 2-4 keywords selected for positive sentiment
- [ ] 2-4 keywords selected for negative sentiment
- [ ] Prior probabilities calculated
- [ ] Likelihood probabilities calculated
- [ ] Marginal probabilities calculated
- [ ] Posterior probabilities calculated using Bayes' Theorem
- [ ] Results visualized
- [ ] Analysis and interpretation included

### Part 3: Manual Gradient Descent (Chinemerem - Lead, All Contribute)
- [ ] Manual calculations completed by hand
- [ ] At least 3 iterations performed
- [ ] Chain rule application shown explicitly
- [ ] All intermediate steps documented
- [ ] Handwritten work scanned/photographed
- [ ] PDF saved as `manual_calculations/Part3_Manual_Gradient_Descent.pdf`
- [ ] Calculations verified with code

### Part 4: Coded Gradient Descent (Ryan)
- [ ] Gradient descent implemented from scratch
- [ ] SciPy optimization implemented
- [ ] Same initial conditions as Part 3 used
- [ ] Parameter history tracked
- [ ] Convergence visualizations generated
- [ ] Comparison with manual calculations included
- [ ] Analysis and interpretation included

### Required Submission Files
- [ ] `Formative3_Notebook.ipynb` with all outputs displayed
- [ ] `manual_calculations/Part3_Manual_Gradient_Descent.pdf` (handwritten)
- [ ] `CONTRIBUTIONS.pdf` showing team member contributions
- [ ] GitHub repository with all code
- [ ] `README.md` (this file)
- [ ] `requirements.txt` with all dependencies

### Final Checks
- [ ] All team members have reviewed the submission
- [ ] Repository is clean (no unnecessary files)
- [ ] All file paths are correct
- [ ] Notebook runs from top to bottom without errors
- [ ] All visualizations are publication-quality
- [ ] Analysis sections are complete and thoughtful

---

## License

This project is for educational purposes as part of coursework.

---

## Contact

For questions or issues, contact team members through the course communication channels.
