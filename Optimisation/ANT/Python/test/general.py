import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as module

currentdir = os.path.dirname(os.path.dirname(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

class TestAntColonyMoreGeneral(unittest.TestCase):
	def test_generalised_node_names(self):
		module.debug = False

		testing_nodes = { 'a' : (1, 1),	15 : (0, 0), 'beaver' : (2, 2), 'yes we can' : (3, 3)}
		
		def testing_distance_callback(start, end):
			if (start == (0, 0) and end == (1, 1)) or (start == (1, 1) and end == (0, 0)):
				return 1.0
			if (start == (1, 1) and end == (2, 2))or (start == (2, 2) and end == (1, 1)):
				return 1.0
			if (start == (2, 2) and end == (3, 3))or (start == (3, 3) and end == (2, 2)):
				return 1.0
			return 3.0
		
		
		test_object = module.ant_colony(testing_nodes, testing_distance_callback)
		self.assertEqual([15, 'a', 'beaver', 'yes we can'], test_object.mainloop())
		
if __name__ == '__main__':
	unittest.main()
