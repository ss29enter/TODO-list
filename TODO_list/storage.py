import json

def load_tasks():
    '''
    Read the data from the file, otherwise create a new one
    '''
    try:
        with open('todo-list','r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_tasks(tasks):
    '''
    Save data to a file
    '''
    with open('todo-list','w',encoding='utf-8') as file:
        json.dump(tasks,file,indent=4,ensure_ascii=False)