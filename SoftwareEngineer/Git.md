# Git and Github guide
## Quick intro

#### What is Git?
Git is a version control system that tracks changes in your code or files over time, making it easy to collaborate and manage versions.

#### What is GitHub?
GitHub is an online platform for hosting Git repositories, allowing teams to collaborate and manage code in one central location.

#### Key Terms
- **Repository (Repo)**: A project folder managed by Git.
- **Working Directory**: The folder on your computer where your project 
  files are located. Files here can be **tracked** (managed by Git) or 
  **untracked** (not yet under Git's control).
- **Staging Area**: A place where changes are prepared (or "staged") before 
  committing.
- **Local Repository**: A database on your computer where Git stores committed changes. 
- **Remote Repository** A shared repository hosted online (e.g., on GitHub).
Allows team members to collaborate and share changes.
- **Branch**: A separate line of development for working on features 
  independently.
- **Commit**: A snapshot of changes in your project history.
- **Push**: Upload local commits to the remote repository.
- **Pull**: Download changes from the remote repository.

#### Set up Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```
#### Clone our Repository
```bash
git clone https://github.com/TianhaoW/AllofQuant
```

## General Workflow
#### Always update your local repo before making changes
```bash
git pull origin main    # Get the most recent version of the main branch
```
#### Make your changes and stage the changes
```bash
git add <file-name>       # This will only stage the file-name to staging area
git add .                 # This will stage all changes 
```
#### Commit your changes with a message
```bash
git commit -m "Describe your changes"
```
#### Push your changes to Github
```bash
git push origin main
git push origin <your branch name>    # If you are working a different use this command
```

