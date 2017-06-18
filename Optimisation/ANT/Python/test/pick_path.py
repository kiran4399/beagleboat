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


class TestAntPickPath(unittest.TestCase):
	def test_is_first_pass(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		test_object.first_pass = True
		test_object.possible_locations = [x for x in range(10)]
		
		def mock_choice(*args):
			return 1
		choice_backup = random.choice
		random.choice = mock_choice
		
		self.assertEqual(test_object._pick_path(), 1)
		
		random.choice = choice_backup
		
	def test_single_path_with_pheromone(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		module.debug = False
		
		self.assertEqual(test_object._pick_path(), 1)
	
	def test_multiple_paths_with_pheromones_low_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		
		def mock_random():
			return .2
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 1)
		
		random.random = random_random_backup
		
	def test_multiple_paths_with_pheromones_medium_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		
		def mock_random():
			return .4
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 2)
		
		random.random = random_random_backup

	def test_multiple_paths_with_pheromones_high_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		
		def mock_random():
			return .8
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 2)
		
		random.random = random_random_backup
	
	def test_ALL_paths_with_pheromones_low_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		test_object.alpha = 1
		test_object.beta = 1
		
		def mock_random():
			return .2
			
		random_random_backup = random.random
		random.random = mock_random
		module.debug = False
		self.assertEqual(test_object._pick_path(), 4)
		
		random.random = random_random_backup
		
	def test_ALL_paths_with_pheromones_medium_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			#override each method EXCEPT _pick_path, to get a clean testing environment
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		def mock_random():
			return .5
			
		random_random_backup = random.random
		random.random = mock_random

		module.debug = False
		
		self.assertEqual(test_object._pick_path(), 7)
		
		random.random = random_random_backup
	
	def test_ALL_paths_with_pheromones_high_probability_toss(self):
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		
		def mock_distance_callback(start, end):
			return 1
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		def mock_random():
			return .9
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 9)
		
		random.random = random_random_backup
	
	def test_ALL_paths_with_pheromones_LOW_probability_toss_distance_varies(self):
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _deposit_pheromone(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		
		def mock_distance_callback(start, end):
			return (2*end - start) ** 2
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		def mock_random():
			return .1
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 1)
		random.random = random_random_backup
	
	def test_ALL_paths_with_pheromones_MEDIUM_probability_toss_distance_varies(self):
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		
		def mock_distance_callback(start, end):
			return (2*end - start) ** 2
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		def mock_random():
			return .5
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		self.assertEqual(test_object._pick_path(), 2)
		
		random.random = random_random_backup
	
	def test_ALL_paths_with_pheromones_HIGH_probability_toss_distance_varies(self):
		
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0)
		
		test_object.pheromone_map[0][1] = 1
		test_object.pheromone_map[0][2] = 2
		test_object.pheromone_map[0][3] = 3
		test_object.pheromone_map[0][4] = 4
		test_object.pheromone_map[0][5] = 5
		test_object.pheromone_map[0][6] = 6
		test_object.pheromone_map[0][7] = 7
		test_object.pheromone_map[0][8] = 8
		test_object.pheromone_map[0][9] = 9
		
		def mock_distance_callback(start, end):
			return (2*end - start) ** 2
		
		test_object.distance_callback = mock_distance_callback
		test_object.alpha = 1
		test_object.beta = 1
		def mock_random():
			return .99
			
		random_random_backup = random.random
		random.random = mock_random
		
		module.debug = False
		
		self.assertEqual(test_object._pick_path(), 9)
		
		random.random = random_random_backup
	
	def test_corner_case_of_attractiveness_of_all_paths_equal_zero(self):
		
		module.debug = True
		
		class test_empty_object(module.ant_colony.ant):
			def __init__(self): pass
			def run(self): pass
			def _traverse(self): pass
			def _update_route(self): pass
			def _update_distance_traveled(self): pass
		test_object = test_empty_object()
		
		def _init_matrix(size, value=None):
			ret = []
			for row in range(size):
				ret.append([value for x in range(size)])
			return ret
		
		test_object.first_pass = False
		test_object.location = 0	#starting at the 0th position
		test_object.possible_locations = [x for x in range(1, 10)]	#so we remove 0 from the list of possible locations for the next traversal
		test_object.pheromone_map = _init_matrix(len(test_object.possible_locations)+1, value=0.0)
		def mock_distance_callback(start, end):
			return (2*end - start) ** 2
		
		test_object.distance_callback = mock_distance_callback
		
		test_object.alpha = 1
		test_object.beta = 1
		
		def mock_random():
			return .99
			
		random_random_backup = random.random
		random.random = mock_random
		
		self.assertEqual(test_object._pick_path(), 1)
		
		random.random = random_random_backup
		
if __name__ == '__main__':
	unittest.main()
