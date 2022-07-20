#=====importing libraries===========
from datetime import date
from collections import Counter
#=========Functions=========== My friend, Steven, helped me with these functions, just as a way to simplify my code
def read_all_tasks():
    task_list = []

    # Open the file 'tasks.tx' and read all of the lines
    with open("tasks.txt" , "r") as task_file:
        for line in task_file.readlines():
            columns = line.strip().split(", ")  # Strip the lists of the newline character and split it at the comma
            task_list.append({
                "name": columns[1],
                "description": columns[2],
                "date_assigned": columns[3],
                "assigned_to": columns[0],
                "due_date": columns[4],
                "completed": columns[5]
            })     
    return task_list

# Prints a task in a user friendly manner
def print_task (task):
    print("%-20s %s" % ("Task", task["name"]))
    print("%-20s %s" % ("Assigned to", task["assigned_to"]))
    print("%-20s %s" % ("Date assigned", task["date_assigned"]))
    print("%-20s %s" % ("Due date", task["due_date"]))
    print("%-20s %s" % ("Task complete?", task["completed"]))
    print("%-20s %s" % ("Task description:", "\n" + task["description"] + "\n"))


#====Login Section====
# Create new lists to store the 'user.txt' passwords and usernames
usernames_login = []
passwords_login = []


# Open the file 'user.txt' and create a list of the authorised passwords and usernames
with open ("user.txt" , "r") as f:
    for lines in f.readlines():
        columns = lines.strip().split(", ")
        usernames_login.append(columns[0])
        passwords_login.append(columns[-1])
        

# Validate the user's login details against the details found in the file user.txt
login = False

while login == False:
    username = input("Enter your username: \t")
    password = input("Enter your password: \t")   

    # If the username is not in the list, but the password is, then the user must try again
    if (username not in usernames_login) and (password in passwords_login):
        print("Wrong username, please try again:")
        continue    # This allows the user to try agian by going to the top again and asking them for their login details
    # If the username is in the list, but the password is not, then the user must try again
    elif (username in usernames_login) and (password not in passwords_login):
        print("Wrong password, please try again:")
        continue
    elif (username not in usernames_login) and (password not in passwords_login):
        print("Wrong username and password, please try again:")
        continue
    else: 
        break # The user's credentials are valid


while True:
    if username == "admin":
        admin_menu = input("Would you like to see the statistics for all of the tasks? (Y or N): \t").upper()
        
        if admin_menu == "Y":
            # Open the file, 'tasks.txt' 
            with open("tasks.txt" , "r") as task_file:
                count = Counter(line.split(", ")[0] for line in task_file)  # Count the amount of times a task is assigned to a user - 
                                                                            # I got this Counter from doing task 20
            print("Tasks assigned:")
            for key, value, in count.items():
                print(key + ":\t" + str(value))
                    
                    
            list_of_names_and_tasks = []    # Create an empty list 
            dict_of_names_and_tasks = {}    # Create an empty dictionary
            with open("tasks.txt" , "r") as task_file:
                for lines in task_file:
                    columns = lines.split(",")      # Split the line by the commas in order to use the data
                    list_of_names_and_tasks.append(columns[0])      # Only add the user's name to the list
                    dict_of_names_and_tasks = (Counter(list_of_names_and_tasks))    # Count the amount of tasks assigned to a user

            for key, value in dict_of_names_and_tasks.items():
                print(f"\nUser: \t{key} \nTasks: \t{value}")    # Print out the username and amount of tasks

    menu = input('''Select one of the following Options below:
        r  - \tRegistering a user
        a - \tAdding a task
        va - \tView all tasks
        vm - \tview my task
        e - \tExit
        \t\t: ''').lower() 

    if menu == 'r':
        
        if username == "admin":
            print("You have chosen to register a new user:")
            # Here the admin can add the new user's details
            new_username = input("Enter your username: \t\t")
            new_password = input("Enter your password: \t\t")
            password_validation = input("Please confirm your password:\t")
        
        # Validate the user's new password against the one they enetered first, if it does not match, they have to try again
            while new_password != password_validation:
                new_password = input("Please enter the same password: ")
                password_validation = input("Please confirm your password:\t")

            # Add the new user's data to the file 'user.txt'
            with open("user.txt" , "a") as username_file:
                username_file.write("\n" + new_username + ", " + new_password)
        else: 
            print("You are not allowed to add new users \n")
        pass

    elif menu == 'a':
        
        # Promp the user to enter new task details to the 'task.txt' file
        username_assigned_to = input("To who is this task assigned to? \t")
        title_of_task = input("What is the title of the task? \t\t")
        description_of_task = input("Describe the task: \t\t\t")
        due_date_of_task = input("When is this task due? (DD Month Year)\t")
        today_date = date.today()
        task_completed = "No"

        # Add the user's input to the 'task.txt' file
        with open("tasks.txt" , "a") as task_file:
            task_file.write(f"\n{username_assigned_to}, {title_of_task}, {description_of_task}, {due_date_of_task}, {today_date}, {task_completed}" )
        pass

    elif menu == 'va':
        # Declare new lists where the corresponding information will be listed
        task_list = read_all_tasks()
    
        # Use a for loop to run through all of the lines and print out the tasks in an easy to raed format
        for task in task_list:
            print_task(task)
        pass
    
    elif menu == 'vm':
        list_tasks = read_all_tasks()   # Call the function 'read_all_tasks'
        users_tasks = []                # Create an empty list to store the tasks in
        for task in list_tasks:
            if task["assigned_to"] == username:   
                users_tasks.append(task)    # Append the user's tasks to the 'user_tasks' list
                print_task(task)            # Print out the user's tasks
        pass

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, please try again")

# My previous code reviewer said that there was an error on line 17, however,
# my code works fine in VS Code, I can't understand why it doesn't work here
# any help would be appreciated, as I can't reproduce the error on my side

