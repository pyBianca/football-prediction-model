import pandas as pd


paok_dict={
    "date_time":["2026-01-18","2026-01-11","2026-01-03","2025-12-21"],
    "home":["ael","paok","osfp","paok"],
    "away":["paok","ofi","paok",'levadiakos'],
    "score":["1:2","2:0","3:1","2:2"]
}

aris_dict={
    "date_time":["2026-01-18","2026-01-10","2026-01-04","2025-12-21"],
    "home":["aris","kifisia","aris","iraklis"],
    "away":["osfp","aris","ofi",'aris'],
    "score":["1:1","2:3","3:1","0:0"]
}

#metatrepste ta 2 dicts se 2 dataframe

paok_df=pd.DataFrame(paok_dict)
aris_df=pd.DataFrame(aris_dict)

print(paok_df)
print ("")
print (aris_df)
#print(paok_df.info())
print ("------------Lets start-----------------")
home_goals_list=[]
away_goals_list=[]
goals_list=[]

for i in range (0,len(paok_df["score"])):
    score=paok_df["score"].iloc[i]
    home_goals=int(score[0])
    away_goals=int(score[-1])
    goals=home_goals+away_goals
    home_goals_list.append(home_goals)
    away_goals_list.append(away_goals)
    goals_list.append(goals)

paok_df["home_goals"]=home_goals_list
paok_df["away_goals"]=away_goals_list
paok_df["goals"]=goals_list


home_goals_list=[]
away_goals_list=[]
goals_list=[]

for i in range (0,len(aris_df["score"])):
    score=aris_df["score"].iloc[i]
    home_goals=int(score[0])
    away_goals=int(score[-1])
    goals=home_goals+away_goals
    home_goals_list.append(home_goals)
    away_goals_list.append(away_goals)
    goals_list.append(goals)

aris_df["home_goals"]=home_goals_list
aris_df["away_goals"]=away_goals_list
aris_df["goals"]=goals_list
print(paok_df)
print ("")
print (aris_df)

print("")
paok_mean=paok_df["goals"].mean()
print(f"The nean of PAOK goales is {paok_mean}")

aris_mean=aris_df["goals"].mean()
print(f"The nean of ARIS goales is {aris_mean}")

sinoliko_mean=(paok_mean+ aris_mean)/2
print (f"I provlepsi tou x   einai {sinoliko_mean}")

sin_mean=0.65*paok_mean+0.35*aris_mean #vari,den einai isaksia ( ta vari prepei naexoun athrisma 1)
print (f"I provlepsi tis bianca  einai {sin_mean}") 

weights_time=[0.4,0.3,0.2,0.1]
paok_mean_weights=0
for i in range(0,len(paok_df["goals"])):
    paok_mean_weights=paok_mean_weights+paok_df["goals"].iloc[i]*weights_time[i] #ama einai lista den thelei . iloc
print(f"The nean of PAOK goales whith vari is {round(paok_mean_weights,3)}")   

aris_mean_weights=0
for i in range(0,len(paok_df["goals"])):
    aris_mean_weights=aris_mean_weights+aris_df["goals"].iloc[i]*weights_time[i] #ama einai lista den thelei . iloc
print(f"The nean of ARIS goales with vari  is {round(aris_mean_weights,3)}")  

sin_mean_weights=0.65*paok_mean_weights+0.35*aris_mean_weights
print (f"I provlepsi tis bianca  einai {sin_mean_weights}") 