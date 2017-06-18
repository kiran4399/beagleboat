import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as modulei

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


class TestAntTraverse(unittest.TestCase):
	def test_correct(self):
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		test_object.location = 0	#starting at the 0th position
		
		self.called_update_route = False
		def mock_update_route(end):
			self.called_update_route = True
		
		test_object._update_route = mock_update_route
		
		self.called_update_distance_traveled = False
		def mock_update_distance_traveled(start, end):
			self.called_update_distance_traveled = True
			
		test_object._update_distance_traveled = mock_update_distance_traveled
		
		test_object._traverse(0, 1)
		
		self.assertEqual(test_object.location, 1)
		self.assertTrue(self.called_update_route)
		self.assertTrue(self.called_update_distance_traveled)
		
		del self.called_update_route
		del self.called_update_distance_traveled

if __name__ == '__main__':
	unittest.main()
