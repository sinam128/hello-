class sinam() :
	def __init__ (self , name , code ) :
		self.name = name 
		self.code = code 

	def write (self) :
		print(f"I am {self.name} and my code is {self.code}")



x = input("Hey there ! Pls enter your name here : ")
y = int(input("And here you will give us you code : "))
student = sinam(x,y)
student.write()
