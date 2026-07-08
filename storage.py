import json

# загрузить задачи из существующего файла или создать новый
def load_tasks():
    try:
        with open('todo-list','r',encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# сохранить задачи в файл
def save_tasks(tasks):
    with open('todo-list','w',encoding='utf-8') as file:
        json.dump(tasks,file,indent=4,ensure_ascii=False)