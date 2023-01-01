import pandas as pd


def evaluate_model(validation_data: pd.DataFrame, data: pd.DataFrame):
    # Make predictions, compare to actual values and return Evaluation Data
    raise NotImplementedError


def use_model(data: pd.DataFrame, probability_tables: list[pd.DataFrame]):
    # Make Predictions based on Probability Tables and given data
    raise NotImplementedError
