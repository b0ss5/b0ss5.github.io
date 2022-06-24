#import fun things section
import PIL
import urllib.request
import json
from replit import db
import requests
import math
#jack section

prioritytargets = ['0cd39a51a8174144aa821c93fcc5ce8e', '6befbb4cbaaf4e8190873c93f315781c', 'e80e8194323e414298515e1bcb8a3508', 'bd3dd5a404384699b2fd36f518154b41', 'ec70bcaf702f4bb8b48d276fa52a780c', 'b984854b50494972afbe5d3c5855e7fe', '5d74806e208c4e2896f9ad9748eca154', 'e4c745df96d5436ca9e4b90edbea5aad', 'b59ffa9e15fe4ad7bb9199a25a533d9d', 'f71d1bf148634e4f832471e8293fdd39', 'b2a791b1f9a0482d99686c65d1675d89', 'ef89019f4bb14815a0611ada90e6d866', 'ce0d844bcdb144368d72300b59d2895a', '060a3552e0e84e499e87bac635a7656a', '5054f8f9a66f4b059357092fce6176fb', '76eab99d8b714aa2a50da4e2f384a7d1', '034bbd4ee7b440729d69d08af9c7e5a4', '3ce0dded77414e42b2cf4dd07fa9a3ce', 'cbc9aa335b584a39ab66ec7cc8cf36f5', '2409b14dc54c4889a6750ad427d86c42', 'b029d5c22a7c4e3a80162d8d2ea6672d', '77080d9795524addbf0056b9f46b2ae6']

def getUsername(username):
	url = "https://api.mojang.com/users/profiles/minecraft/" + username
	uf = urllib.request.urlopen(url)
	html = uf.read()
	htmldict = json.loads(html)
	return htmldict["name"]
def getStatus(username, key):
	try:
		url = "https://api.mojang.com/users/profiles/minecraft/" + username
		uf = urllib.request.urlopen(url)
		html = uf.read()
		htmldict = json.loads(html)
		uuid = htmldict["id"]
		url = "https://api.hypixel.net/status?key="+key+"&uuid=" + uuid  
		uf = urllib.request.urlopen(url)
		html = uf.read()



		html = str(html)
		x = html.find('{"o')
		htmldict = json.loads(html[x:-2])

		url = "https://api.hypixel.net/status?key="+key+"&uuid=" + uuid  
		uf = urllib.request.urlopen(url)
		html = uf.read()
		html = str(html)
		x = html.find


		if '"online":false' in html:
			return "Offline"
		else:
			print (htmldict)
			try:
				response1 = (htmldict['map'])
			except: 
				response1= "N/A"
			response2 = htmldict["gameType"]
			try:
				response3 = htmldict["mode"]
				return ["Online", response2, response1, response3]
			except:
				return ["Online", response2, response1]
	except:
		return "Player Does Not Exist"		


def getHtmlDict(username, key):
	url = "https://api.mojang.com/users/profiles/minecraft/" + username
	uf = urllib.request.urlopen(url)
	html = uf.read()
	htmldict = json.loads(html)
	uuid = htmldict["id"]
	print (uuid)

	url = "https://api.hypixel.net/player?key="+key+"&uuid=" + uuid  
	uf = urllib.request.urlopen(url)
	html2 = uf.read()
	htmldict2 = json.loads(html2)
	return htmldict2["player"]

def getStat(username, mode, stat, key):
	url = "https://api.mojang.com/users/profiles/minecraft/" + username
	uf = urllib.request.urlopen(url)
	html = uf.read()
	htmldict = json.loads(html)
	uuid = htmldict["id"]
	print (uuid)

	url = "https://api.hypixel.net/player?key="+key+"&uuid=" + uuid  
	uf = urllib.request.urlopen(url)
	html2 = uf.read()
	htmldict2 = json.loads(html2)

	return htmldict2["player"]['stats'][mode][stat]


def getSwColor(level):
	if level<5:
		level = str(level)
		return ('#AAAAAA')
	elif 5<=level<10:
		level = str(level)
		return ('#FFFFFF')
	elif 10<=level<15:
		level = str(level)
		return ('#FFAA00')
	elif 15<=level<20:
		level = str(level)
		return ('#55FFFF')
	elif 20<=level<25:
		level = str(level)
		return ('#00AA00')
	elif 25<=level<30:
		level = str(level)
		return ('#00AAAA')
	elif 30<=level<35:
		level = str(level)
		return ('#AA0000')
	elif 35<=level<40:
		level = str(level)
		return ('#FF55FF')
	elif 40<=level<45:
		level = str(level)
		return ('#5555FF')
	elif 45<=level<50:
		level = str(level)
		return ('#AA00AA')
	elif level>=50:
		level = str(level)
		return ['#FF5555','#FFAA00','#FFFF55','#55FF55','#55FFFF','#FF55FF','#AA00AA']
	
