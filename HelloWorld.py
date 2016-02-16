# HelloWorld.py

# Hi Mickey, this is your first introduction to Python
# Follow the instructions below 

class HelloWorld():
	'''
	You will want to replace `pass` in each method (notated by `def blahblah(self):`)
	with the appropriate "return" statement
	'''
	def __init__(self):
		print "You've created a HelloWorld object! Hooray!"

	def hello(self):
		'''
		Returns the string "Hello World!"
		'''
		pass

	def goodbye(self):
		'''
		Returns the string "Goodbye World!"
		'''
		pass

	def get_name(self):
		'''
		Returns the string "HelloWorld"
		'''
		pass

# Unit testing. We have three assert statements that should pass.
# To run this program, go to terminal, cd to this directory, and
# then run "python HelloWorld.py".

if __name__ == "__main__":
	# 1) We take the `HelloWorld` template 
	# and make it usable. We "instantiate the class".
	helloWorld = HelloWorld()
	# 2) We run `helloWorld`'s methods through an assert statement
    # to see if we did the right thing 
	assert helloWorld.hello() == "Hello World!"
	assert helloWorld.goodbye() == "Goodbye World!"
	assert helloWorld.get_name() == "HelloWorld"
	# 3) We print "Done." 
	print "Done."