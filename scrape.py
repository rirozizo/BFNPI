## TODO: Add a setup script that will act as a first-time setup to update the json file without doing anything else
## TODO: Iterate through the list of Google apps (or at least, the important apps) and check each one and update its value

from google_play_scraper import app
import tweepy
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

## Check if "Bug fixes and Performance Improvements" are in the changes
def BFPI(changes):
		if "bug fixes and performance improvements" in str.lower(changes) or "bug fixes & performance improvements" in str.lower(changes) or "bug fixes and stability improvements" in str.lower(changes) or "bug fixes & stability improvements" in str.lower(changes):
			return True


## Get info about an app
for i in updated_apps:
	print("Checking: " + i)
	app_info = app(i)
	#print(app_info)

## If the app has gotten an update since its last check
	if app_info['updated'] > updated_apps[i]:
		if BFPI(app_info['recentChanges']):
			print(app_info['title'] + " has been updated!: https://play.google.com/store/apps/details?id=" + i + " \n " + app_info['recentChanges'])
			#api.update_status(app_info['title'] + " has been updated!: https://play.google.com/store/apps/details?id=" + i + " \n " + app_info['recentChanges'])
		an_app_got_an_update = True
		updated_apps[i] = app_info['updated']

## If any app got an update, then update the json file with the new values
if (an_app_got_an_update):
	apps = open("important_list.json", "w")
	json.dump(updated_apps, apps)
	apps.close()