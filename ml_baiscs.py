import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def load_data(file_path):
    dataset = pd.read_csv("/home/pooja/Downloads/Salary Data.csv")
    return dataset

def split_data(dataset, test_size=0.2, random_state=42):
    """
    Split the dataset into training and testing sets.
    """
    X = dataset[['YearsExperience']].values  # Independent variable (reshape to 2D if necessary)
    y = dataset['Salary'].values    # Dependent variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train):
    """
    Train the linear regression model using the training data.
    """
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on the test data.
    """
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    print("Mean Squared Error:", mse)
    return y_pred

def plot_results(X_test, y_test, y_pred):
    """
    Plot the actual vs predicted values.
    """
    plt.scatter(X_test, y_test, color='blue', label='Actual data')  # Test data points
    plt.plot(X_test, y_pred, color='red', label='Predicted line')  # Fitted regression line
    plt.xlabel('Independent Variable (X)')
    plt.ylabel('Dependent Variable (y)')
    plt.title('Simple Linear Regression with Dataset')
    plt.legend()
    plt.show()

def main(file_path):
    """
    Main function to execute the linear regression workflow.
    """
    # Load data
    dataset = load_data(file_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = split_data(dataset)

    # Train the linear regression model
    model = train_model(X_train, y_train)

    # Print out the model parameters
    print("Slope:", model.coef_)
    print("Intercept:", model.intercept_)

    # Evaluate the model
    y_pred = evaluate_model(model, X_test, y_test)

    # Plot the results
    plot_results(X_test, y_test, y_pred)

# Run the main function with your dataset file path
file_path = 'your_dataset.csv'  # Replace with your actual dataset path
main(file_path)
