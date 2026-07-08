from textwrap import wrap
from os import system

# вывести разделители 
def print_separator(cmd):
    if cmd == 'title':
        print(f'{'='*19} TODO  LIST {'='*19}\n')
    if cmd == 'menu':
        print(f'{'='*22} MENU {'='*22}\n')
    if cmd == 'sep':
        print(f'{'='*25}{'='*25}\n')
    if cmd == 'act':
        print('='*50)
        print('\t\tSelect an action\n')

# добавить задачу + присвоить ей номер
def add_task(tasks):
    task = input('Task: ')
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
        for line in wrap(task,width=45):
            print(line)
    print()
    count_done(tasks)

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

# показать действия
def show_actions():
    print_separator('menu')
    print('1. Add a task')
    print('2. Mark сompleted')
    print('3. Remove a task')
    print('4. Save & Exit\n')
    print_separator('act')

# отметить задачу завершенной
def mark_completed(tasks):
    number = input('Enter the number: ')
    tasks[number]['done'] = True

# удалить задачу из списка + перенумеровать задачи  
def remove_task(tasks):
    number = input('Enter the number: ')
    del tasks[number]
    new_tasks = {}
    for id,task in enumerate(tasks.values(),start=1):
        new_tasks[str(id)] = task
    return new_tasks
    
# очищает экран перед выводом
def clear_screen(tasks):
    system('cls')
    show_tasks(tasks)
    show_actions()

