# Git_Commit_Backdater

Git Commit Backdater is a Python script that helps students and developers upload old projects or coursework to GitHub with accurate commit history. The script initializes a Git repository, commits files based on their last modified dates, and creates a corresponding GitHub repository, ensuring that your GitHub contribution chart reflects your historical work.
Features

    Folder Selection: A user-friendly file chooser to select the project folder.
    GitHub Repository Creation: Automatically creates a new GitHub repository with a specified name (default: folder name).
    Commit History Backdating: Commits files with their last modified dates.
    Git Repository Reset: Prompts to reset existing repositories if a .git folder is found.
    GitHub API Key Input: User inputs their API key securely for GitHub integration.

Prerequisites

    Python 3.6+
    Git installed on your system.
    PyGithub library installed:

    pip install PyGithub  

    A GitHub account with a Personal Access Token.

Installation

    Clone this repository:

git clone <repository_url>  

Install required Python packages:

    pip install -r requirements.txt  

Usage

    Run the script:

    python github_commit_backdate.py  

    Choose a Folder: Use the file chooser to select the folder to backdate.
    GitHub API Key: Enter your GitHub API key (Personal Access Token).
    Repository Name: Enter a name for the GitHub repository (or press Enter to default to the folder name).
    The script will:
        Initialize or reset the Git repository in the folder.
        Commit each file with its last modified date as the commit date.
        Create a GitHub repository and push the commits.

Notes

    Reset Confirmation: The script automatically deletes existing .git folders without confirmation—use cautiously.
    Error Handling: Errors (e.g., API or subprocess failures) are displayed in the terminal.
    Dependencies: Ensure shutil and os are compatible with your Python version.

Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or bug fixes.
License

This project is licensed under the MIT License.
Acknowledgements

Designed to help students and developers showcase their historical work on GitHub with ease and accuracy.
