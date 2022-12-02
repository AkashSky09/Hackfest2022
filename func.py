import os
import re
import json
from bs4 import BeautifulSoup


directory ='C:\\Users\\AJagadish\\Desktop\\Func'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
            soup = BeautifulSoup(f.read(),'html.parser')
            jsonData = open('ref.json')
            data = json.load(jsonData)
            #mydivs = soup.find_all("a", {"class": "version-tag"},)
            for versionKey in data:
                elms = soup.select("a."+versionKey)
                for i in elms:
                    url_data = i.attrs["href"]
                    s = [float(s) for s in re.findall(r'-?\d+\.?\d*', url_data)]
                    ddd = url_data.replace(str(s[0]), data[versionKey])
                    print(ddd)
            
