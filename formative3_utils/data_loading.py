"""
Data Loading Module

Authors: James Mukunzi & Favor (Shared)
Purpose: Load and preprocess datasets for analysis
"""


def load_education_data(filepath='data/education_data.csv'):
    """
    Load and preprocess education dataset for bivariate analysis.
    
    Parameters
    ----------
    filepath : str, optional
        Path to the education data CSV file
    
    Returns
    -------
    pandas.DataFrame
        Preprocessed education data with relevant columns
    
    TODO: James Mukunzi - Implement education data loading
    Note: Should handle missing values and basic preprocessing
    """
    raise NotImplementedError("load_education_data needs to be implemented")


def load_imdb_data(filepath='data/imdb_reviews.csv'):
    """
    Load and preprocess IMDB reviews dataset for Bayesian analysis.
    
    Parameters
    ----------
    filepath : str, optional
        Path to the IMDB reviews CSV file
    
    Returns
    -------
    pandas.DataFrame
        Preprocessed IMDB data with text and ratings
    
    TODO: Favor - Implement IMDB data loading
    Note: Should handle text preprocessing and rating extraction
    """
    raise NotImplementedError("load_imdb_data needs to be implemented")
