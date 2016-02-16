# I'm importing a library called 're'. You can ignore this for now.
import re

# NameFriend.py

# Hi again Mickey, this assignment is going to teach you 
# about lists and arrays

class NameFriend:
	# This method is run when you do `NameFriend()`
	# Doing `NameFriend()` is telling the computer to
	# "instantiate a NameFriend object"
	# Touch this method if you want to experiment with 
	# writing class instantiators.
	def __init__(self, *args):
		for friend_name in args:
			self.friends.append(friend_name)
	
	# These are 'Object properties' that the class, once instantiated,
	# will have internally.
	friends = []
	friend_numbers = {}

	# This method prints out all of your friends
	def print_friends(self):
		return_val = "Friends: {}".format(self.friends)
		print return_val
		return return_val

	'''
	Fix the methods below.
	'''

	def first_friend(self):
		'''
		Returns the first friend
		HINT: to access object properties, use `self.<property_name>`
		'''
		pass

	def last_friend(self):
		'''
		Returns the last friend
		HINT: to access object properties, use `self.<property_name>`
		'''
		pass

	def second_friend(self):
		'''
		Returns the second friend (or `None` if there's only one friend)
		HINT: to access object properties, use `self.<property_name>`
		'''
		pass

	def populates_friend_numbers(self):
		'''
		Populate the `friend_numbers` dictionary property with the following structure:
		key = index (starting at zero and identifying what order the friend is in the list)
		value = friend's name
		HINT: Dictionaries can be populated with the following syntax:
			test_dictionary[{key}] = {value}
			Where {key} can be substituted with a string or number and {value} can
			be substituted with anything else.
		HINT: to access object properties, use `self.<property_name>`
		'''
		pass

if __name__ == '__main__':
	# Here we've commented out the name_friend instantiation.
	# You will want to add a bunch of "Strings" to the arguments of NameFriend.
	# Example:
	# name_friend = NameFriend('Jerry', 'Bob', 'Ellis', 'Yvonne')

	# Here is one you can uncomment (remove the hash-tag before it)
	# name_friend = NameFriend()
	if name_friend:
		assert re.search(r"Friends: ", name_friend.print_friends()) is not None
		assert name_friend.first_friend() == name_friend.friends[0]
		assert name_friend.last_friend() == name_friend.friends[-1]
		assert (name_friend.second_friend() ==  name_friend.friends[1]) or (name_friend.second_friend() is None)
		name_friend.populates_friend_numbers()
		assert name_friend.friend_numbers[0] == name_friend.first_friend()

	else:
		print "Make sure this program instantiates the NameFriend class"

