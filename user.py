import numpy as np
import csv
import json
import requests

userid=1000000
#3146257
# main_user_id = []
# main_user_name = []
# main_user_region = []
# main_user_region_id = []
# main_user_overall_points = []
# main_user_overall_rank = []
# main_user_team_name = []
# main_user_bank_value =  []
# main_user_balance =[]
# main_user_started_event =[]
# main_user_favourite_team =[]
# main_user_total_transfers =[]

filepath = 'data18.csv'
writer=csv.writer(open(filepath,'wb'))
header=['main_user_id','main_user_name','main_user_region','main_user_region_id','main_user_overall_points','main_user_overall_rank ',
'main_user_team_name ','main_user_bank_value','main_user_balance ','main_user_started_event','main_user_favourite_team','main_user_total_transfers'
]

#for word in header:
writer.writerow(header)


actual_data=[]

for counter in range(254849,userid):
	try:
	
		response = requests.get("https://fantasy.premierleague.com/drf/entry/"+str(counter))
		json_data = json.loads(response.text)
	
	except Exception, e:
		print("no data")
	else:
	
		actual_data.append(json_data["entry"]["id"])
		
		username= json_data["entry"]["player_first_name"] + ' '+json_data["entry"]["player_last_name"]
	 	s = username.encode('ascii', 'ignore').decode('ascii')
		actual_data.append(str(s))

		actual_data.append(str(json_data["entry"]["player_region_name"].encode('ascii', 'ignore').decode('ascii')))
		actual_data.append(json_data["entry"]["player_region_id"])
		actual_data.append(json_data["entry"]["summary_overall_points"])
		actual_data.append(json_data["entry"]["summary_overall_rank"])
		actual_data.append(str(json_data["entry"]["name"].encode('ascii', 'ignore').decode('ascii')))
		actual_data.append(json_data["entry"]["value"])
		actual_data.append(json_data["entry"]["bank"])
		actual_data.append(json_data["entry"]["started_event"])
		actual_data.append(json_data["entry"]["favourite_team"])
		actual_data.append(json_data["entry"]["total_transfers"])
		print counter
		
		#for word in actual_data:
		writer.writerow(actual_data)

		actual_data=[]
	finally:
		pass


# main_user_id_arr = np.array(main_user_id)
# main_user_name_arr = np.array(main_user_name)
# main_user_region_arr = np.array(main_user_region)
# main_user_region_id_arr = np.array(main_user_region_id)
# main_user_overall_points_arr = np.array(main_user_overall_points)
# main_user_overall_rank_arr = np.array(main_user_overall_rank)
# main_user_team_name_arr = np.array(main_user_team_name)
# main_user_bank_value_arr =  np.array(main_user_bank_value)
# main_user_balance_arr =np.array(main_user_balance)
# main_user_started_event_arr =np.array(main_user_started_event)
# main_user_favourite_team_arr =np.array(main_user_favourite_team)
# main_user_total_transfers_arr =np.array(main_user_total_transfers)

# np.savetxt('data2.csv', (main_user_id_arr,main_user_name_arr), delimiter=',')

#main_user_id_arr,main_user_name_arr,main_user_region_arr,
	# main_user_region_id_arr,main_user_overall_points_arr,
	# main_user_overall_rank_arr,
	# main_user_team_name_arr,main_user_bank_value_arr,main_user_balance_arr,
	# main_user_started_event_arr,main_user_favourite_team_arr,main_user_total_transfers_arr
