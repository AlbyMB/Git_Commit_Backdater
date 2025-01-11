# Git Commit Backdater

Git Commit Backdater is a Python script that helps students and developers upload old projects or coursework to GitHub with a (somewhat) accurate commit history. The script :
* initializes a Git repository, 
* commits files based on their last modified dates, 
* and creates a corresponding GitHub repository, ensuring that your GitHub contribution chart reflects your historical work.

## Prerequisites
* Python 3.6+
* Git installed on your system.
* `PyGithub` library installed:

	```bash
	pip install PyGithub
	```
* A GitHub account with a [Personal Access Token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token). Remember to set Administration permissions to 'Read and Write' under Permission -> Repository Permissions
## How to use

* You can either clone this repo or just copy the python code.
* Remember to install `PyGithub` which is the only non-builtin package used. Instructions above.
* Run the code in your favorite IDE or in the terminal with 
	```bash
	python git_commit_backdater.py
	```
	#### Note:
	* When choosing a folder, make sure the folder doesn't already have a git repo with any git history you want to keep. The **script will delete any existing git repos in the folder without asking for confirmation**
	* Might only work on Windows. I'm not entirely sure if the commands used with subprocess, os and shutil libraries will work on Linux or Mac.  
	*  Remember, the script will **only make as many commits as there are items inside the directory** you choose. Meaning if you choose something like a directory containing a directory which then contains all your files, only one commit will be made as the chosen parent directory has only one item, the child directory.
  
* Choose a folder :  Choose the folder with your project files. 
* Enter your GitHub API key :  Paste your GitHub Personal Access Token.
* Enter a name for your GitHub Repo : Enter a name you want give the repo. Or press enter to default to the folder name.
* If no errors happen, you can now go to your GitHub and see a beautiful contribution chart, one that's more reflective of your suffering in the past year. 
* You now have the power to time travel. Use it wisely.
