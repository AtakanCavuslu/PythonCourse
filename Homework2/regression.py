import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

# Function to get beta0 and beta1 values of simple linear regression
def getRegressionCoefficients(x, y):

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
def plotRegressionGraph(x, y, beta):
    # Plot the data points
    pyplot.scatter(x, y, color = "b", marker = "o", s = 30)
    # Get the estimated values
    yEstimate = beta[0] + beta[1]*x
    # Plot the regression line
    pyplot.plot(x, yEstimate, color = "r")
    pyplot.xlabel('x')
    pyplot.ylabel('y')
    plt.show()
