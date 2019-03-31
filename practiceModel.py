from Useful import *


# Q = [[1, 3], [4, 2]]
# Q = [[42]]
Q = [[math.pi, 2.7], [1, 3]]

# Will need to change this later. numInputs should be the
# number of columns of the first matrix
numInputs = len(Q[0])
numOutputs = len(Q)

numTrials = 100
numTests = 1
test_samples = createQTests(numTrials, numTests, numInputs, numOutputs, Q, 1)
numLayers = 3

if __name__ == "__main__":
	w = [
		[[2, 3], [5, 4]], # multiply this row by in 1 by 1 input vector (layer0) to get the layer1 activations
		[[1, 1], [3, 1]] # multiply this row by the 2 by 1 layer1 activation to get output layer
		 ]
	# w = [
	# 	[[1], [2]], # multiply this row by in 1 by 1 input vector (layer0) to get the layer1 activations
	# 	[[3, 4]] # multiply this row by the 2 by 1 layer1 activation to get output layer
	# 	 ]
	output_Vals = [[] for i in range(numOutputs)]
	yVals = [[] for i in range(numOutputs)]
	wVals = []

	for i in range(numTrials):

		a = [[0] for k in range(numLayers + 1)]

		# Later will layer by layer copy matrices, here just hardcode
		# d = [
		# 	[[0], [0]],
		# 	[[0, 0]]
		# 	]

		dw = copy.deepcopy(w)

		# later iterate over many test case in a particular sample
		test_case = test_samples[i][0]
		a[0] = test_case[0] # inputs
		y = test_case[1] # labels

		# need a for loop to iterate activation computations
		# a[1] = MVM(w[0], a[0])
		# a[2] = MVM(w[1], a[1])

		a = compute_output(w, a, numLayers-1)

		# iterate through all the edges in the last layer
		# dw[numLayers-1][0][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][0][1] = 2 * (a[2][0] - y[0]) * a[1][1]
		#
		# dw[numLayers-1][1][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][1][1] = 2 * (a[2][0] - y[0]) * a[1][1]

		# one of these should be numOutputs?
		# for i1 in range(len(w[numLayers-1])):
		for i1 in range(numOutputs):
			for i2 in range(len(w[numLayers-2])):
				dw[numLayers-2][i1][i2] = 2 * (a[numLayers-1][i1] - y[i1]) * a[numLayers-2][i2]


		# can use the d value of the layer in front to calculate backwards
		# dw[0][0][0] = dw[1][0][0] / a[1][0] * w[1][0][0] * a[0][0]
		# dw[0][1][0] = dw[1][0][1] / a[1][1] * w[1][0][1] * a[0][0]

		# need to calculate da values to calculate the next dw values

		clayer = 2
		something = 2
		da = [0 for k in range(0, something)]
		for k1 in range(0, something):
			# da[0] = dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0]
			for k2 in range(len(w)):
				da[0] += dw[clayer][k1][k2] / a[clayer][k2] * w[clayer][k2][k1] * w[1][k1][k2]



		dw[0][0][0] = (dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0]) * a[0][0]
		dw[0][1][0] = (dw[1][0][1] / a[1][1] * w[1][0][1] + dw[1][1][1] / a[1][1] * w[1][1][1]) * a[0][0]

		dw[0][0][1] = (dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0]) * a[0][1]
		dw[0][1][1] = (dw[1][0][1] / a[1][1] * w[1][0][1] + dw[1][1][1] / a[1][1] * w[1][1][1]) * a[0][1]

		total_cost = compute_cost(a, numLayers-1, numOutputs, y)
		c = - 1 / 100
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
	# print(w)
	# print(w[0][0][0] * w[1][0][0] + w[0][1][0] * w[1][0][1])
	# print(w[0][0][0] * w[1][0][0] + w[0][1][0] * w[1][0][1])
	for i in range(numOutputs):
		pylab.subplot((numOutputs + 1) * 100 + 11 + i)
		pylab.plot(xVals, yVals[i], 'b--', label="yVals[{}]".format(i))
		pylab.plot(xVals, output_Vals[i], 'b.', label="output_Vals[{}]".format(i))
		pylab.legend()

	pylab.subplot((numOutputs + 1) * 100 + 11 + numOutputs)
	pylab.plot(xVals, costVals, 'g--')
	pylab.show()
	# show_results()





