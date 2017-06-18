import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as module

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

class TestAntColonyMainLoop(unittest.TestCase):
	def test_correct(self):
		module.debug = False
	
	class test_empty_object(module.ant_colony):
		def __init__(self): pass
		def _get_distance(self, start, end): pass
		def _init_matrix(self, size, value = None): pass
		def _init_ants(self, start): pass
		def _update_pheromone_map(self): pass
		def _populate_and_updated_pheromone_map(self, ant): pass

	test_object = test_emp_object()


	def _init_matrix(size, value = None)
		ret = []
		for row in range(size):
			ret.append([value for x in range(size)])
		return ret

	class mock_ant:
		def get_distance_traveled(self): pass
		def get_route(self): pass
		def start(self): pass
		def join(self): pass

	test_object.ants = [mock_ant()]
	self.called_populate_ant_updated_pheromone_map = False
	def mock_populate_ant_updated_pheromone_map(ant):
		self.called_populate_ant_updated_pheromone_map = True

	test_object._populate_ant_updated_pheromone_map = mock_populate_ant_updated_pheromone_map

	self.called_update_pheromone_map = False
	def mock_update_pheromone_map():
		self.called_update_pheromone_map = True

	test_object._update_pheromone_map = mock_update_pheromone_map
	
	test_object.iterations = 1

	test_object.first_pass = None
	test_object.nodes = dict()
	test_object.shortest_distance = None
	test_object.shortest_path_seen = [0]
	test_object.start = 0
	test_object.id_to_key = {0: 0}
	
	test_object.mainloop()
	self.assertTrue(self.called_update_pheromone_map)
	self.assertTrue(self.called_populate_ant_updated_pheromone_map)

	def self.called_update_pheromone_map
	def self.called_populate_ant_updated_pheromone_map


if __name__ == '__main__':
	unittest.main()
