def display_task():
    with open("tasks.txt","r") as f:
        l = f.read()
        print(l)

def add_task(task):
    with open("tasks.txt","a") as f:
        f.write('\n'+task)
    display_task()

def remove_task(task):
    new_list = []
    with open("tasks.txt","r") as f:
        tasks = f.readlines()
    for i in tasks:
        if i.strip()!=task:
            new_list.append(i)
    with open("tasks.txt","w+") as f:
        f.writelines(new_list)
    print("Task has been removed")
    print("the current tasks are:")
    display_task()
