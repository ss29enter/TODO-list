from task_manager import *
from storage import *

# работа основной программы
def main():
    tasks = load_tasks()
    show_tasks(tasks)
    show_actions()
    user = input('≫ ').lower()
    while user != '4':
        if user == '1':
            add_task(tasks)
            clear_screen(tasks)
            user = input('≫ ').lower()
        if user == '2':
            mark_completed(tasks)
            clear_screen(tasks)
            user = input('≫ ').lower()
        if user == '3':
            tasks = remove_task(tasks)
            clear_screen(tasks)
            user = input('≫ ').lower()
    save_tasks(tasks)

# запуск программы
if __name__ == '__main__':
    main()