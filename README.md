# Venus
A Discord Bot


How this bot works.
Uses:
1. Discord.py
2.Instagram-scraper

Instagram-scraper downloads the Images and comment/meta-data from IG(InstaGram).
While Discord.py handles the communication with Discord bot.

The Pathfinder file gets list[array type datastructure in Python] of image-names from the folder where instagram-scraper saved them with date and time of their upload as their names.

The Captions file helps to find the Caption from the  json file made by instagram-scraper. (-- media-metadata | also --comments can be used)
By converting the date given to unix-timestamp then matching corresponding post in json file and extracting the owner's caption from that.

Bot file has regular responding on event code and some regular expression code for user message recognization.
It also has a small code for converting 'today' into date for Pathfinder.



