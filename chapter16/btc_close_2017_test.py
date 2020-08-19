import unittest
from btc_close_2017 import draw_line
import json

class Btc_Close_Test(unittest.TestCase):
	

	def test_average_result(self):
		"""是否能正确完成功能"""
		filename = 'btc_close_2017.json'
		with open(filename)    as f:
			btc_data = json.load(f)

		dates, months, weeks, weekdays, close = [], [], [], [], []
		month_close = []

		for btc_dict in btc_data:
			dates.append(btc_dict['date'])
			months.append(int(btc_dict['month']))
			weeks.append(int(btc_dict['week']))
			weekdays.append(btc_dict['weekday'])
			close.append(int(float(btc_dict['close'])))
			month_close.append((int(btc_dict['month']),int(float(btc_dict['close']))))
		print(months)
		month = [1,2,3,4,5,6,7,8,9,10,11,12]
		result =[0,0,0,0,0,0,0,0,0,0,0,0]
		mont_data_number = [0,0,0,0,0,0,0,0,0,0,0,0]
		result_compare =[]
		for x,y in month_close:
			result[month.index(x)] += y
			mont_data_number[month.index(x)] += 1
		print(result)
		print(mont_data_number)
		for i in range(0,12):
			y = result[i] / mont_data_number[i]
			result_compare.append(y)
		# 考虑到测试时，需要验证的两种数据最好通过不同的算法得出，所以在测试中的结果使用了另一种算法：
		# 把月数和收盘数据组合成一个二元列表后，通过第一个for循环，按照索引把其值分别加到result和mont_data_number
		# 的对应索引位中，这样最后result中的12个元素对应的是该月总值，mont_data_number对应的是该月有几个数据
		#最后除法得到均值，与draw_line中的数据进行对比，注意draw_line中的return值需要改一下，因为原方法返回的是一个图表
		result_function = line_chart_month = draw_line(months,close,'a','b')
	#	prin(list(result_function))
	#	print(result_compare)
		self.assertEqual(result_compare,list(result_function))
	
unittest.main()