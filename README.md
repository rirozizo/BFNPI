# BFNPI
 Bug Fixes aNd Performance Improvements Twitter Bot

# Purpose
Just to poke fun at Google's obscure changelogs whenever they update one of their apps.

# What is it?

This is a Twitter bot that checks if a Google app has been updated with "Bug fixes and Performance improvements" as a changelog on the Playstore. If so, it tweets on @BFNPI.

# How to use it?

First, run the `installer.sh` file:
```
sh installer.sh
```

Then whenever you want to check for an app update, run:
```
python scrape.py
```

You can add the above command to crontab, if you want to run this on root's crontab, you're gonna have to reinstall using sudo.
