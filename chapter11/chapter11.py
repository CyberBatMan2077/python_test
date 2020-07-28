#homework  11-1
import unittest
from city_functions import country_city

class CountryCityTest(unittest.TestCase):
	"""测试city.function.py"""

	def test_city_country(self):
		"""是否能正确完成功能"""
		result = country_city('Guangzhou','china')
		self.assertEqual(result,'Guangzhou, China')

#homework  11-2
	def test_city_country_with_population(self):
		"""加入人口参数"""
		result = country_city('Shenzhen','china','10000')
		self.assertEqual(result,'Shenzhen, China - 10000')

#unittest.main()
#if you use pycharm please delete unittest.main(),
#because when pycharm run a unittest case,it won't start from main function

#homework  11-3
class Employee():
	def __init__(self,first_name,last_name,salary):
		self.first_name = first_name
		self.last_name = last_name
		self.salary	= salary

	def salary_increase(self,increment=5000):
		self.salary += increment

class EmployeeTest(unittest.TestCase):
	def setUp(self):
		self.person_1 = Employee('Michael','Jackson',0)

	def test_give_default_raise(self):
		self.person_1.salary_increase()
		self.assertEqual(self.person_1.salary,5000)


	def test_give_custom_raise(self):
		self.person_1.salary_increase(3000)
		salary = self.person_1.salary
		self.assertEqual(self.person_1.salary,3000)

	def test_give_custom_raise_1(self):
		self.person_1.salary_increase(1000)
		salary = self.person_1.salary
		self.assertEqual(self.person_1.salary,1000)
