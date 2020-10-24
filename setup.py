from google_play_scraper import app
import json

#auth = tweepy.OAuthHandler("API Key", "API Secret")
#auth.set_access_token("Access Token", "Access Token Secret")
#api = tweepy.API(auth)

## apps.json contains a list of all Google apps with their last update value
apps = open("important_list.json", "r")
updated_apps = json.load(apps)
apps.close()
#print(updated_apps)
an_app_got_an_update = False

for i in updated_apps:
	print("Setting up: " + i)
	app_info = app(i)
	
	if app_info['updated'] > updated_apps[i]:
		an_app_got_an_update = True
		updated_apps[i] = app_info['updated']

if (an_app_got_an_update):
	apps = open("important_list.json", "w")
	json.dump(updated_apps, apps)
	apps.close()