from config import *
import requests
import base64
import json
import re
from github import Github


url = "https://raw.githubusercontent.com/adrianmoo2/readme-template/master/README.md"

readme = requests.get(url)
readmeText = str(readme.text)

cleanReadmeText = re.search(r'^# \*Project title\*(.|\n)+\/LICENSE\)\.$', readmeText, re.MULTILINE)

g = Github(access_token)
user = g.get_user()

repo = user.create_repo("test-repo")

# adrianReadMeURL = "https://api.github.com/repos/adrianmoo2/readme-template/readme"

# readme = requests.get(adrianReadMeURL)
# readmeJSON = readme.json()
# readmeContents = readmeJSON['content']

# readmeInfo = base64.decodestring(readmeContents)

# print (readmeInfo)