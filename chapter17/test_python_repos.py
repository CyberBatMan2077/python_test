import unittest
from python_repos import r
# import *arg that you want to get from python_repos.py directly

class PythonReposTest(unittest.TestCase):

	def test_status_code(self):
		#python_repos
		correct_status_code = 200
		self.assertEqual(correct_status_code, r.status_code)


unittest.main()