import regression
import getData

(x, y) = getData.getData()
(beta0, beta1) = regression.getRegressionCoefficients(x, y)
print("beta0 is: " + str(beta0))
print("beta1 is: " + str(beta1))
regression.plotRegressionGraph(x, y, beta0, beta1)
