
from Useful import *

# generating test samples
numLayers = 2
numSamples = 1000
test_samples = [random.random() for i in range(numSamples)]
test_labels = [test_samples[i] * math.pi for i in range(numSamples)]
if __name__ == "__main__":

    # '''
    w = [random.random() for i in range(numLayers)]

    # book keeping
    xVals = []
    yVals = [[] for i in range(numLayers)]

    for i in range(numSamples):

        a = [0 for v in range(numLayers+1)]
        d = [0 for v in range(numLayers)]

        a[0]  = test_samples[i]

        for k in range(0, numLayers):
            a[k+1] = w[k] * a[k]

        y = test_labels[i]

        d[numLayers-1] = a[numLayers-1] * 2 * (a[numLayers] - y)

        for j in range(numLayers-2, -1, -1):
            d[j] = a[j] * w[j+1] / a[j+1] *  d[j+1]

        for m in range(numLayers):
            w[m] -= d[m] / 100

        xVals.append(i)
        for q in range(numLayers):
            yVals[q].append(w[q])

    for i in range(len(yVals)):
        pylab.plot(xVals, yVals[i], 'b--')

    pylab.show()
    t = 1
    for j in range(numLayers):
        t *= w[j]
    print(t)

    # '''
