#PROGRAMMER: Frederick Herzog
#DATE: 12-05-2017



class Employee:

	def __init__(self, name, id_num, dept, title):
		self.__name = name 
		self.__id_num = id_num
		self.__department = dept
		self.__title = title 

	def Set_name(self, name):
		self.__name = name

	def Set_id_num(self, id_num):
		self.__id_num = id_num

	def Set_department(self, dept):
		self.__department = dept

	def Set_title(self, title):
		self.__title = title

	def Get_name(self):
		return self.__name 

	def Get_id_num(self):
		return self.__id_num

	def Get_department(self):
		return self.__department

	def Get_title(self):
		return self.__title