def getBwColor(level):
	if level<100:
		level = str(level)
		return ('#AAAAAA')
	elif 100<=level<200:
		level = str(level)
		return ('#FFFFFF')
	elif 200<=level<300:
		level = str(level)
		return ('#FFAA00')
	elif 300<=level<400:
		level = str(level)
		return ('#55FFFF')
	elif 400<=level<500:
		level = str(level)
		return ('#00AA00')
	elif 500<=level<600:
		level = str(level)
		return ('#00AAAA')
	elif 600<=level<700:
		level = str(level)
		return ('#AA0000')
	elif 700<=level<800:
		level = str(level)
		return ('#FF55FF')
	elif 800<=level<900:
		level = str(level)
		return ('#5555FF')
	elif 900<=level<1000:
		level = str(level)
		return ('#AA00AA')
	elif level>=1000:
		level = str(level)
		return ['#FF5555', '#FFAA00', '#FFFF55', '#55FF55','#55FFFF', '#FF55FF','#AA00AA']

#ben section 

def getUUID(username):
		api = f"https://api.mojang.com/users/profiles/minecraft/{username}"
		data = requests.get(api)
		return data.json()['id']

def getusername(uuid):
	api = f"https://sessionserver.mojang.com/session/minecraft/profile/{uuid}"
	data = requests.get(api)
	return data.json()['name']


def signup (username, password, key):
	if username == "" or password == "" or key == "":
		return "Empty"
	else:	
		if username in db.keys():
			return False
		else:

			return True

def apicheck (username, key):
	try:
		UUID = getUUID(username)
	except:
		return False
	url = f"https://api.hypixel.net/key?key={key}"
	try:
		uf = urllib.request.urlopen(url)
		html = uf.read()
		data = json.loads(html)
		data = data["record"]["owner"]
		data = data.replace("-", "")
		print (data)
		print (UUID)
		if data == str(UUID):
			return True
		else:
			return False
	except: 
		return False

def uuidreal(uuid):
		url = "https://api.mojang.com/users/profiles/minecraft/" +(uuid)
		uf = urllib.request.urlopen(url)
		html = uf.read()
		data = json.loads(html)
		if data.json()['id'] == uuid:
			return True
		else: return False
#eaa53007-41e8-4ada-a2fd-d60217ef11c7



def getHead(uuid):
	url = "https://crafatar.com/renders/head/" + uuid
	return url
def getModel(uuid):
	url = 'https://crafatar.com/renders/body/' + uuid
	return url


def getAnyStat(htmldict, stat):
	
	if stat == "Skywars Kills":
		try:
			result = htmldict['stats']['SkyWars']['kills']
		except: 
			result = "error"
		return result
	elif stat == "Skywars Wins":
		try:
			result = htmldict['stats']['SkyWars']['wins']
		except: 
			result = "error"
		return result
	elif stat == "Skywars K/D":
		try:
			result = round((int(htmldict['stats']['SkyWars']['kills'])/int(htmldict['stats']['SkyWars']['deaths'])),2)
		except: 
			result = "error"
		return result
	elif stat == "Skywars Star":
		try:
			result = htmldict['achievements']['skywars_you_re_a_star']
		except: 
			result = "error"
		return result
	elif stat == "Skywars W/L":
		try: 
			result = round((int(htmldict['stats']['SkyWars']['wins'])/int(htmldict['stats']['SkyWars']['losses'])), 2)
		except:
			result = 'error'
		return result
	elif stat == "Bedwars Finals":
		try:
			result = htmldict['stats']['Bedwars']['final_kills_bedwars']
		except: 
			result = "error"
		return result
	elif stat == "Bedwars Wins":
		try:
			result = htmldict['stats']['Bedwars']['wins_bedwars']
		except: 
			result = "error"
		return result
	elif stat == "Bedwars Final K/D":
		try: 
			result = round((int(htmldict['stats']['Bedwars']['final_kills_bedwars']))/(int(htmldict['stats']['Bedwars']['final_deaths_bedwars'])),2)
		except:
			result = 'error'
		return result
	elif stat == "Bedwars Star":
		try:
			result = htmldict['achievements']['bedwars_level']
		except: 
			result = "error"
		return result
	elif stat == "Bedwars Winstreak":
		try: 
			result = htmldict['stats']['Bedwars']['winstreak']
		except:
			result='error'
		return result
	elif stat == "Bedwars W/L": 
		try:
			result = round((int(htmldict['stats']['Bedwars']["wins_bedwars"]))/(int(htmldict['stats']['Bedwars']['losses_bedwars'])), 2)
		except:
			result = "error"
		return result
	elif stat == "Hypixel Level":
		try:
			result = int((math.sqrt((2 * int(htmldict['networkExp'])) + 30625) / 50) - 2.5)
		except:
			result = "error"
		return result
	else: result = "error" 


def notablePlayers():
	notable={}
	size=0
	for player in prioritytargets:
		status = getStatus(getusername(player), '336a58a8-966f-4d34-97d1-1a511bda9172')
		if status !='Offline':
			notable.update({getusername(player):{'mode': status[1], 'map':status[2]}})
			size=size+1
		if size==3:
			break
	return notable
			
