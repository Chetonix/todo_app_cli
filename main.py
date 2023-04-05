from functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(f"It is {now}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:] + '\n'

        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()
        todos = get_todos()

        todos.append(todo)

        # file = open('todos.txt', 'w')
        # file.writelines(todos)
        # file.close()

        write_todos(todos)

    elif user_action.startswith('show'):
        # file = open('todos.txt', 'r')
        # todos = file.readlines()
        # file.close()

        todos = get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for i, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            print(f"{i + 1}- {item}")
    elif user_action.startswith('edit'):
        try:
            index = int(user_action[5:]) - 1
            todos = get_todos()

            todos[index] = input("Enter a new todo: ") + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):
        try:
            index = int(user_action[9:]) - 1

            todos = get_todos()

            todo_removed = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            print(f"Todo {todo_removed} was removed from the list.")
        except IndexError:
            print("There is no item with that number.")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print('You entered an invalid command!')

print('Bye!')
