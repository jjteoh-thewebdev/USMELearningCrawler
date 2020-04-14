import requests
import json
from bs4 import BeautifulSoup
from pathlib import Path
# import mechanise

USM_ELEARNING_URL= "https://elearning.usm.my/sidang1920/"
SETTINGS_FILE = "settings.json"


def initSettings():
    # read file
    with  open(SETTINGS_FILE, 'r') as jsonFile:
        data = jsonFile.read()
    
    return json.loads(data)

SETTINGS = initSettings()

# go to elearning homepage
response = requests.get(USM_ELEARNING_URL)
soup = BeautifulSoup(response.text, "html.parser")

# look for login button span.login > a
loginLink = soup.find("span", class_="login").find('a').get('href')
print(loginLink)

# go to login page


# login


# loop > lookup target courses (a.courselist_course > span)
# go to the link
# div.activityinstance
# download resources 


