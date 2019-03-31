from Useful import *


# Q = [[1, 3, 5], [4, 2, 1]]
# Q = [[1, 3], [2, 4]]
Q = [[42]]
# Q = [[math.pi, 2.7], [1, 3]]

# Will need to change this later. numInputs should be the
# number of columns of the first matrix
numInputs = len(Q[0])
numOutputs = len(Q)

numTrials = 100
numTests = 1
test_samples = createQTests(numTrials, numTests, numInputs, numOutputs, Q, 1)

print(test_samples)
if __name__ == "__main__":
	# w = [
	# 	[[2, 3], [5, 4]], # multiply this row by in 1 by 1 input vector (layer0) to get the layer1 activations
	# 	[[1, 1], [3, 1]],
	# 	[[1, 1], [3, 1]] # multiply this row by the 2 by 1 layer1 activation to get output layer
	# 	 ]
	# w = [
	# 	[[0], [0]],
	# 	[[0], [0]]
	# 	  ]
	w = [
		[[1], [1]],
		[[1, 1]],
		[[1]]
		]
	# need plus 1 for input layer
	numLayers = len(w) + 1
	# w = [
	# 	[[1], [2]], # multiply this row by in 1 by 1 input vector (layer0) to get the layer1 activations
	# 	[[3, 4]] # multiply this row by the 2 by 1 layer1 activation to get output layer
	# 	 ]
	output_Vals = [[] for i in range(numOutputs)]
	yVals = [[] for i in range(numOutputs)]

	for i in range(numTrials):
		# need to change 100 later
		a = [[0 for j in range(100)] for k in range(numLayers + 1)]
		da = copy.deepcopy(a)
		dw = copy.deepcopy(w)

		# later iterate over many test case in a particular sample
		test_case = test_samples[i][0]
		a[0] = test_case[0] # inputs
		y = test_case[1] # labels

		# need a for loop to iterate activation computations

		a = compute_output(w, a, numLayers-1)

		# iterate through all the edges in the last layer
		# dw[numLayers-1][0][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][0][1] = 2 * (a[2][0] - y[0]) * a[1][1]
		#
		# dw[numLayers-1][1][0] = 2 * (a[2][0] - y[0]) * a[1][0]
		# dw[numLayers-1][1][1] = 2 * (a[2][0] - y[0]) * a[1][1]

		# For last layer
		for i1 in range(numOutputs):
			for i2 in range(len(w[numLayers-2])):
				dw[numLayers-2][i1][i2] = 2 * (a[numLayers-1][i1] - y[i1]) * a[numLayers-2][i2]

		# can use the d value of the layer in front to calculate backwards
		# dw[0][0][0] = dw[1][0][0] / a[1][0] * w[1][0][0] * a[0][0]
		# dw[0][1][0] = dw[1][0][1] / a[1][1] * w[1][0][1] * a[0][0]

		# need to calculate da values to calculate the next dw values

		# layer_num = 1

		# fixing layer number 1
		# for e1 in range(len(a[1])):
		# 	for e2 in range(len(a[2])):
		# 		# da[1][e] += (dw[1][0][0] / a[1][e] * w[1][0][0] + dw[1][1][0] / a[1][e] * w[1][1][0])
		# 		da[1][e1] += dw[1][e1][e2] / a[1][e1] * w[1][e1][e2]

		#
		# for e1 in range(len(a[1])):
		# 	for e2 in range(len(a[2])):
		# 		dw[layer_num-1][e1][e2] = da[e1][e2] * a[layer_num-1][e2]

		for layer_num in range(numLayers-2, 0, -1):
			# fixing layer number 1
			for e1 in range(len(a[1])):
				for e2 in range(len(a[2])):
					# da[1][e] += (dw[1][0][0] / a[1][e] * w[1][0][0] + dw[1][1][0] / a[1][e] * w[1][1][0])
					# da[1][e1] += dw[1][e1][e2] / a[1][e1] * w[1][e1][e2]
					da[layer_num][e1] += dw[layer_num][e1][e2] / a[layer_num][e1] * w[layer_num][e1][e2]
			# da[1][0] = (dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0])
			# da[1][1] = (dw[1][0][1] / a[1][1] * w[1][0][1] + dw[1][1][1] / a[1][1] * w[1][1][1])

			for e1 in range(len(a[1])):
				for e2 in range(len(a[2])):
					dw[layer_num-1][e1][e2] = da[e1][e2] * a[layer_num-1][e2]

		# da[1][0] = (dw[1][0][0] / a[1][0] * w[1][0][0] + dw[1][1][0] / a[1][0] * w[1][1][0])
		# da[1][1] = (dw[1][0][1] / a[1][1] * w[1][0][1] + dw[1][1][1] / a[1][1] * w[1][1][1])
		#
		# dw[0][0][0] = da[1][0] * a[0][0]
		# dw[0][1][0] = da[1][1] * a[0][0]
		#
		# dw[0][0][1] = da[1][0] * a[0][1]
		# dw[0][1][1] = da[1][1] * a[0][1]

		total_cost = compute_cost(a, numLayers-1, numOutputs, y)
		c = - 1 / 10
		for i1 in range(0, len(w)):
			for i2 in range(0, len(w[i1])):
				for i3 in range(0, len(w[i1][i2])):
					w[i1][i2][i3] += c * dw[i1][i2][i3]

		xVals.append(i)
		costVals.append(total_cost)
		# print(total_cost)
		for q in range(0, numOutputs):
			output_Vals[q].append(a[numLayers-1][q])
		for q in range(0, numOutputs):
			yVals[q].append(y[q])
	# print(w)
	for i in range(numOutputs):
		pylab.subplot((numOutputs + 1) * 100 + 11 + i)
		pylab.plot(xVals, yVals[i], 'b--', label="yVals[{}]".format(i))
		pylab.plot(xVals, output_Vals[i], 'r.', label="output_Vals[{}]".format(i))
		pylab.legend()

	pylab.subplot((numOutputs + 1) * 100 + 11 + numOutputs)
	pylab.plot(xVals, costVals, 'g--')
	pylab.show()
	# show_results()





