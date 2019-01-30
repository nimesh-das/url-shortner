#!/usr/bin/python3
import hashlib
import base64
import string
import random
import sqlite3

# External database for strategy # 2
if (os.path.isfile("database.db") == False):
	db = sqlite3.connect('database.db')
	db.execute('create table shortner (url_code text, url_full text)')


class Shortner:

	def code_generator(self):
		return ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
		
	def add_url(self):
		#check in the database whether url exists
		new_code = self.code_generator()
		cur = db.cursor()
		cur.execute("select * from shortner where url_code=?", new_code)
		data = cur.fetchall()
		while (data is not None):
			new_code = self.code_generator()
			cur.execute("select * from shortner where url_code=?", new_code)
			data = cur.fetchall()
		
		#when a unique code has been found, enter it in the dictionary
		result = "http://bit.ly/" + new_code;
		url = input("Please enter your url: ")
		new_dict[new_code] = result;
		print("Your shortnened url is: " + result)
		

s1 = Shortner()
s1.add_url()
		
		
			
		
	

