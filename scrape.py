from google_play_scraper import app
import tweepy
import json

#auth = tweepy.OAuthHandler("API Key", "API Secret")
#auth.set_access_token("Access Token", "Access Token Secret")
#api = tweepy.API(auth)

apps = open("apps.json", "r")
updated_apps = json.load(apps)
apps.close()
#print(updated_apps)
an_app_got_an_update = False

def BFPI(changes):
		if "bug fixes and performance improvements" in str.lower(changes) or "bug fixes & performance improvements" in str.lower(changes) or "bug fixes and stability improvements" in str.lower(changes) or "bug fixes & stability improvements" in str.lower(changes):
			return True


gmail = app('com.google.android.gm')
#print(gmail)
print(gmail['title'])
print(gmail['recentChanges'])
print(gmail['updated'])

if gmail['updated'] > updated_apps['gmail']:
	if BFPI(gmail['recentChanges']):
		print("Gmail has been updated!: https://play.google.com/store/apps/details?id=com.google.android.gm \n " + gmail['recentChanges'])
		#api.update_status("Gmail has been updated!: \n " + gmail['recentChanges'])
		an_app_got_an_update = True
		updated_apps["gmail"] = gmail['updated']

truecaller = app('com.truecaller')
#print(truecaller)
print(truecaller['title'])
print(truecaller['recentChanges'])
print(truecaller['updated'])

if truecaller['updated'] > updated_apps['truecaller']:
	if BFPI(truecaller['recentChanges']):
		print("Truecaller has been updated!: https://play.google.com/store/apps/details?id=com.truecaller \n " + truecaller['recentChanges'])
		#api.update_status("Truecaller has been updated!: \n " + truecaller['recentChanges'])
		an_app_got_an_update = True
		updated_apps["truecaller"] = truecaller['updated']

if (an_app_got_an_update):
	apps = open("apps.json", "w")
	json.dump(updated_apps, apps)
	apps.close()