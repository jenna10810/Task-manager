# Task-manager

## Uses
This program will help a small business manage all the tasks that have been assigned to different users. 

## Files included
### tasks.txt
This file contains a list of all of the tasks that the team is working on. Each line contains the following data about the task:
* the username of the person to whom the task is assigned
* the title of the task
* a description of the task
* the date that the task was assigned to the user
* the due date of the task
* either a _"yes"_ or _"no"_ value that specifies if the task has been completed yet

### user.txt
This file contains the usernames and passwords for each team member that has permission to use the program.
The format is as follows:
* the username followed by a comma and a space and then the corresponding password
* one username and corresponding password per line

## Actual code
The user should be able to login, register a user, add a task, view all tasks and view their own tasks. This is all displayed in a user friendly manner. This was the initial assignement, but it was later needed that only the _"admin"_ user could register a new user. The _"admin"_ user also has a different menu option, this allows them to view statistics about all of the tasks, such as the total number of tasks in the _"tasks.txt"_ file, as well as the number of users in the _"user.txt"_ file.
