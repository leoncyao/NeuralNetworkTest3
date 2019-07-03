import pygame
import math
import copy

white = (255, 255, 255)
black = (0, 0, 0)
layer_dist = 250 # dist between layers horizontally
node_height = 25 # dist between nodes vertically
node_rad = 5
edge_width = 3

top_left_corner = (100, 75)


pygame.init()
class Node:
	def __init__(self, pos, val):
		self.pos = pos
		self.val = val

class Edge:
	def __init__(self, start_pt, end_pt):
		self.start_pt = start_pt
		self.end_pt = end_pt



class Visualizer:
	def __init__(self, screen_dim: tuple):
		self.nodes = []
		self.edges = []
		self.display_width = screen_dim[0]
		self.display_height = screen_dim[1]
		self.center_screen_x = self.display_width / 2
		self.center_screen_y = self.display_height / 2
		self.Display = pygame.display.set_mode((self.display_width, self.display_height))
		self.Display.fill(white)

	def run_visualization(self):
		Running = True
		while Running:
			pass
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					Running = False
			pygame.display.update()

	def load_network(self, n):
		# store nodes
		for i in range(n.numLayers):
			# self.nodes.append([])
			for j in range(len(n.nodes[i])):
				self.nodes[i].append(Node((top_left_corner[0] + i * layer_dist, top_left_corner[1] + j * node_height), n.nodes[i][j]))
				# self.draw_node(n.nodes[i][j], (top_left_corner[0] + i * layer_dist, top_left_corner[1] + j * node_height))

		# store edges

		for i in range(0, len(self.nodes)-1):
			for j in range(0, len(self.nodes[i])):
				for k in range(0, len(self.nodes[i][j])):
				self.edges.append(Edge(self.nodes[i][j], self.nodes[i][k]))

		# self.edges = copy.deepcopy(n.w)

		# for i in range(len(self.edges)):
		# 	for j in range(len(self.edges[i])):
		# 		for k in range(len(self.edges[i][j])):
		# 			print(self.edges[i][j][k])
					# self.edges[i][j][k] = Edge(self.nodes[i][j], self.nodes[i][k])
		# for i in range(n.numLayers - 1):
		# 	self.edges.append([])
		# 	for j in range(len(n.w[i])):
		# 		# self.edges[i] = n.w[i].deepcopy()
		# 		self.edges[i] = copy.deepcopy(n.w[i])
		# 		for k in range(len(n.nodes[i])):
		# 			# self.edges[i].append(Edge(self.nodes[i][j], self.nodes[i+1][k]))
		# 			self.edges[i][j].append(Edge(self.nodes[i][j], self.nodes[i + 1][k]))

	def draw_network(self):
		for i in range(len(self.nodes)):
			for j in range(len(self.nodes[i])):
				self.draw_node(nodes[i][j])

		for edge in self.edges:
			pass
			# self.draw_edge(edge)
		# # draw nodes
		# for i in range(n.numLayers):
		# 	for j in range(len(n.nodes[i])):
		# 		self.draw_node(n.nodes[i][j], (top_left_corner[0] + i * layer_dist, top_left_corner[1] + j * node_height))
		# # draw edges
		# for i in range(n.numLayers-1):
		# 	for j in range(n.w[i]):
		# 		for k in range(len(n.nodes[i])):
		# 			self.draw_edge(

	# should make private later
	def draw_node(self, node):
		pygame.draw.circle(self.Display, black, (int(node.pos[0]), int(node.pos[1])), node_rad)

	def draw_edge(self, edge):
		pygame.draw.line(self.Display, black, edge.start_pt, edge.end_pt, edge_width)


if __name__ == "__main__":
	v = Visualizer((720, 480))
	v.run_visualization()