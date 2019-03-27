

from math import pi
from Useful import *


# trend will be multiply by pi

nodesPerLayer = 2
# generating test samples
numSamples = 1
# test_samples = [[random.random() for j in range(nodesPerLayer)] for i in range(numSamples)]
test_samples = [[1, 2] for j in range(0, numSamples)]
M = [[1, 2],[3, 4]]

test_labels = [MVM(M, test_samples[i]) for i in range(numSamples)]
# test_labels = [[test_samples[i][j] * pi for j in range(0, nodesPerLayer)] for i in range(numSamples)]

# print(test_samples)
# print(test_labels)


# trend will be multiply by pi
if __name__ == "__main__":

	# w = [[random.random() for z in range(nodesPerLayer)] for i in range(nodesPerLayer)]
	# w = [[pi for z in range(nodesPerLayer)] for i in range(nodesPerLayer)]
	w = [[0, 2], [3, 4]]

	xVals = []
	output_Vals = [[] for i in range(nodesPerLayer)]
	yVals = [[] for i in range(nodesPerLayer)]
	costVals = []
	wVals = []
	for i in range(numSamples):

		a = [[0] for v in range(nodesPerLayer+1)]
		d = [[0 for l in range(0, nodesPerLayer)]  for v in range(0, nodesPerLayer)]

		a[0] = test_samples[i]
		y = test_labels[i]
		a[1] = MVM(w, a[0])

		print ("a[1] is {}".format(a[1]))
		print("y is {}".format(y))
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

		matrixPrinter(d)
		matrixPrinter(w)


		# print(d[1])
		# print(w[1])
		c = -1/100
		w = MMA([w] , SMM(c, [d]))[0]
		# w[0] = VVA(w[0], SVM(c, d[0]))
		# w[1] = VVA(w[1], SVM(c, d[1]))

		xVals.append(i)
		costVals.append(total_cost)
		for q in range(0, nodesPerLayer):
			output_Vals[q].append(a[1][q])
		for q in range(0, nodesPerLayer):
			yVals[q].append(y[q])
		# for q in range(0, nodesPerLayer):
		wVals.append(w[0][0])


	for i in range(0, nodesPerLayer):
		pylab.subplot((nodesPerLayer+1) * 100 + 11+i)
		pylab.plot(xVals, wVals, 'b--')
		pylab.plot(xVals, output_Vals[i], 'b--')
		pylab.plot(xVals, yVals[i], 'r--')


	pylab.subplot((nodesPerLayer+1) * 100 + 11 + nodesPerLayer)
	pylab.plot(xVals, costVals, 'g--')
	# print(w)
	# print(MVM(w, [1,1]))
	# matrixPrinter(w)
	pylab.show()
	# t = 1
	# for j in range(numLayers):
	# 	t *= w[j]
	# print(t)






