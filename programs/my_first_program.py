# Nada Program to calculate Linear Regression using its Formula
from nada_dsl import *

def nada_main():

    # Define the party
    party1 = Party(name="Party1")

    # Define the input secret integers
    sum_x = SecretInteger(Input(name="sum_x", party=party1))  # Sum of x values
    sum_y = SecretInteger(Input(name="sum_y", party=party1))  # Sum of y values
    sum_x_squared = sum_x ** Integer(2)  # Sum of x^2 values
    sum_xy = sum_x * sum_y  # Sum of x*y values
    n = Integer(5)  # Number of data points

    # Initialize coefficients for linear regression
    slope = Integer(0)
    intercept = Integer(0)

    # Calculate the slope (m) and intercept (c) using the formulas:
    # m = (n*sum_xy - sum_x*sum_y) / (n*sum_x_squared - sum_x^2)
    # c = (sum_y - m*sum_x) / n

    # Step 1: Calculate the numerator and denominator for the slope
    numerator = (n * sum_xy) - (sum_x * sum_y)
    denominator = (n * sum_x_squared) - (sum_x * sum_x)

    # Step 2: Calculate the slope
    slope = numerator / denominator

    # Step 3: Calculate the intercept
    intercept = (sum_y - (slope * sum_x)) / n

    # Define an example x value for prediction
    example_x = SecretInteger(Input(name="example_x", party=party1))

    # Calculate the predicted y value using the linear regression equation: y = mx + c
    predicted_y = (slope * example_x) + intercept

    # Define the outputs
    output_slope = Output(slope, "slope", party1)
    output_intercept = Output(intercept, "intercept", party1)
    output_predicted_y = Output(predicted_y, "predicted_y", party1)

    return [output_slope, output_intercept, output_predicted_y]
