
def return_func():

	def func_inside():
		print("I'm inside")

	print("I'm outside")
	return func_inside
print(return_func)
inside = return_func()