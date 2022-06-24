#SETUP AREA
#NO SCROLLING

from flask import Flask,redirect,url_for
from flask import render_template
from flask import request
import model
from replit import db
import PIL
app = Flask('app')
global username 
global primary
global secondary
db.clear()
@app.route('/login')
@app.route('/', methods=["POST","GET"])
def landing():
	global username
	for key in db.keys():
		print((key + str(db[key])))
	if request.method == 'POST':
		#SIGN UP
		if request.form['submit'] == 'signin':
			if model.signup(request.form["newuser"], request.form["newpassword"],request.form["newkey"]) == True:	
				if model.apicheck(request.form["newuser"], request.form["newkey"]) == True:		
					db[request.form["newuser"]]={'theme' : {'primary' : 'light', 'secondary' : {'text':'blue', 'button':'btn-primary btn-lg','collapsible':'collapsibleBlue'}},'stat1':'Hypixel Level','stat2':'Bedwars Star','stat3':'Skywars Star', 'list':[]}
					secondaryB=db[request.form["newuser"]]['theme']['secondary']['button']
					secondaryT=db[request.form["newuser"]]['theme']['secondary']['text']
					db[request.form["newuser"]].update({"password" : request.form["newpassword"]})
					db[request.form["newuser"]].update({"apikey" : request.form["newkey"]})
					username = request.form["newuser"]
					return redirect('/home')

				else:
					return render_template("login.html", error = "API Key does not match username")
			elif model.signup(request.form["newuser"], request.form["newpassword"],request.form["newkey"]) == "Empty":
				return render_template("login.html", error = "Please fill out all parameters")

			
			else:
					return render_template("login.html", error = "account already taken")
		

#hi -ava 
#she doesn't know what to say
#i also do not know what to say :)
#tell her she has ruined my focus
#your welcome :)
#that's not nice ;-;
#I've done it B0ss5
#I made it rainbow :)

		#LOG IN
		elif request.form['submit'] == 'login':
			if request.form['username'] in db.keys():
				if db[request.form['username']]["password"] == request.form['password']:
					
					username = request.form['username']
					
					if model.apicheck(username, db[username]['apikey']) == True:
						return redirect('/home')
					else:
						return render_template("login.html", error="API Key does not match username")
				else:
					return render_template('login.html', error="invalid password")
			else: 
				return render_template('login.html', error="invalid username")
	elif request.method =='GET': 
		return render_template("login.html")

