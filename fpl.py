import json
import requests

main_user_id = 3146257

# response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-static")
# json_data = json.loads(response.text)

# players = []
# player_info = []
# for element in json_data["elements"]:
# 	full_name = element["first_name"]+' '+element["second_name"]
# 	s = full_name.encode('ascii', 'ignore').decode('ascii')
# 	a = element["id"]
# 	b = element["team_code"]
# 	c = element["total_points"]
# 	player_info.append(str(s))
# 	player_info.append(str(a))
# 	player_info.append(str(b))
# 	player_info.append(str(c))
# 	players.append(player_info)
# 	player_info=[]
# print(players)

gameweek=17
# response = requests.get("https://fantasy.premierleague.com/drf/entry/"+str(main_user_id)+"/event/"+str(gameweek)+"/picks")
# json_data = json.loads(response.text)

# main_user_gameweek_points = json_data["entry_history"]["points"]
# main_user_total_points_till_gw = json_data["entry_history"]["total_points"]
# main_user_gameweek_rank =  json_data["entry_history"]["rank"]
# main_user_rank_till_gw =   json_data["entry_history"]["overall_rank"]
# gw_highest_scoring_user = json_data["event"]["highest_scoring_entry"]
# gw_highest_score = json_data["event"]["highest_score"]
# gw_average_score = json_data["event"]["average_entry_score"]

# gw_team=[]
# for player in json_data["picks"]:
# 	gw_team.append(player["element"])
# 	if player["is_captain"]:
# 		gw_captain=player["element"]
# 	if player["is_vice_captain"]:
# 		gw_vice_captain=player["element"]
# print(gw_team)
# print(gw_captain)
# print(gw_vice_captain)


# response = requests.get("https://fantasy.premierleague.com/drf/event/"+str(gameweek)+"/live")
# json_data = json.loads(response.text)
# all_fixtures=[]
# fixtures={}
# for fixture in json_data["fixtures"]:
# 	fixtures["home_team"]=fixture["team_h"]
# 	fixtures["away_team"]=fixture["team_a"]
# 	fixtures["home_team_score"]=fixture["team_h_score"]
# 	fixtures["away_team_score"]=fixture["team_a_score"]
	
# 	bonus_players_home={}
# 	bonus_players_away={}

# 	for player in fixture["stats"][8]["bonus"]["h"]:
# 		bonus_players_home[player["element"]] = player["value"]

# 	for player in fixture["stats"][8]["bonus"]["a"]:
# 		bonus_players_away[player["element"]] = player["value"]

# 	fixtures["bonus_players_home"]=bonus_players_home
# 	fixtures["bonus_players_away"]=bonus_players_away

# 	yellow_card_home={}
# 	yellow_card_away={}
# 	red_card_home={}
# 	red_card_away={}

# 	for player in fixture["stats"][5]["yellow_cards"]["h"]:
# 		yellow_card_home[player["element"]] = player["value"]	

# 	for player in fixture["stats"][5]["yellow_cards"]["a"]:
# 		yellow_card_away[player["element"]] = player["value"]

# 	for player in fixture["stats"][6]["red_cards"]["h"]:
# 		red_card_home[player["element"]] = player["value"]	

# 	for player in fixture["stats"][6]["red_cards"]["a"]:
# 		red_card_away[player["element"]] = player["value"]

# 	fixtures["yellow_card_home"]=yellow_card_home
# 	fixtures["yellow_card_away"]=yellow_card_away
# 	fixtures["red_card_home"]=red_card_home
# 	fixtures["red_card_away"]=red_card_away

# 	saves_home={}
# 	saves_away={}

# 	for player in fixture["stats"][7]["saves"]["h"]:
# 		saves_home[player["element"]] = player["value"]


# 	for player in fixture["stats"][7]["saves"]["a"]:
# 		saves_away[player["element"]] = player["value"]

# 	fixtures["saves_home"]=saves_home
# 	fixtures["saves_away"]=saves_away
	
# 	#could hv done List in List, Dict in Dict, List in Dict or Dict in List

# 	#fixtures_list = [ [k,v] for k, v in fixtures.items() ]
# 	all_fixtures.append(fixtures)
# 	fixtures={}

# print all_fixtures


response = requests.get("https://fantasy.premierleague.com/drf/bootstrap-dynamic")

r2 = response.json()

json_data = json.loads(response.text)


print r2


# print main_user_name
# print main_user_favourite_team
# print main_user_region

# next_gw_fixtures=[]
# fixture_detail={}
# for fixture in json_data["next_event_fixtures"]:
# 	fixture_detail["home_team"]=fixture["team_h"]
# 	fixture_detail["away_team"]=fixture["team_a"]
# 	fixture_detail["week"]=fixture["event"]
# 	next_gw_fixtures.append(fixture_detail)
# 	fixture_detail={}
# print next_gw_fixtures













#from bs4 import BeautifulSoup
#html_doc = urllib2.urlopen("https://fantasy.premierleague.com/drf/bootstrap-static").read()
#print(html_doc[1])
#print(html_doc["elements"][0]["id"])
#jsonelement = html_doc["elements"]
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup)
#results = soup.find_all('div')
#results = soup.findAll("div", {"class" : "ism-element__name"})
#for result in results :
    #print result
#class="ismjs-menu ism-element__menu"
#print(results)