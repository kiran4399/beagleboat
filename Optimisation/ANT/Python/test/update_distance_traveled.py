import os
import unittest
import importlib
import sys
import inspect
import random
import ant_colony as module

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 


class TestAntUpdateDistanceTraveled(unittest.TestCase):
	def test_correct(self):
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _pick_path(self): pass
		test_object = test_empty_object()
		
		test_object.distance_traveled = 0
				
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object._update_distance_traveled(0, 1)
		
		self.assertEqual(test_object.distance_traveled, 1)

if __name__ == '__main__':
	unittest.main()
