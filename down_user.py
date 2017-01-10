#from __future__ import print_function
import gevent
from gevent import monkey,pool

# patches stdlib (including socket and ssl modules) to cooperate with other greenlets
monkey.patch_all()
#import sys

import csv
import json
import requests

userid=3000000

filepath = '201300data.csv'
writer=csv.writer(open(filepath,'wb'))

header=['main_user_id','main_user_name','main_user_region','main_user_region_id','main_user_overall_points','main_user_overall_rank ',
'main_user_team_name ','main_user_bank_value','main_user_balance ','main_user_started_event','main_user_favourite_team','main_user_total_transfers'
]

writer.writerow(header)

error=[]


jobs=[]
p = pool.Pool(70)

#for counter in range(900000,userid):

def make_request(counter):
	try:
	
		response = requests.get("https://fantasy.premierleague.com/drf/entry/"+str(counter))
		json_data = json.loads(response.text)
	
	except Exception, e:
		print("no data"+str(counter))
		print e
		error.append(counter)
	else:
		actual_data=[]	
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
		
		writer.writerow(actual_data)

		actual_data=[]
	finally:
		pass

#jobs = [gevent.spawn(make_request, counter) for counter in range(900000,userid)]
for counter in range(2010409,userid):
    jobs.append(p.spawn(make_request, counter))
gevent.joinall(jobs)
jobs=[]
for counter in error:
    jobs.append(p.spawn(make_request, counter))
gevent.joinall(jobs)