@app.route('/home', methods=["POST","GET"])
def homepage():
	if request.method == "POST":
		db[username]['stat1'] = request.form["stat1"]
		db[username]['stat2'] = request.form['stat2']
		db[username]['stat3'] = request.form['stat3']
		print(db[username])
	else:
		pass
	#theme
	if db[username]['theme']['primary'] == 'dark':
		theme = 'dark'
	elif db[username]['theme']['primary'] == 'light':
		theme = 'light'
	else:
		db[username]['theme'] = 'dark'
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	notable = model.notablePlayers()
	print (notable)
	return render_template('index.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB, notable=notable)

@app.route('/settings', methods=['POST', 'GET'])
def settings():
	try:
		s1default = db[username]['stat1']
		s2default = db[username]['stat2']
		s3default = db[username]['stat3']
	except:
		s1default = "Hypixel Level"
		s2default = "Bedwars Star"
		s3default = "Skywars Star"
	theme = db[username]['theme']['primary']
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	return render_template('settings.html', theme=theme, secondaryT=secondaryT, secondaryB=secondaryB, s3default = s3default, s2default = s2default, s1default = s1default)


@app.route('/lightTheme', methods=['POST', 'GET'])
def light():
	global theme
	db[username]['theme']['primary'] = 'light'
	theme = 'light'
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	print (theme)
	return render_template('settings.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)

@app.route('/darkTheme', methods=['POST', 'GET'])
def dark():
	db[username]['theme']['primary'] = 'dark' 
	theme = 'dark'
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	print (theme)
	return render_template('settings.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)

@app.route("/redSecondary", methods=['POST','GET'])
def red():
	theme = db[username]['theme']['primary']
	db[username]['theme']['secondary'] = {'text':'red','button':"btn-danger btn-lg", 'collapsible':'collapsibleRed'}
	secondaryT = db[username]['theme']['secondary']["text"]
	secondaryB = db[username]['theme']['secondary']['button']
	return render_template('settings.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)
@app.route("/blueSecondary", methods=['POST','GET'])
def blue():
	theme = db[username]['theme']['primary']
	db[username]['theme']['secondary'] = {'text':'blue','button':"btn-primary btn-lg", 'collapsible' :'collapsibleBlue'}
	secondaryT = db[username]['theme']['secondary']["text"]
	secondaryB = db[username]['theme']['secondary']['button']
	return render_template('settings.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)
@app.route("/yellowSecondary", methods=['POST','GET'])
def yellow():
	theme = db[username]['theme']['primary']
	db[username]['theme']['secondary'] = {'text':'yellow','button':"btn-warning btn-lg", 'collapsible': 'collapsibleYellow'}
	secondaryT = db[username]['theme']['secondary']["text"]
	secondaryB = db[username]['theme']['secondary']['button']
	return render_template('settings.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)





@app.route('/search', methods = ["GET", "POST"])
def search():
	global username
	if request.method == "GET":
		theme = db[username]['theme']['primary']
		secondaryT = db[username]['theme']['secondary']['text']
		secondaryB = db[username]['theme']['secondary']['button']
		print (secondaryT)
		print (theme)
		return render_template('search.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)
	else:
		theme = db[username]['theme']['primary']
		secondaryT = db[username]['theme']['secondary']['text']
		secondaryB = db[username]['theme']['secondary']['button']
		secondaryC =  db[username]['theme']['secondary']['collapsible']
		Susername=request.form['Susername']
		status=model.getStatus(Susername, db[username] ['apikey'])
		if status=="Player Does Not Exist":
			theme = db[username]['theme']['primary']
			secondaryT = db[username]['theme']['secondary']['text']
			secondaryB = db[username]['theme']['secondary']['button']
			return render_template('searchError.html', username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)
		else:
			htmldict2 = model.getHtmlDict(Susername, db[username]['apikey'])
			Susername= model.getUsername(Susername)
			def getStat(htmldict, mode, stat):
				return htmldict2['stats'][mode][stat]
			if status[0] == "Online":
				try:
					mode = status[3]
				except:
					mode = status[1]
				try:
					gameMap = status[2]
				except:
					gameMap = "N/A"
				try:
					sw_level = htmldict2["achievements"]["skywars_you_re_a_star"]
				except:
					sw_level = 0
				try:
					sw_kills = getStat(htmldict2, 'SkyWars', 'kills')
				except:
					sw_kills = 0
				try:
					sw_deaths = getStat(htmldict2, "SkyWars", "deaths")
				except:
					sw_deaths=0
				try:
					sw_wins = getStat(htmldict2, "SkyWars", "wins")
				except:
					sw_wins = 0
				try:
					sw_losses = getStat(htmldict2, "SkyWars", "losses")
				except:
					sw_losses=0
				try:
					sw_KD = round((sw_kills/sw_deaths),2)
				except:
					sw_KD = "N/A"
				try:
					sw_WL = round((sw_wins/sw_losses),2)
				except:
					sw_WL = "N/A"
				try:
					bw_level = htmldict2["achievements"]["bedwars_level"]
				except:
					bw_level = 0
				try:
					bw_kills = getStat(htmldict2, "Bedwars", "kills_bedwars")
				except:
					bw_kills = 0
				try:
					bw_deaths = getStat(htmldict2, "Bedwars", "deaths_bedwars")
				except:
					bw_deaths=0
				try:
					bw_wins = getStat(htmldict2, "Bedwars", "wins_bedwars")
				except:
					bw_wins = 0
				try:
					bw_losses = getStat(htmldict2, "Bedwars", "losses_bedwars")
				except:
					bw_losses=0
				try:
					bw_KD = round((bw_kills/bw_deaths),2)
				except:
					bw_KD = "N/A"
				try:
					bw_WL = round((bw_wins/bw_losses),2)
				except:
					bw_WL = "N/A"
				try:
					bw_final_kills = getStat(htmldict2, "Bedwars", "final_kills_bedwars")
				except:
					bw_final_kills = 0
				try:
					bw_final_deaths = getStat(htmldict2, "Bedwars", "final_deaths_bedwars")
				except:
					bw_final_deaths=0
				try:
					bw_final_KD = round((bw_final_kills/bw_final_deaths),2)
				except:
					bw_final_KD = "N/A"
				try: 
					beds_broken = getStat(htmldict2, "Bedwars", "beds_broken_bedwars")
				except:
					beds_broken=0
				bw_color = model.getBwColor(bw_level)
				if bw_level>=1000:
					bw_color1=bw_color[0]
					bw_color2=bw_color[1]
					bw_color3=bw_color[2]
					bw_color4=bw_color[3]
					bw_color5=bw_color[4]
					bw_color6=bw_color[5]
					bw_color7=bw_color[6]
				else:
					bw_color1=bw_color
					bw_color2=bw_color
					bw_color3=bw_color
					bw_color4=bw_color
					bw_color5=bw_color
					bw_color6=bw_color
					bw_color7=bw_color
				sw_color = model.getSwColor(sw_level)
				if isinstance(bw_level,int)==True:
					bw_level=str(bw_level)
				bw_level1=bw_level[0]
				try: 
					bw_level2=bw_level[1]
					try:
						bw_level3=bw_level[2]
						try:
							bw_level4=bw_level[3]
							bw_level5="⭒"
							bw_level6="]"
						except:
							bw_level4="⭒"
							bw_level5="]"
							bw_level6=""
					except:
						bw_level3="⭒"
						bw_level4="]"
						bw_level5=""
						bw_level6=""
				except: 
					bw_level2="⭒"
					bw_level3="]"
					bw_level4=""
					bw_level5=""
					bw_level6=""
				if sw_level>=50:
					sw_color1=sw_color[0]
					sw_color2=sw_color[1]
					sw_color3=sw_color[2]
					sw_color4=sw_color[3]
					sw_color5=sw_color[4]
					sw_color6=sw_color[5]
					sw_color7=sw_color[6]
				else:
					sw_color1=sw_color
					sw_color2=sw_color
					sw_color3=sw_color
					sw_color4=sw_color
					sw_color5=sw_color
					sw_color6=sw_color
					sw_color7=sw_color
				if isinstance(sw_level,int)==True:
					sw_level=str(sw_level)
				sw_level1=sw_level[0]
				try: 
					sw_level2=sw_level[1]
					try:
						sw_level3=sw_level[2]
						try:
							sw_level4=sw_level[3]
							sw_level5="⭒"
							sw_level6="]"
						except:
							sw_level4="⭒"
							sw_level5="]"
							sw_level6=""
					except:
						sw_level3="⭒"
						sw_level4="]"
						sw_level5=""
						sw_level6=""
				except: 
					sw_level2="⭒"
					sw_level3="]"
					sw_level4=""
					sw_level5=""
					sw_level6=""
				return render_template('searchResultsOnline.html',Susername=Susername, sw_wins=sw_wins,sw_losses=sw_losses,gameMap=gameMap,mode=mode,sw_kills=sw_kills,sw_deaths=sw_deaths,sw_KD=sw_KD,sw_WL=sw_WL, sw_level=sw_level,bw_wins=bw_wins,bw_losses=bw_losses,bw_kills=bw_kills,bw_deaths=bw_deaths,bw_KD=bw_KD,bw_WL=bw_WL, bw_level=bw_level,bw_final_KD=bw_final_KD,beds_broken=beds_broken,bw_final_deaths=bw_final_deaths,bw_final_kills=bw_final_kills,sw_color=sw_color,bw_color2=bw_color2,bw_color1=bw_color1,bw_color3=bw_color3,bw_color4=bw_color4,bw_color5=bw_color5,bw_color6=bw_color6,bw_level4=bw_level4,bw_level3=bw_level3,bw_level2=bw_level2,bw_level1=bw_level1,sw_level1=sw_level1,sw_level2=sw_level2,sw_level3=sw_level3,sw_level4=sw_level4,sw_level5=sw_level5,sw_level6=sw_level6,sw_color2=sw_color2,sw_color1=sw_color1,sw_color3=sw_color3,sw_color4=sw_color4,sw_color5=sw_color5,sw_color6=sw_color6,sw_color7=sw_color7,bw_level5=bw_level5,bw_level6=bw_level6,bw_color7=bw_color7, username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB, secondaryC=secondaryC)
			else:
				try:
					sw_level = htmldict2["achievements"]["skywars_you_re_a_star"]
				except:
					sw_level = 0
				try:
					sw_kills = getStat(htmldict2, 'SkyWars', 'kills')
				except:
					sw_kills = 0
				try:
					sw_deaths = getStat(htmldict2, "SkyWars", "deaths")
				except:
					sw_deaths=0
				try:
					sw_wins = getStat(htmldict2, "SkyWars", "wins")
				except:
					sw_wins = 0
				try:
					sw_losses = getStat(htmldict2, "SkyWars", "losses")
				except:
					sw_losses=0
				try:
					sw_KD = round((sw_kills/sw_deaths),2)
				except:
					sw_KD = "N/A"
				try:
					sw_WL = round((sw_wins/sw_losses),2)
				except:
					sw_WL = "N/A"
				try:
					bw_level = htmldict2["achievements"]["bedwars_level"]
				except:
					bw_level = 0
				try:
					bw_kills = getStat(htmldict2, "Bedwars", "kills_bedwars")
				except:
					bw_kills = 0
				try:
					bw_deaths = getStat(htmldict2, "Bedwars", "deaths_bedwars")
				except:
					bw_deaths=0
				try:
					bw_wins = getStat(htmldict2, "Bedwars", "wins_bedwars")
				except:
					bw_wins = 0
				try:
					bw_losses = getStat(htmldict2, "Bedwars", "losses_bedwars")
				except:
					bw_losses=0
				try:
					bw_KD = round((bw_kills/bw_deaths),2)
				except:
					bw_KD = "N/A"
				try:
					bw_WL = round((bw_wins/bw_losses),2)
				except:
					bw_WL = "N/A"
				try:
					bw_final_kills = getStat(htmldict2, "Bedwars", "final_kills_bedwars")
				except:
					bw_final_kills = 0
				try:
					bw_final_deaths = getStat(htmldict2, "Bedwars", "final_deaths_bedwars")
				except:
					bw_final_deaths=0
				try:
					bw_final_KD = round((bw_final_kills/bw_final_deaths),2)
				except:
					bw_final_KD = "N/A"
				try: 
					beds_broken = getStat(htmldict2, "Bedwars", "beds_broken_bedwars")
				except:
					beds_broken=0
				bw_color = model.getBwColor(bw_level)
				if bw_level>=1000:
					bw_color1=bw_color[0]
					bw_color2=bw_color[1]
					bw_color3=bw_color[2]
					bw_color4=bw_color[3]
					bw_color5=bw_color[4]
					bw_color6=bw_color[5]
					bw_color7=bw_color[6]
				else:
					bw_color1=bw_color
					bw_color2=bw_color
					bw_color3=bw_color
					bw_color4=bw_color
					bw_color5=bw_color
					bw_color6=bw_color
					bw_color7=bw_color
				sw_color = model.getSwColor(sw_level)
				if isinstance(bw_level,int)==True:
					bw_level=str(bw_level)
				bw_level1=bw_level[0]
				try: 
					bw_level2=bw_level[1]
					try:
						bw_level3=bw_level[2]
						try:
							bw_level4=bw_level[3]
							bw_level5="⭒"
							bw_level6="]"
						except:
							bw_level4="⭒"
							bw_level5="]"
							bw_level6=""
					except:
						bw_level3="⭒"
						bw_level4="]"
						bw_level5=""
						bw_level6=""
				except: 
					bw_level2="⭒"
					bw_level3="]"
					bw_level4=""
					bw_level5=""
					bw_level6=""
				if sw_level>=50:
					sw_color1=sw_color[0]
					sw_color2=sw_color[1]
					sw_color3=sw_color[2]
					sw_color4=sw_color[3]
					sw_color5=sw_color[4]
					sw_color6=sw_color[5]
					sw_color7=sw_color[6]
				else:
					sw_color1=sw_color
					sw_color2=sw_color
					sw_color3=sw_color
					sw_color4=sw_color
					sw_color5=sw_color
					sw_color6=sw_color
					sw_color7=sw_color
				if isinstance(sw_level,int)==True:
					sw_level=str(sw_level)
				sw_level1=sw_level[0]
				try: 
					sw_level2=sw_level[1]
					try:
						sw_level3=sw_level[2]
						try:
							sw_level4=sw_level[3]
							sw_level5="⭒"
							sw_level6="]"
						except:
							sw_level4="⭒"
							sw_level5="]"
							sw_level6=""
					except:
						sw_level3="⭒"
						sw_level4="]"
						sw_level5=""
						sw_level6=""
				except: 
					sw_level2="⭒"
					sw_level3="]"
					sw_level4=""
					sw_level5=""
					sw_level6=""
				return render_template('searchResultsOffline.html',Susername=Susername, sw_wins=sw_wins,sw_losses=sw_losses,sw_kills=sw_kills,sw_deaths=sw_deaths,sw_KD=sw_KD,sw_WL=sw_WL, sw_level=sw_level,bw_wins=bw_wins,bw_losses=bw_losses,bw_kills=bw_kills,bw_deaths=bw_deaths,bw_KD=bw_KD,bw_WL=bw_WL, bw_level=bw_level,bw_final_KD=bw_final_KD,beds_broken=beds_broken,bw_final_deaths=bw_final_deaths,bw_final_kills=bw_final_kills,sw_color=sw_color,bw_color2=bw_color2,bw_color1=bw_color1,bw_color3=bw_color3,bw_color4=bw_color4,bw_color5=bw_color5,bw_color6=bw_color6,bw_level4=bw_level4,bw_level3=bw_level3,bw_level2=bw_level2,bw_level1=bw_level1,sw_level1=sw_level1,sw_level2=sw_level2,sw_level3=sw_level3,sw_level4=sw_level4,sw_level5=sw_level5,sw_level6=sw_level6,sw_color2=sw_color2,sw_color1=sw_color1,sw_color3=sw_color3,sw_color4=sw_color4,sw_color5=sw_color5,sw_color6=sw_color6,sw_color7=sw_color7,bw_level5=bw_level5,bw_level6=bw_level6,bw_color7=bw_color7,username=username, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB, secondaryC=secondaryC)

@app.route('/listsettings', methods=["POST", "GET"])
def listsettings():
	theme = db[username]['theme']['primary']
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	code = {}
	error = ""
	if request.method == "POST":
		try:
			if request.form["add"] == "add":
				try:
					if model.getUUID(request.form['newplayer']) in 	db[username]['list']:
						error = "That account is already in your list"
					else:
						try:
							nametoadd = model.getUUID(request.form["newplayer"])
							db[username]["list"].append(nametoadd)
						except:
								error = "invalid account!"
				except:
					error = "invalid account!"
		except:
			db[username]["list"].remove(model.getUUID(request.form["remove"]))
	else:
		pass
	for players in db[username]["list"]:
		player = model.getusername(players)
		head = model.getHead(players)
		if players == "5d74806e208c4e2896f9ad9748eca154":
			head = model.getHead("d1857b3bbae84567b6111c69f6b1cf52")
		if player in db[username]["list"]:
			db[username]["list"].remove(player)
			error = "name alreay in list!"
		code.update({player:head})



	return render_template('listsettings.html', code=code, error=error, theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)

@app.route('/plloading')	
def plloading():
	theme = db[username]['theme']['primary']
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']	
	return render_template('loading.html', theme=theme, secondaryT=secondaryT, secondaryB=secondaryB)

@app.route('/playerlist')
def playerlist():
	#get the list from db
	theme = db[username]['theme']['primary']
	secondaryT = db[username]['theme']['secondary']['text']
	secondaryB = db[username]['theme']['secondary']['button']
	statdict = {}
	stat1=db[username]['stat1']
	stat2=db[username]['stat2']
	stat3=db[username]['stat3']
	for player in db[username]['list']:
		player = model.getusername(player)
		statdict[player] = {stat1:model.getAnyStat(model.getHtmlDict(player, db[username]['apikey']), stat1)}
	print (statdict)
	stats = {}
	sortedstats={}
	for player in statdict:
		stats.update({player:statdict[player][stat1]})
	for players in statdict:
		value = 0
		for player in stats: 
			if stats[player]>=value:
				value=stats[player]
				p1 = player
		print (stats)
		sortedstats.update({p1:value})
		stats.pop(p1)
	print(sortedstats)
	onplist={}
	offplist={}
	skinlist ={}
	for player in sortedstats:
		if player == 'StarBoy145':
			skinlist.update({player:model.getModel(model.getUUID('fourvict'))})
		else:
			skinlist.update({player: model.getModel(model.getUUID(player))})
 
	for player in sortedstats:

		status = model.getStatus(player, db[username]['apikey'])
		if isinstance(status, str)==True:
			offplist.update({player: {stat1:sortedstats[player],stat2:model.getAnyStat(model.getHtmlDict(player, db[username]['apikey']), stat2), stat3:model.getAnyStat(model.getHtmlDict(player, db[username]['apikey']), stat3), 'Status':status}})
		else:
			onplist.update({player: {stat1:sortedstats[player],stat2:model.getAnyStat(model.getHtmlDict(player, db[username]['apikey']), stat2), stat3:model.getAnyStat(model.getHtmlDict(player, db[username]['apikey']), stat3), 'Mode':status[1],'Map':status[2]}})
	
	
	return render_template('playerlist.html', onplist=onplist,offplist=offplist, skinlist=skinlist, theme=theme, secondaryB=secondaryB, secondaryT=secondaryT)
app.run(host='0.0.0.0', port=8080, debug=True)
