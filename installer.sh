#!/bin/bash
echo "Installing google play scraper"
pip3 install google-play-scraper
echo "Installing tweepy"
pip3 install tweepy
echo "First-Time setup"
python3 setup.py
echo "Done! Now run scrape.py whenever you want to check for any Google app update"
echo "Don\'t forget to put your API KEY, SECRET, and ACCESS TOKEN and SECRET inside scrape.py!!"