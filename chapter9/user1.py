class User():
	def __init__(self,first_name,last_name,age,region):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.region = region

	def describe_user(self):
		print("User's name is " + self.first_name.title() + ' ' +
			  self.last_name.title() + ' ,age is ' + self.age +
			  ' user is from ' + self.region)

	def greet_user(self):
		print("Welcome, " + self.first_name.title() + ' ' +
			  self.last_name.title())
