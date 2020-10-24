#!/bin/bash
echo "Installing google play scraper"
pip install google-play-scraper
echo "Installing tweepy"
pip install tweepy
echo "First-Time setup"
python setup.py
echo "Done! Now run scrape.py whenever you want to check for any Google app update"
echo "Don\'t forget to put your API KEY, SECRET, and ACCESS TOKEN and SECRET inside scrape.py!!"