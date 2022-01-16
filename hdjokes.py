import random
import os
import json
# 
# jokesdict = open('jokes.js#on')
# 
# 

class haridadejokes:
	def __init__(self,language='pt'):
		#return dict
		name = "jokes/"+language+"/jokes.json"
		print(name)
		pt = json.load(open(name))
		self.jokes = pt[language]

	#get jokes, futhermore will implemente list of ob to mixe categories and so on  	
	def get_joke(self,category=''):
		return random.choice(self.jokes)





hd =  haridadejokes()
print(hd.get_joke())