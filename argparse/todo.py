import argparse
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    """Загружает задачи из файла"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Сохраняет задачи в файл"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f)

def add_task(args):
    """Добавляет новую задачу"""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        'id': task_id,
        'text': args.text,
        'status': 'pending'
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Задача добавлена (ID: {task_id})")

def list_tasks(args):
    """Выводит список задач"""
    tasks = load_tasks()
    
    if not tasks:
        print("Нет задач")
        return
    
    if args.status:
        tasks = [task for task in tasks if task['status'] == args.status]
    
    for task in tasks:
        status_icon = '✓' if task['status'] == 'completed' else '○'
        print(f"{task['id']}. [{status_icon}] {task['text']}")

def complete_task(args):
    """Отмечает задачу как выполненную"""
    tasks = load_tasks()
    
    for task in tasks:
        if task['id'] == args.id:
            task['status'] = 'completed'
            save_tasks(tasks)
            print(f"Задача {args.id} выполнена")
            return
    
    print(f"Задача с ID {args.id} не найдена")

def delete_task(args):
    """Удаляет задачу"""
    tasks = load_tasks()
    
    for i, task in enumerate(tasks):
        if task['id'] == args.id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Задача {args.id} удалена")
            return
    
    print(f"Задача с ID {args.id} не найдена")

def main():
    parser = argparse.ArgumentParser(description='Менеджер задач')
    subparsers = parser.add_subparsers(dest='command', help='Доступные команды')
    
    parser_add = subparsers.add_parser('add', help='Добавить задачу')
    parser_add.add_argument('text', help='Текст задачи')
    
    parser_list = subparsers.add_parser('list', help='Показать задачи')
    parser_list.add_argument('--status', choices=['pending', 'completed'], 
                           help='Фильтр по статусу')
    
    parser_complete = subparsers.add_parser('complete', help='Завершить задачу')
    parser_complete.add_argument('id', type=int, help='ID задачи')
    
    parser_delete = subparsers.add_parser('delete', help='Удалить задачу')
    parser_delete.add_argument('id', type=int, help='ID задачи')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args)
    elif args.command == 'list':
        list_tasks(args)
    elif args.command == 'complete':
        complete_task(args)
    elif args.command == 'delete':
        delete_task(args)

if __name__ == '__main__':
    main()


# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/todo.py add "Добавить интеграцию TG API"
# Задача добавлена (ID: 1)
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/todo.py list --status pending 
# 1. [○] Добавить интеграцию TG API
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/todo.py complete 1
# Задача 1 выполнена
# alisa@MacBook-Air-Alisa uni_repo % python3 argparse/todo.py delete 1  
# Задача 1 удалена
