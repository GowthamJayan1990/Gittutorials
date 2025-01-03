
This is a note of all git commands used so far in terminal

git --version : Returns version of git installed

Create new repository in command line (Go to repository location)

git init : initialise the repository

git config --global user.name "User Name"
git config --global user.email useremail

git status : status of tracking
git add filename : adds file to tracking
git add . : Adds all files in location to staging

git commit -m "First commit" : Changes to be committed or added are moved to staging environment (use git status to see what is ready to be committed)

git branch -M main : Rename master branch to main
git remote add origin "https://github.com/GowthamJayan1990/reposityname.git" : to connect Local repository to remote repository 
git remote -v : origin variable is staging enviornment
git push origin main : Pushing the commit to repository

git restore filename : Restore any new changes in the staging enviorment

git clone "https://github.com/GowthamJayan1990/reposityname.git" : clones the remote repository to the current location

dir : list all files in the location