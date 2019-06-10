from config import *
import requests
import base64
import json
import re
from github import Github
import pygit2

# ------- Pull README template and extract template portion ------- 

url = "https://raw.githubusercontent.com/adrianmoo2/readme-template/master/README.md"

readme = requests.get(url)
readmeText = str(readme.text)

cleanReadmeText = re.search(r'^# \*Project title\*(.|\n)+\/LICENSE\)\.$', readmeText, re.MULTILINE)


# ------- Github repo creation (change access_token value) ------- 

g = Github(access_token)
user = g.get_user()

nameInput = ""
descriptionInput = ""
privateInput = ""
privateBool = True

def displayValues():
    global nameInput
    global descriptionInput
    global privateInput

    print ("\nHere are your inputted values:")
    print ("Name: " + nameInput)
    print ("Description: " + descriptionInput)
    print ("Private: " + privateInput)

    

def inputRepoParams():
    global nameInput
    nameInput = input("Desired name: ")
    global descriptionInput
    descriptionInput = input("Desired description: ")
    global privateInput 
    privateInput = input("Private? (yes / no): ")
    global privateBool
    if (privateInput == "yes"): 
        privateBool = True
    elif (privateInput == "no"):
        privateBool = False
    
    displayValues()
    

while True:
    inputRepoParams()
    if (input("\nAre these values okay? (yes / no): ") == "yes"):
        break

if re.match(r'\.$', descriptionInput) is None:
    descriptionInput += "."
descriptionInput += " Repo made by github-rcreator."

repo = user.create_repo(
    name = nameInput,
    description = descriptionInput,
    private = privateBool
)

print ("Repo created")

# ------- README and local directory creation ------- 

#repo.create_file("/README.md", "rcreator init commit :)", str(cleanReadmeText))