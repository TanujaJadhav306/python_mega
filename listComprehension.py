# text=["tanuja","santosh","jadhav"]
# for name in text:
#     print(name)

# for i in range (1,11):
#     print(i)


# while 3<9:
#     print("enter you name")
#     name=input()
#     print(name)



while True:
    user_action = input("Type 'add'  or 'show' or 'edit' or 'complete' ': ")
    user_action=user_action.strip()


    if 'add' in user_action:
            todo = (user_action[4:]) + "\n"

            try:
                with open('todos.txt', 'r') as file:
                    todos = file.readlines()
            except FileNotFoundError:
                todos = []

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

    elif 'show' in user_action:
            file=open('todos.txt','r')
            todos=file.readlines()
            file.close()
            for index,item in enumerate(todos):
                row=f"{index+1}-{item}"
                print(item)

    elif 'edit' in user_action:
            number=int(user_action[5:])
            print(number)
            number=number-1

            with open('todos.txt','r') as file:
                todos=file.readlines()
            new_todo=input("enter new todo")
            todos[number]=new_todo + "\n"

            with open('todos.txt','w')as file:
                file.writelines(todos)

    elif 'complete' in user_action:
            num=int(user_action[9:])

            with open('todos.txt','r')as file:
                todos=file.readlines()
            index=num-1
            todo_to_remove=todos[index].strip('\n')
            todos.pop(index)

            with open('todos.txt','w')as file:
                todos=file.writelines(todos)

            message=f"todo{todo_to_remove}was removed from the list"
            print(message)

    else :
               break
               print("Bye")



