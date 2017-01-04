# fantasypremierleague-datascience
An experiment to find out the decision making in famous online game - Fantasy Premier League. (FPL)

##Idea
English Premier League (EPL) - one of the famous leagues in sport of football. Most viewed and followed across the globe.
FPL provides opportunity for enthusiasts to try their hand at decision making.
To predict the best set of players who perform every game.
Points are given based on various parameters.
Goal - To get the maximum Team Score every week

##Concept
Data Science provides me an opportunity to understand the dynamics of EPL and FPL.

##Problem Statement

1.Rate a person's decision making ability

2.Assist user for making further decisions

3.Predict the best team 


##Steps

1.Data Acquisition
###Extraction
From FPL / EPL - All the raw data, statistics related to players, teams, points, etc

2.Data Analysis
Using Simple Statistics and Machine Learning (if need be) to analyse every player, team and score

3.Data Visualization
For every user, to make sense of data and to understand the 3 outcomes of the problem, using interactive techniques - graphs,charts,diagrams in an intuitive manner 

##Details
###Extraction
Database -

1. Universe 
Entire data available on EPL, FPL website

2. User data
User's data of Players Selected, Removed, Replaced(Transferred), Considered, Benched, etc

FPL Manager data - 
main_user_id,
main_user_name,
main_user_region,main_user_region_id,
main_user_team_name ,
main_user_started_event,
main_user_favourite_team,


Changing - 
main_user_overall_points,
main_user_overall_rank ,
main_user_bank_value,
main_user_balance ,
main_user_total_transfers

Analysis - User-id based
1. Countries (region wise)
2. Clustering based on Team-names
3. Started event
4. Favourite team

Country vs Team favourite
