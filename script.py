import tweepy

import random

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

#Faut Changer Les Numeros en differentes phrases qui contiennent deux variables aleatoires, cad annee et donnee, qui pointe au .csv et apres c fini lol
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
          
api.update_status(random.sample(list1, 1))
  