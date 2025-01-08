import tkinter as tk
from tkinter import filedialog
from github import Github
import stat
import os
import git
import subprocess
import shutil
from envVar import GITHUB_KEY

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

# show window  for choosing folder
root = tk.Tk()
root.withdraw()

#get folder path
folder_path = filedialog.askdirectory()

#if folder selected
if folder_path:
    items = os.listdir(folder_path) #get contents

    if(".git" in items):#if already git repo, delete it
        git_repo_path = os.path.join(folder_path, ".git")
        try:
            shutil.rmtree(git_repo_path, onerror=remove_readonly) 
            print("The Git repository has been removed.")
        except Exception as e:
            print(f"Error while deleting the .git folder: {e}")

    items = os.listdir(folder_path)#get contents again
    if ".gitignore"in items: 
        items.remove(".gitignore")#removes gitignore from list

    #make a git repo
    try:
        subprocess.run(["git", "init"], cwd=folder_path, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error while initializing Git repository: {e}")


    while(len(items) > 0):
        committing_item = items[-1].removesuffix("\n")
        items = items[0:-1]
        subprocess.run(["git", "add", f"{committing_item}"], cwd=folder_path, check=True)
        subprocess.run(["git", "commit", "-m", f"Added file '{committing_item}'",], cwd=folder_path, check=True)
        committing_item_path = os.path.join(folder_path, committing_item)
        date_modified = os.path.getmtime(committing_item_path)
        subprocess.run(["git", "commit", "--amend", "-m", f"Added file '{committing_item}'", f'--date="{date_modified}"',], cwd=folder_path, check=True)
        print(f"{committing_item} commited at {date_modified}. path was {committing_item_path}")

    try:
        folder_name = os.path.basename(folder_path)
        ghub = Github(GITHUB_KEY)

        user = ghub.get_user()

        repo = user.create_repo(folder_name)
        print(f"Repo {folder_name} created for {user} ")
    except Exception as e:
        print(e)
    
    subprocess.run(["git", "remote", "add", "origin", f"{repo.html_url}"], cwd=folder_path, check=True)
    subprocess.run(["git", "push", "-u", "origin", "master"], cwd=folder_path, check=True)


