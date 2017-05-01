#import gevent
import csv
import json
import requests
import time

gameweek=1
filepath = 'player_data_gw_1_'+str(gameweek)+'.csv'
writer=csv.writer(open(filepath,'wb'))
header=['main_user_id','main_user_gameweek_points','main_user_total_points_till_gw','main_user_gameweek_rank','main_user_rank_till_gw','gw_team','gw_captain','gw_vice_captain','triple_captain']
writer.writerow(header)

#for some other Response
#header=['main_user_id','main_user_name','main_user_region','main_user_region_id','main_user_overall_points','main_user_overall_rank ','main_user_team_name ','main_user_bank_value','main_user_balance ','main_user_started_event','main_user_favourite_team','main_user_total_transfers' ]

#create new csv for every gameweek

player_data_per_gw=[]
row1=[]
for main_user_id in range(1,4546257):
	response=''
	while response == '':
		try:
			#url="10.0.0.0"
			url="https://fantasy.premierleague.com/drf/entry/"+str(main_user_id)+"/event/"+str(gameweek)+"/picks"
			response = requests.get(url)
		except:
			print "Connection refused"
			time.sleep(5)
			continue
	player_data_per_gw.append(main_user_id)
	if(response.status_code!=200):
		print "na"
		player_data_per_gw.append("empty")
	else:
		print "200"
		json_data = json.loads(response.text)
		if(main_user_id==1):
			#store the game week values only once (hence for first user)
			gw_highest_scoring_user = json_data["event"]["highest_scoring_entry"]
			gw_highest_score = json_data["event"]["highest_score"]
			gw_average_score = json_data["event"]["average_entry_score"]			
			row1.append(gw_highest_score)
			row1.append(gw_highest_scoring_user)
			row1.append(gw_average_score)
			writer.writerow(row1)
		#for every user store following data
		main_user_gameweek_points = json_data["entry_history"]["points"]
		main_user_total_points_till_gw = json_data["entry_history"]["total_points"]
		main_user_gameweek_rank =  json_data["entry_history"]["rank"]
		main_user_rank_till_gw =   json_data["entry_history"]["overall_rank"]

		gw_team=[]
		triple_captain=0
		for player in json_data["picks"]:
			gw_team.append(player["element"])
			if player["is_captain"]:
				gw_captain=player["element"]
			if player["is_vice_captain"]:
				gw_vice_captain=player["element"]
			if(player["multiplier"]==3):
				triple_captain=1

		player_data_per_gw.append(main_user_gameweek_points)
		player_data_per_gw.append(main_user_total_points_till_gw)
		player_data_per_gw.append(main_user_gameweek_rank)
		player_data_per_gw.append(main_user_rank_till_gw)
		player_data_per_gw.append(gw_team)
		player_data_per_gw.append(gw_captain)
		player_data_per_gw.append(gw_vice_captain)
		player_data_per_gw.append(triple_captain)
	writer.writerow(player_data_per_gw)
	player_data_per_gw=[]
	gw_team=[]
