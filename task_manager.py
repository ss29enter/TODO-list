from textwrap import wrap
from os import system

### интерфейс

# меню
def show_actions():
    print_separator('menu')
    print('1. Add a task')
    print('2. Mark сompleted')
    print('3. Remove a task (tasks)')
    print('4. Save & Exit')
    print('X. Exit the action\n')
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

# ввод пользователя + ввод уровня приоритета
def user_input(opt):
    if opt == 'u':
        user = input('>> ').lower()
    if opt == 'p':
        user = input('Priority level [1-4]: ')
    if user not in ['1','2','3','4']:
        print('Invalid action number.')
        return user_input(opt)
    return user

# выход из действия
def exit_from_action(user):
    return user.lower() in ['x','exit']

### действия

# добавить задачу + присвоить ей номер + приоритет
def add_task(tasks):
    task = input('Task: ')
    priority = user_input('p')
    priority_range = ['Critical','High','Medium','Low'][int(priority)-1]
    if exit_from_action(task):
        return
    if task=='':
        return print('You entered an empty string.'), add_task(tasks)                             
    if tasks:
        new_id = str( max(map(int,tasks.keys()) ) + 1)
    else: new_id = '1'
    tasks[new_id] = {
        'task': task,
        'done': False,
        'priority': priority_range
    }

# показать текущие задачи + рассортировать по приоритету
def show_tasks(tasks):
    print_separator('title')
    priority_order = [
        'Critical',
        'High',
        'Medium',
        'Low'
    ]
    if tasks == {}:
        return print("\t\tYou don't have any\n\t\tcurrent tasks yet\n")

    for priority in priority_order:
        print('! ' + priority.upper())
        for number in tasks.keys():
            id = tasks[number]
            if id['priority'] == priority:
                task = f'{number}) ☒  {id['task']}' if id['done'] else f'{number}) ☐  {id['task']}' 
                for line in wrap(task,width=48):
                    print(' '*2 + line.ljust(48,'.'))
            else: continue
        print()
    count_completed(tasks)

# отметить задачу завершенной
def mark_completed(tasks):
    number = input('Enter the number: ')
    if exit_from_action(number):
        return
    try: 
        tasks[number]['done'] = True
    except KeyError:
        print('Invalid issue number.')
        mark_completed(tasks)

# подсчитать кол-во завершенных/оставшихся задач
def count_completed(tasks):
    done = 0
    for id in tasks:
        done += tasks[id]['done']
    not_done = len(tasks) - done
    if tasks == {}:
         pass
    elif done == len(tasks):
        print('All tasks are completed!')
    else:
        print(f'Done: {done}')
        print(f'Remained: {not_done}') 

# удалить задачу из списка + перенумеровать задачи  
def remove_task(tasks):
    number = input('Enter the number or "ALL" to clear list: ')
    if number == 'ALL':
        return {}
    if exit_from_action(number):
        return
    try:
        del tasks[number]
    except KeyError:
        print('Invalid issue number.')
        remove_task(tasks)
    new_tasks = {}
    for id,task in enumerate(tasks.values(),start=1):
        new_tasks[str(id)] = task
    return new_tasks
