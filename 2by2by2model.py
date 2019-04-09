from Useful import *

Q = [[10, 3], [2, 4]]

numInputs = len(Q[0])
numOutputs = len(Q)

numTrials = 100
numTests = 1
test_samples = createQTests(numTrials, numTests, numInputs, numOutputs, Q, 1)

if __name__ == "__main__":

	#'''
	w = [
		[[1, 3], [2, 4]],
		[[1, 3], [2, 4]],
		  ]
	#'''

	# need plus 1 for input layer, should always be greater equal to 2
	numLayers = len(w) + 1
	output_Vals = [[] for i in range(numOutputs)]
	yVals = [[] for i in range(numOutputs)]

	for i in range(numTrials):
		a = [[0 for j in range(len(w[k]))] for k in range(numLayers-1)]
		# a.insert(0, [0])
		test_case = test_samples[i][0]
		a.insert(0, test_case[0])
		da = copy.deepcopy(a)
		dw = copy.deepcopy(w)

		y = test_case[1] # labels

		a = compute_output(w, a, numLayers-1)

		# iterate through all the edges in the last layer
		# dw[numLayers-1][0][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][0][1] = 2 * (a[2][0] - y[0]) * a[1][1]
		#
		# dw[numLayers-1][1][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][1][1] = 2 * (a[2][0] - y[0]) * a[1][1]

		# For last layer
		for i1 in range(numOutputs):
			for i2 in range(len(w[numLayers - 2])):
				# I am computing the change in the cost function with respect to the weight of the edge
				# going from node i2 in the second last layer to node i1 in the last layer
				dw[numLayers - 2][i1][i2] = 2 * (a[numLayers - 1][i1] - y[i1]) * a[numLayers - 2][i2]

		# da[1][0] = (dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0])
		# da[1][1] = (dw[1][0][1] / a[1][1] * w[1][0][1] + dw[1][1][1] / a[1][1] * w[1][1][1])
		#
		# dw[0][0][0] = da[1][0] * a[0][0]
		# dw[0][1][0] = da[1][1] * a[0][0]
		#
		# dw[0][0][1] = da[1][0] * a[0][1]
		# dw[0][1][1] = da[1][1] * a[0][1]

		total_cost = compute_cost(a, numLayers - 1, numOutputs, y)
		c = - 1 / 10
		for i1 in range(0, len(w)):
			for i2 in range(0, len(w[i1])):
				for i3 in range(0, len(w[i1][i2])):
					w[i1][i2][i3] += c * dw[i1][i2][i3]

		xVals.append(i)
		costVals.append(total_cost)
		for q in range(0, numOutputs):
			output_Vals[q].append(a[numLayers-1][q])
		for q in range(0, numOutputs):
			yVals[q].append(y[q])

	print("w " + str(w))
	for i in range(numOutputs):
		pylab.subplot((numOutputs + 1) * 100 + 11 + i)
		pylab.plot(xVals, yVals[i], 'b--', label="yVals[{}]".format(i))
		pylab.plot(xVals, output_Vals[i], 'r.', label="output_Vals[{}]".format(i))
		pylab.legend()

	pylab.subplot((numOutputs + 1) * 100 + 11 + numOutputs)
	pylab.plot(xVals, costVals, 'g--')
	pylab.show()