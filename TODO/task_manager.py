from textwrap import wrap
from os import system

### интерфейс

# меню
def show_actions():
    print_separator('menu')
    print('1. Add a task')
    print('2. Mark сompleted')
    print('3. Remove a task')
    print('4. Save & Exit')
    print('X. Undo action\n')
    print_separator('act')

# вывести разделители 
def print_separator(cmd):
    if cmd == 'title':
        print(f'{'='*19} TODO  LIST {'='*19}\n')
    if cmd == 'menu':
        print(f'{'='*22} MENU {'='*22}\n')
    if cmd == 'sep':
        print(f'{'='*50}\n')
    if cmd == 'act':
        print('='*50)
        print('\t\tSelect an action\n')

# очищает экран перед выводом
def clear_screen(tasks): 
    system('cls')
    show_tasks(tasks)
    show_actions()

# ввод пользователя
def user_input():
    user = input('≫ ').lower()
    if user not in ['1','2','3','4']:
        print('Неверный номер действия.')
        return user_input()
    return user

# выход из действия
def exit_from_action(user):
    return user.lower() in ['x','exit']

### действия

# добавить задачу + присвоить ей номер
def add_task(tasks):
    task = input('Task: ')
    if exit_from_action(task):
        return
    if task=='':
        return print('Вы ввели пустую строку.'), add_task(tasks)                             
    if tasks:
        new_id = str( max(map(int,tasks.keys()) ) + 1)
    else: new_id = '1'
    tasks[new_id] = {
        'task': task,
        'done': False
    }

# показать текущие задачи   
def show_tasks(tasks):
    print_separator('title')
    if tasks == {}:
        print("\t\tYou don't have any\n\t\tcurrent tasks yet")
    for number in tasks.keys():
        id = tasks[number] 
        task = f'{number}. ☒  {id['task']}' if id['done'] else f'{number}. ☐  {id['task']}' 
        for line in wrap(task,width=50):
            print(line)
    print()
    count_done(tasks)

# отметить задачу завершенной
def mark_completed(tasks):
    number = input('Enter the number: ')
    if exit_from_action(number):
        return
    try: 
        tasks[number]['done'] = True
    except KeyError:
        print('Неверный номер задачи.')
        mark_completed(tasks)

# подсчитать кол-во завершенных/оставшихся задач
def count_done(tasks):
    done = 0
    for id in tasks:
        done += tasks[id]['done']
    undone = len(tasks) - done
    if tasks == {}:
         pass
    elif done == len(tasks):
        print('Цель достигнута!')
    else:
        print(f'Завершенных: {done}')
        print(f'Осталось: {undone}') 

# удалить задачу из списка + перенумеровать задачи  
def remove_task(tasks):
    number = input('Enter the number: ')
    if exit_from_action(number):
        return
    try:
        del tasks[number]
    except KeyError:
        print('Неверный номер задачи.')
        remove_task(tasks)
    new_tasks = {}
    for id,task in enumerate(tasks.values(),start=1):
        new_tasks[str(id)] = task
    return new_tasks
    




