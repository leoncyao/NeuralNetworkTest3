from Useful import *

class Network:

	def __init__(self, config):
		'''
		:param config: array of length L, specifying the number of nodes in each layer
		assuming an edge between every pair of nodes in adjacent layers

		>>> config = [1,1]
		>>> n = Network(config)
		>>> print(n.w)
		[[[0]]]


		'''
		self.numLayers = len(config)
		self.nodes = [[0 for i in range(config[k])] for k in range(self.numLayers)]
		self.initialize_weights(self.numLayers, config)


	def initialize_weights(self, numLayers, config):
		'''
		:return w: a weight matrix whose entries are arrays detailing the transitions between layers
		w[i] represents the transitions between the ith layer and i+1th layer
		w[i][j] represents the connection between layer a[i] and node j in layer a[i+1]
		w[i][j][k] is the weight of the kth node in layer a[i] and the jth node in layer a[i+1]

		'''
		# might to reference field itself and not return since its a matrix and not a primitive
		self.w = []
		for i in range(numLayers-1):
			# create a matrix with dimensions config[k] by config[j]
			row = [0 for k in range(config[i])]
			m = [row for j in range(config[i+1])]
			self.w.append(m)

# class Node:
# 	def __init__(self):
# 		self.activation = 0