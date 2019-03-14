import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

# Function to get beta0 and beta1 values of simple linear regression
def getRegressionCoefficients(xList, yList):

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
    beta1 = SSxy/SSxx
    beta0 = yBar - beta1*xBar

    return (beta0, beta1)

# For visual aid, a function to plot the graph with regression line
def plotRegressionGraph(xList, yList, beta0, beta1):
    # Plot the data points
    x = np.array(xList)
    y = np.array(yList)
    pyplot.scatter(x, y, color = "b", marker = "o", s = 30)
    # Get the estimated values
    yEstimate = beta0 + beta1*x
    # Plot the regression line
    pyplot.plot(x, yEstimate, color = "r")
    pyplot.xlabel('GDP Per Capita (Current US$)')
    pyplot.ylabel('Urban population (% of total)')
    pyplot.show()
