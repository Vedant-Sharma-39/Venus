import os
import re

def getpath(date):
    def get(yyyymmdd,list):

        time = re.compile(yyyymmdd)
        list = filter(time.match,list)
        return list

    y = os.listdir('iisc.ugmemes')
    z = get(date,y)
    s = []
    for word in z:
        s.append(word)
    return s

