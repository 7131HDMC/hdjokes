import random
import os
import json
# 
# jokesdict = open('jokes.js#on')
# 
# 
def head(listarr):
	aux='Array is empty'
	if len(listarr)>0:
		print(listarr)
		aux=listarr[0] 
	return aux 

class haridadejokes:
	def __init__(self,language='pt',web=True):
		#return dict
		name = "../../jokes/"+language+"/jokes"	 
		if web:
			 name+="web"
		name+=".json"  
		#
		print(name)
		self.jokes = json.load(open(name))

	#get jokes, futhermore will implemente list of ob to mixe categories and so on  	
	def get_joke(self,category=''):
		select = random.choice(self.jokes)

		return select['joke']





hd =  haridadejokes()
print(hd.get_joke())