# runs the whole thing

from visualizer import *
from network import *

if __name__ == "__main__":
	v = Visualizer((720, 400))
	config = [3, 2, 3]
	n = Network(config)
	v.load_network(n)
	v.draw_network()
	v.run_visualization()