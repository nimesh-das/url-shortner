#!/usr/bin/python3
import hashlib
import base64
import string
import random

#hash_object = hashlib.md5(b'Hello World')
#print(hash_object.hexdigest())

#data = base64.b64encode(b'data to be encoded')
#print(data)

# External dictionary/database
new_dict = dict()

class Shortner:

	def code_generator(self):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		
	def add_url(self):
		#either check in database if url exists
		# or if you don't have database, check in the dictionary
		new_code = self.code_generator()
		while new_code in new_dict:
			new_code = code_generator()
		#when a unique code has been found, enter it in the dictionary
		result = "http://bit.ly/" + new_code;
		url = input("Please enter your url: ")
		new_dict[new_code] = result;
		print("Your shortnened url is: " + result)
		

s1 = Shortner()
s1.add_url()
		
		
			
		
	

