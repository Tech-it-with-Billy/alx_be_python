task = input("Enter your task: ")
priority = input("Priority (high, medium, low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority.lower():
    case 'high':
        if time_bound.lower() == 'yes':
            print(f"Reminder: {task} is a high priority task that needs to be completed today!")
        else:
            print(f"Reminder: {task} is a high priority task, please complete it as soon as possible!")
    case 'medium':
        if time_bound.lower() == 'yes':
            print(f"Reminder: {task} is a medium priority task that should be completed soon!")
        else:
            print(f"Reminder: {task} is a medium priority task, try to complete it in the next few days.")
    case 'low':
        if time_bound.lower() == 'yes':
            print(f"Reminder: {task} is a low priority task, but it should be completed when you have time.")
        else:
            print(f"Reminder: {task} is a low priority task, you can complete it whenever you find time.")