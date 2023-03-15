#!/usr/bin/env python
# coding: utf-8

# In[10]:


"""import requests
import pandas as pd
import json
import ast
import yaml

def process_yaml():
    with open("../config.yaml") as file:
        return yaml.safe_load(file)

def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    (url, resultFileName) = create_twitter_url()
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token, url)

    tweets = res_json["data"]
    for t in tweets:
        print(t)
        
    from datetime import datetime

    # get current date and time
    current_date = datetime.today().date()
    
    #print("Current date & time : ", current_datetime)

    # convert datetime obj to string
    str_current_date = str(current_date)
    
    #with open(resultFileName, 'w', encoding='utf-8') as f:
    with open(resultFileName+str_current_date+".json", 'w', encoding='utf-8') as f: #/!/ append dico mais remet result_count et ouverture/fermeture dico
        json.dump(res_json, f, ensure_ascii=False, indent=4)
        

def create_twitter_url():
    #tweets sur la réforme des retraites : #ReformesDesRetraites, 
    #ou contenant "réforme" et "retraite"
    #ou contenant "retraite" + 1 autre indice : Macron, @EmmanuelMacron, @Elisabeth_Borne, projet, âge, #greve, #grevegenerale, #Macron, #MacronDemission
    #RT exclus
    
    url = 'https://api.twitter.com/2/tweets/search/recent?max_results=100&query=(%23reformedesretraites%20OR%20réforme%20retraite%20OR%20retraite%20(macron%20OR%20to:EmmanuelMacron%20OR%20to:Elisabeth_Borne%20OR%20projet%20OR%20âge%20OR%20%23greve%20OR%20%23grevegenerale%20OR%20%23macron%20OR%20%23macrondemission))-is:retweet&tweet.fields=author_id,created_at,public_metrics,lang,entities&user.fields=location,public_metrics,created_at&place.fields=country,name&expansions=attachments.media_keys'
    #url = 'https://api.twitter.com/2/tweets/search/recent?max_results=10&query=retraite%20(macron%20OR%20to:EmmanuelMacron%20OR%20to:Elisabeth_Borne%20OR%20projet%20OR%20âge%20OR%20%23greve%20OR%20%23grevegenerale%20OR%20%23macron%20OR%20%23macrondemission)'
    resultFileName = 'corpus_projet/100_tweets_projet' 
    
    return (url, resultFileName)



if __name__ == "__main__":
    main()"""


# In[9]:


import requests
import pandas as pd
import json
import ast
import yaml
import schedule
import time

def process_yaml():
    with open("../config.yaml") as file:
        return yaml.safe_load(file)

def create_bearer_token(data):
    return data["search_tweets_api"]["bearer_token"]

def twitter_auth_and_connect(bearer_token, url):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    response = requests.request("GET", url, headers=headers)
    return response.json()

def main():
    (url, resultFileName) = create_twitter_url()
    data = process_yaml()
    bearer_token = create_bearer_token(data)
    res_json = twitter_auth_and_connect(bearer_token, url)

    tweets = res_json["data"]
    for t in tweets:
        print(t)
                
        # import module => mettre date dans nom fichier
    from datetime import datetime

    current_date = datetime.today()
    
    #print("Current date & time : ", current_datetime)

    # convert datetime obj to string
    str_current_date = str(current_date)[:13].replace(" ","_")
    
    #with open(resultFileName, 'w', encoding='utf-8') as f:
    with open(resultFileName+str_current_date+".json", 'w', encoding='utf-8') as f: #/!/ append dico mais remet result_count et ouverture/fermeture dico
        json.dump(res_json, f, ensure_ascii=False, indent=4)
        

def create_twitter_url():
    #tweets sur la réforme des retraites : #ReformesDesRetraites, 
    #ou contenant "réforme" et "retraite"
    #ou contenant "retraite" + 1 autre indice : Macron, @EmmanuelMacron, @Elisabeth_Borne, projet, âge, #greve, #grevegenerale, #Macron, #MacronDemission
    #RT exclus
    
    url = 'https://api.twitter.com/2/tweets/search/recent?max_results=100&query=(%23reformedesretraites%20OR%20réforme%20retraite%20OR%20retraite%20(macron%20OR%20to:EmmanuelMacron%20OR%20to:Elisabeth_Borne%20OR%20projet%20OR%20âge%20OR%20%23greve%20OR%20%23grevegenerale%20OR%20%23macron%20OR%20%23macrondemission))-is:retweet lang:fr&expansions=attachments.poll_ids,attachments.media_keys,author_id,entities.mentions.username,geo.place_id,in_reply_to_user_id,referenced_tweets.id,referenced_tweets.id.author_id&user.fields=location,public_metrics,created_at&place.fields=country,name&tweet.fields=author_id,created_at,public_metrics,lang,entities'
    #url = 'https://api.twitter.com/2/tweets/search/recent?max_results=10&query=retraite%20(macron%20OR%20to:EmmanuelMacron%20OR%20to:Elisabeth_Borne%20OR%20projet%20OR%20âge%20OR%20%23greve%20OR%20%23grevegenerale%20OR%20%23macron%20OR%20%23macrondemission)'
    resultFileName = '/home/fanny/Documents/M2/cognition/Projet/corpus_projet_plus/100_tweets_projet_plus' 
    
    return (url, resultFileName)

def open_twitter():
# first import the module
    import webbrowser
      
    # then make a url variable
    url = "https://twitter.com/home"
      
    # then call the default open method described above
    webbrowser.open(url)

schedule.every(4).hours.do(open_twitter)
schedule.every(4).hours.do(main)

while 1:
    schedule.run_pending()
    time.sleep(1)

""""if __name__ == "__main__":
    # first import the module
    import webbrowser
      
    # then make a url variable
    url = "https://twitter.com/home"
      
    # then call the default open method described above
    webbrowser.open(url)
    main()"""

