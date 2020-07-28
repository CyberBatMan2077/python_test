from user1 import User
class Privileges():
	def __init__(self,privileges = 'can add post'):
		self.privileges	= privileges

	def show_privileges(self):
		print(self.privileges)

class Admin_new(User):
	def __init__(self,first_name,last_name,age,region):
		super().__init__(first_name,last_name,age,region)
		self.privileges = Privileges()