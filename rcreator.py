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
    privateInput = input("Private? (y / n): ")
    global privateBool
    if (privateInput == "y"): 
        privateBool = True
    elif (privateInput == "n"):
        privateBool = False
    
    displayValues()
    

while True:
    inputRepoParams()
    if (input("\nAre these values okay? (y / n): ") == "y"):        
        break

if re.match(r'\.$', descriptionInput) is None:
    descriptionInput += "."
descriptionInput += " Made by github-rcreator."

repo = user.create_repo(
    name = nameInput,
    description = descriptionInput,
    private = privateBool
)

print ("Repo created")

# ------- README and local directory creation ------- 

repo.create_file("README.md", "rcreator init commit :)", cleanReadmeText.group(0))

# repoClone = pygit2.clone_repository(repo.git_url, 'C:\\Users\\Adrian\\Desktop\\Job-Stuff\\test-directory')

# ------- Commit -------

# repoClone.remotes.set_url("origin", repo.clone_url)
# index = repoClone.index
# index.add_all()
# # author = pygit2.Signature("Adrian Tran", "me@adriantran.dev")
# # committer = pygit2.Signature("Adrian Tran", "me@adriantran.dev")
# tree = index.write_tree()
# oid = repoClone.create_commit('refs/heads/master', "Adrian Tran", "Adrian Tran", "init commit",tree,[repoClone.head.get_object().hex])
# remote = repoClone.remotes["origin"]
# credentials = pygit2.UserPass(user, password)
# remote.credentials = credentials

# callbacks=pygit2.RemoteCallbacks(credentials=credentials)

# ------- Push -------

# remote.push(['refs/heads/master'],callbacks=callbacks)