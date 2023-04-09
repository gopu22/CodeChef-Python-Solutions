#!/bin/bash

# Set the directory to watch for new files
WATCH_DIR="/home/govardhan/Documents/CodeChef/Solutions!/Solutions!"

# Set the Git repository and branch to push to
GIT_REPO="https://github.com/gopu22/CodeChef-Python-Solutions.git"
GIT_BRANCH="main"

# Set the commit message to use
COMMIT_MESSAGE="Automated commit"

# Change to the watch directory
cd $WATCH_DIR

# Continuously monitor for new files
while true; do
    # Wait for a new file to appear
    inotifywait -e create --format '%f' $WATCH_DIR |
    while read FILENAME; do
        # Add the new file to the Git repository
        git add $FILENAME

        # Commit the changes with the specified message
        git commit -m "$COMMIT_MESSAGE"

        # Push the changes to the remote Git repository
        git push $GIT_REPO $GIT_BRANCH
    done
done

