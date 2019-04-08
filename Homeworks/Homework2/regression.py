import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import math

# Function to get alpha and beta values of simple linear regression
def getRegressionResults(xList, yList):

    # Convert list to numpy arrays
    x = np.array(xList)
    y = np.array(yList)
    # To regress, least squares method is used. Formula can be found at:
    # https://en.wikipedia.org/wiki/Least_squares

    # Get the number of the observations
    n = np.size(x)
    # Get the mean values to use in the least squares formula
    xBar = np.mean(x)
    yBar = np.mean(y)
    # Get cross-deviations to use in the least squares formula
    SSxy = np.sum(y*x) - n*yBar*xBar
    SSxx = np.sum(x*x) - n*xBar*xBar
    # Calculate regression coeefficients
    beta = SSxy/SSxx
    alpha = yBar - beta*xBar

    # Get the estimated values of y
    yEstimate = alpha + beta*x

    # Calculate regression standard error of beta
    stdErrorSquared = np.sum(np.square(yEstimate - y)) / ((n-2)*np.sum(np.square(x - xBar)))
    standardError = math.sqrt(stdErrorSquared)

    # Calculate the 0.95 CI bounds for beta
    lowerBound = beta - 1.96*standardError
    upperBound = beta + 1.96*standardError

    return (alpha, beta, standardError, lowerBound, upperBound)

# For visual aid, a function to plot the graph with regression line
def plotRegressionGraph(xList, yList, alpha, beta):
    # Plot the data points
    x = np.array(xList)
    y = np.array(yList)
    pyplot.scatter(x, y, color = "b", marker = "o", s = 30)
    # Get the estimated values
    yEstimate = alpha + beta*x
    # Plot the regression line
    pyplot.plot(x, yEstimate, color = "r")
    pyplot.xlabel('GDP Per Capita (Current US$)')
    pyplot.ylabel('Urban population (% of total)')
    pyplot.show()
