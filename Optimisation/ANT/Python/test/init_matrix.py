import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as module

class TestAntColonyInitMatix(unittest.TestCase):
	def test_correct(self):
		module.debug = False

		class test_empty_object(module.ant_colony):

			def __init__(self): pass
			def _get_distance(self,start, end): pass
			def _init_ants(self, count, start=0): pass
			def _add_pheromone_value(self, route, pheromone_values): pass
			def _dissipate_pheromones(self): pass
			def mainloop(self): pass

		test_object = test_empty_object()

		self.assertEqual(test_object._init_matrix(1), [[0.0]])

if __name__ == '__main__':
	unittest.main()
