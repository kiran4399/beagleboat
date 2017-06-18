import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as module

class TestAntColonyInitNodes(unittest.TestCase):
	def test_correct(self):
		module.debug = False

	class test_empty_object(module.ant_colony):
		def __init__(self): pass
		def _get_distance(self, start, end): pass
		def _init_matrix(self, size, value=None): pass
		def _init_ants(self, start=0): pass
		def _update_pheromone_map(self): pass
		def _populate_ant_updated_pheromone_map(self, ant): pass
		def mainloop(self): pass

	test_object = test_empty_onject()

	testing_nodes = { 'a' : (1,1), 15 : (0,0), 'beaver': (2,2), 'yes we can' : (3,3)}
	
	id_to_key , id_to_values = test_object._init_nodes(testing_nodes)
	self.assertEqual({0:15, 1:'a', 2:'beaver', 3:'yes we can'}, id_to_key)
	self.assertEqual({0:(0,0), 1:(1,1), 2:(2,2), 3:(3,3), id_to_values)


if __name__ == '__main__':
	unittest.main()
