

from math import pi
from Useful import *

# generating test samples
# numSamples = 1000 # make multiple of 10 for now
# test_samples = [random.random() for i in range(numSamples)]
# test_labels = [test_samples[i] * pi for i in range(numSamples)]
# trend will be multiply by pi

nodesPerLayer = 1
# generating test samples
numSamples = 100
test_samples = [[random.random() for j in range(nodesPerLayer)] for i in range(numSamples)]
test_labels = [[test_samples[i][j] * pi for j in range(0, nodesPerLayer)] for i in range(numSamples)]
# trend will be multiply by pi
if __name__ == "__main__":

	w = [[random.random() for z in range(nodesPerLayer)] for i in range(nodesPerLayer)]

	xVals = []
	output_Vals = [[] for i in range(nodesPerLayer)]
	yVals = [[] for i in range(nodesPerLayer)]
	costVals = []
	for i in range(numSamples):

		a = [[0] for v in range(nodesPerLayer+1)]
		d = [[0 for l in range(0, nodesPerLayer)]  for v in range(0, nodesPerLayer)]

		a[0] = test_samples[i]
		y = test_labels[i]
		a[1] = MVM(w, a[0])

		# print("output vector is {} label is {}".format(a[1], y))

		total_cost = 0
		for o in range(nodesPerLayer):
			total_cost += pow((a[1][o] - y[o]), 2)


		for r in range(0, nodesPerLayer):
			for v in range(0, nodesPerLayer):
				total_change = 0
				# for t in range(0, nodesPerLayer):
				total_change += a[0][r] * 2 * (a[1][v] - y[v])
				d[r][v] = total_change

		# print(d[1])
		# print(w[1])
		w[0] = VVA(w[0], SVM(-1/10, d[0]))
		# w[1] = VVA(w[1], SVM(-1/100, d[1]))

		xVals.append(i)
		costVals.append(total_cost)
		for q in range(0, nodesPerLayer):
			output_Vals[q].append(a[1][q])
		for q in range(0, nodesPerLayer):
			yVals[q].append(y[q])

	for i in range(0, nodesPerLayer):
		pylab.subplot((nodesPerLayer+1) * 100 + 11+i)
		pylab.plot(xVals, output_Vals[i], 'b--')
		pylab.plot(xVals, yVals[i], 'r--')
	pylab.subplot((nodesPerLayer+1) * 100 + 11 + nodesPerLayer)
	pylab.plot(xVals, costVals, 'g--')
	# for i in range(len(yVals)):
	# 	pylab.plot(xVals, yVals[i], 'b--')

	pylab.show()
	# t = 1
	# for j in range(numLayers):
	# 	t *= w[j]
	# print(t)
	# print(w)
	'''
	
	
	w = [random() for i in range(numLayers)]

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
	
	'''






