#!env/bin/python3

# pygablib ist eine Pythonbibliothek für den Einsatz mit der Gab.ai Seite
# geschrieben von Heinrich Rosen-Kreutz
# September 2017

# importiert
from bs4 import BeautifulSoup
import json
from pprint import pprint
import requests
from requests import Session as session

class gablib():

	# Initialisierung
	def __init__(self, passedUsername, passedPassword):
		self.username = passedUsername
		self.password = passedPassword
		self.token = None
		
	# Anmeldung
	def login(self):

		s = requests.session()
		r = s.get('https://gab.ai/auth/login')
		if r.status_code == 200:
			soup = BeautifulSoup(r.content, 'html.parser')
			hiddenToken = soup.find("input",{"name":"_token"})['value']
			#print(hiddenToken)
			payload = {'username':self.username, 'password':self.password, '_token':hiddenToken}
			r = s.post('https://gab.ai/auth/login', params=payload)
			if r.status_code == 200:
				print(s.cookies)
				return True
			else:
				print('Scheisse')
				print(r.status_code)
				return False
			# print(r.status_code)
			# print(r.content)
		else: 
			print('Achtung! Fehler beim Zugriff auf die Anmeldeseite.')
			return False


	# Eigenes Futter bekommen

	# bekomme jemand anderes Futter

	# Eigenes Futter bekommen Pulse

	# Folgen

	# aufhoren zu folgen

	# wie ein posten

	# mag einen Beitrag nicht

	# entfernen wie

	# entfernen Abneigung

	# Suche

	# bekomme Benachrichtigungen

	