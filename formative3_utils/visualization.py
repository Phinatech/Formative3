"""
Visualization Module

Authors: James Mukunzi & Ryan (Shared)
Purpose: Visualization functions for optimization and analysis
"""


def plot_convergence(history, title="Gradient Descent Convergence"):
    """
    Plot the convergence of gradient descent over iterations.
    
    Parameters
    ----------
    history : list
        List of (x, f(x)) tuples from optimization history
    title : str, optional
        Plot title
    
    Returns
    -------
    matplotlib.figure.Figure
        The created figure showing convergence
    
    TODO: Ryan - Implement convergence plot
    Note: Should show function value vs iteration number
    """
    raise NotImplementedError("plot_convergence needs to be implemented")


def compare_methods(manual_history, scipy_result, title="Method Comparison"):
    """
    Create visualization comparing manual and scipy optimization methods.
    
    Parameters
    ----------
    manual_history : list
        History from manual gradient descent
    scipy_result : dict
        Results from scipy optimization
    title : str, optional
        Plot title
    
    Returns
    -------
    matplotlib.figure.Figure
        The created comparison figure
    
    TODO: Ryan - Implement method comparison visualization
    Note: Should show side-by-side or overlaid comparison
    """
    raise NotImplementedError("compare_methods needs to be implemented")
