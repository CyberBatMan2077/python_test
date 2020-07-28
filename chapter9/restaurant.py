class Restaurant_new_new():
	def __init__(self,restaurant_name,cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print("The name of restaurant is " + self.name.title())
		print("The type of cuisine is " + self.type.title())


	def open_restaurant(self):
		print("We are now opening,Welcome")

	def number_change(self,served_number):
		self.number_served = served_number

	def increment_number_served(self,increment):
		self.number_served += increment