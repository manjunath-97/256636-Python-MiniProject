# Python program to
# demonstrate todolist project using queue
''' 
    Some tasks you can use whiile running program:
    read a book
    revise CNS 1st unit 
    Deposit money in the bank
    setup linux instalation
    build a mini project
'''
    
tasks = [] #Holds all the tasks we add.(our Todo ist)

#displays all the tasks in the list
def allTasks():
    print("All upcoming tasks",end='\n')
    if len(tasks) == 0:
        print("No tasks in the list currenty...(Use add task option)")
        return
    for task in tasks:
        print(tasks.index(task)+1,task,sep=".")

#adds a task to the todo list
def addTask(task):
    tasks.append(task)
    print('Task added successfully')

#Displays upcoming 5 tasks
def show5():
    if len(tasks)==0:
        print("No tasks in the list")
    elif len(tasks)<5:
        print("Your tasks:")
        for task in tasks:
            print(tasks.index(task)+1,task,sep=".")
        print('\nthat\'s it. You have only',len(tasks),'tasks',sep=' ',end='\n')
    else:
        print("5 upcoming tasks",end='\n')
        for task in tasks:
            print(tasks.index(task)+1,task,sep=".")

#Displays Upcoming task
def show1():
    if len(tasks)==0:
        print('No upcoming tasks..(Use add options to add some)')
        return
    print("upcoming task: ",tasks[0],end='\n')

#clears the current task if its completed 
def update():
    if len(tasks) == 0:
        print('You have no tasks in the list')
        return
    print('Have you completed this task',tasks[0],sep='--> "',end='" (Enter yes/no): ')
    if(input().lower()=='yes'):
        tasks.pop(0)
        print('\ntask is cleared from the list.')
        show1()
    else:
        print('\nComplete task to remove it from the list')

#clears the tasks in the todo list
def reset():
    tasks.clear()
    print('List is reset.')


#Our menu for the application
print('\"\n\nTodolist application\"s')
print('--------------------------------')
while True:
    print("1.Add a task")
    print("2.Update list")
    print("3.Show upcoming task")
    print("4.Show upcomin 5 tasks")
    print('5.Show all the tasks in the list')
    print('6.Reset the list')
    print('7.Exit')
    print('--------------------------------')
    print('input your choice',end=' : ')
    choice = int(input())
    
    
    if choice == 1:
        task = input('Enter the task: ')
        addTask(task)
        print('--------------------------------')
    elif choice == 2:
        update()
        print('--------------------------------')
    elif choice == 3:
        show1()
        print('--------------------------------')
    elif choice==4:
        show5()
        print('--------------------------------')
    elif choice == 5:
        allTasks()
        print('--------------------------------')
    elif choice == 6:
        reset()
        print('--------------------------------')
    else:
        print('You sure you want to leave ?(Yes or no) : ',end='')
        if(input().lower()=='no'):
            continue
        print('                  Bye then, Have a good time!')
        break

#END

