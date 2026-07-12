from task_manager import *
from storage import *

def main():
    tasks = load_tasks()
    show_tasks(tasks)
    show_actions()
    user = user_input('u')
    while user != '4':
        if user == '1':
            add_task(tasks)
            clear_screen(tasks)
            user = user_input('u')
        if user == '2':
            mark_completed(tasks)
            clear_screen(tasks)
            user = user_input('u')
        if user == '3':
            tasks = remove_task(tasks)
            clear_screen(tasks)
            user = user_input('u')
    save_tasks(tasks)

if __name__ == '__main__':
    main()