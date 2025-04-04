# user_prompt="enter text"
# todo1=input(user_prompt)
# todo2=input(user_prompt)
# todo3=input(user_prompt)
#
# todo=[todo1,todo2,todo3]
# print(todo)

todos = []

while True:
    user_action = input("Type 'add'  or 'show' or 'edit' or 'remove': ")

    match user_action:
        case 'add':
            todo = input("Enter todo: ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                print(f"{index}-{item}")
        case 'edit':
            number=int(input("enter the index"))
            number=number-1
            new_todo=input("enter new todo")
            todos[number]=new_todo
        case 'remove':
            num=int(input("enter the number to remove item"))
            num=num-1
            todos.pop(num)
        case 'length':
            length=len(todos)
            print("length of todos is :",length)