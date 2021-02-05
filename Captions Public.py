import json
from datetime import datetime
import os
try:
    os.remove('iisc.ugmemes\\iisc.ugmemes.json')
    os.system(
        'cmd /c instagram-scraper iisc.ugmemes -u Username-p Password --comments --latest -T {datetime}')
except :
    os.system('cmd /c instagram-scraper iisc.ugmemes -u Username -p Password --media-metadata --media-type none')

# Instagram Username and Password in above code


fileh = open('iisc.ugmemes\\iisc.ugmemes.json','r',encoding='utf-8')

data = json.load(fileh)


def caption(date_time):

    for element in data['GraphImages']:
        time = datetime.fromtimestamp(int(element['taken_at_timestamp']))
        time = time.strftime("%Y%m%d %Hh%Mm%Ss")

        if time == date_time:
            return element['edge_media_to_caption']['edges'][0]['node']['text']
    else:
        return 'No Caption'

fileh.close()
