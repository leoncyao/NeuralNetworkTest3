
from Useful import *

# generating test samples
numLayers = 1
# numSamples = 1000
numTrials = 100
numTests = 1
# test_samples = [random.random() for i in range(numSamples)]

# lol i don't really need these
Q = [[1, 3], [4, 2]]
# Q = [[math.pi]]
# Will need to change this later. numInputs should be the
# number of columns of the first matrix
numInputs = len(Q[0])
numOutputs = len(Q)
test_samples = createQTests(numTrials, numTests, numInputs, numOutputs, Q, 1)
# test_labels = [test_samples[i] * math.pi for i in range(numSamples)]


def compute_output(matrix, activations, num_layers):
    for num_layer in range(0, num_layers):
        # a[k+1] = w[k] * a[k]
        a[num_layer + 1] = MVM(w, a[num_layer])
    return a

def compute_cost(activations, num_layers, num_outputs):
    tc = 0
    for o1 in range(0, num_outputs):
        tc += pow(activations[num_layers][o1]- y[o1], 2)
        # can change cost function later
    return tc
if __name__ == "__main__":

    # '''
    # w = [random.random() for i in range(numLayers)]
    # w = list(Q)
    # w = [[0, 0], [0, 0]]
    # w = [[0 for i2 in range(numOutputs)] for i1 in range(numInputs)]
    w = [[random.random() for i2 in range(numOutputs)] for i1 in range(numInputs)]

    # book keeping
    xVals = []
    yVals = [[] for i in range(numOutputs)]
    costVals = []
    output_Vals = [[] for i in range(numOutputs)]
    for i in range(numTrials):
        a = [[0] for v in range(numLayers + 1)]
        d = [[0 for v2 in range(numOutputs)] for v1 in range(numInputs)]

        test_case = test_samples[i][0]
        # test_input = test_case[0][0]

        a[0]  = test_case[0]

        a = compute_output(w, a, numLayers)

        # for k in range(0, numLayers):
        #     # a[k+1] = w[k] * a[k]
        #     a[k+1] = MVM(w, a[k])

        y = test_case[1]

        # total_cost = 0
        # for o in range(numOutputs):
        #     total_cost += pow((a[1][o] - y[o]), 2)

        total_cost = compute_cost(a, numLayers, numOutputs)

        # this works for the last layer ONLY
        for s1 in range(numInputs):
            for s2 in range(numOutputs):
                d[s1][s2] = a[numLayers-1][s1] * 2 * (a[numLayers][s2] - y[s2])

        # however backpropogating will need more calculations, ie to calculate the
        # change in the cost over an activation not in the last layer, will need to do
        # a sum over the nodes it affects in the next layer

        # for j in range(numLayers-2, -1, -1):
        #     for s1 in range(numInputs): # assuming a square network
        #         for s2 in range(numOutputs): # assuming a square network
        #             for s3 in range(numOutputs):
                        # sum over the changes in cost of the nodes in the next layer it affects,
                        # multiply by the activation of node?
                        # this is for the edge d[j][s1][s2]
                # d[j][s1][s2] = ...

        # computing d, the gradient vector
        # d[numLayers-1] = a[numLayers-1] * 2 * (a[numLayers] - y)
        # for j in range(numLayers-2, -1, -1):
        #     d[j] = a[j] * w[j+1] / a[j+1] *  d[j+1]

        c = - 1 / 100

        # w = MMA([w], SMM(c, [d]))[0]
        new_w = MMA([w], SMM(c, [d]))[0]
        new_a = [[0] for v in range(numLayers + 1)]

        new_a[0]  = test_case[0]

        for k in range(0, numLayers):
            # a[k+1] = w[k] * a[k]
            new_a[k+1] = MVM(new_w, new_a[k])

        # new_total_cost = 0
        # for o in range(0, numOutputs):
        #     new_total_cost += pow((new_a[1][o] - y[o]), 2)

        new_total_cost = compute_cost(new_a, numLayers, numOutputs)


        # note that i only compute one test per time, later should average

        k1 = 1 - total_cost/(total_cost + new_total_cost)
        k2 = total_cost/(total_cost + new_total_cost)

        w = MMA(SMM(k1, [w]), SMM(k2, [new_w]))[0]

        # can first check to see if adding the gradient decreases total cost
        # it may be the case that we overshoot, in which case,
        # it will be better to take a weight of the average of w and new_w


        # book keeping
        xVals.append(i)
        costVals.append(total_cost)
        for q in range(0, numOutputs):
            output_Vals[q].append(a[1][q])
        for q in range(0, numOutputs):
            yVals[q].append(y[q])




    matrixPrinter([w])

    for i in range(numOutputs):
        pylab.subplot((numOutputs + 1) * 100 + 11 + i)
        pylab.plot(xVals, yVals[i], 'b--', label="yVals[{}]".format(i))
        pylab.plot(xVals, output_Vals[i], 'b.', label="output_Vals[{}]".format(i))
        pylab.legend()
    pylab.subplot((numOutputs + 1) * 100 + 11 + numOutputs)
    pylab.plot(xVals, costVals, 'g--')
    pylab.show()

    # checking the product
    # t = 1
    # for j in range(numLayers):
    #     t *= w[j]
    # print(t)

    # '''
