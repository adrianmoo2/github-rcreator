from config import *
import requests
import json

# url = "https://api.github.com/users/adrianmoo2/repos?accesstoken="

# url += 

adrianReadMeURL = "https://api.github.com/repos/adrianmoo2/readme-template/readme"

readme = requests.get(adrianReadMeURL)
readmeJSON = readme.json()
readmeContent = readmeJSON['content']


print (readmeJSON['content'])