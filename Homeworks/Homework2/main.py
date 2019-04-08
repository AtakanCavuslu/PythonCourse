import regression
import getData
import numpy as np

(xList, yList) = getData.getData()

# Feature scaling GDP data to achieve meaningful resulsts
xArray = np.array(xList)
xMin = np.amin(xArray)
xMax = np.amax(xArray)
xScaled = (xArray - xMin) / (xMax - xMin)
x = xScaled.tolist()

# Converting percent values to decimals for urban population ratio - Normalizing
yArray = np.array(yList)
yNormalized = yArray / 100
y = yNormalized.tolist()

(alpha, beta, standardError, lowerBound, upperBound) = regression.getRegressionResults(x, y)
print("With given format of Y = alpha + beta*X")
print("Alpha value is: " + str(alpha))
print("Beta value is: " + str(beta))
print("Standard error is: " + str(standardError))
print("95% Confidence interval for beta: " + str(lowerBound) + " - " + str(upperBound))
regression.plotRegressionGraph(x, y, alpha, beta)

# Getting statistical values - std error etc
