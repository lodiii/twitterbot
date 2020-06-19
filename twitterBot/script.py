import tweepy

import random

import csv

import schedule

import time

auth = tweepy.OAuthHandler("V971oAexc7MRbys5AwQEF5DI3", 
    "hGSvD5DDfgfgp327BWZoVECjmSvFR22qWXux9nqAdTOFgaWVFs")
auth.set_access_token("1271078448002478081-MYm2S22wLa5tFJAtAR6pvC2iQTiYum", 
    "XpwppnGBRhaBdYMNWvWN7FukvbbfzQgFNxpwEQ3RhaLRB")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Auth OK")
except:
    print("Auth Error")

results = []
with open("finalDATA.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        results.append(row)
        
randomR = random.choice(results)

myList = [f'In {randomR[1]}, {randomR[2]} casualties due to HIV/AIDS were recorded in {randomR[0]}.',f'{randomR[0]} recorded an approximate of {randomR[2]} deaths related to HIV/AIDS in {randomR[1]}.',f'HIV/AIDS was responsible for more than {randomR[2]} deaths in {randomR[1]}, in {randomR[0]}.',f'At the end of {randomR[1]} it was reported that {randomR[2]} people died due to HIV/AIDS in {randomR[0]}.',f'More than {randomR[2]} people died in {randomR[1]} in {randomR[0]}. The cause was HIV or AIDS. This shows us the gravity of the situation.',f'If people had been more educated on HIV and AIDS, the death toll of {randomR[1]} in {randomR[0]} - {randomR[2]} - would have certainly been lower.',f'At the end of {randomR[1]}, more than {randomR[2]} deaths were reported in {randomR[0]}.',f'In {randomR[0]}, more than {randomR[2]} deaths by HIV/AIDS were recorded at the end of {randomR[1]}. This is largely due to a lack of education/protection.',f'The Government registered an approximate of {randomR[2]} deaths due to HIV/AIDS in {randomR[0]}, at the end of {randomR[1]}.']

api.update_status(random.choice(myList))
    


  