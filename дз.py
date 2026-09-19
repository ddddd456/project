tasks = []

def show_menu():
    """Задача 1: Создать пользовательское меню"""
    print("\n=== Менеджер задач ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выйти из программы")
    print("======================")

def show_tasks():
    if not tasks:
        print("\n[Инфо] Список задач пуст.")
        return
    
    print("\n--- Ваш список задач ---")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print("------------------------")

def add_task():
    new_task = input("Введите текст новой задачи: ").strip()
    if new_task:
        tasks.append(new_task)
        print(f"[Успех] Задача '{new_task}' добавлена!")
    else:
        print("[Ошибка] Текст задачи не может быть пустым.")

def edit_task():
    show_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Введите номер задачи для редактирования: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Введите новое название задачи: ").strip()
            if new_name:
                tasks[task_num - 1] = new_name
                print("[Успех] Название задачи обновлено!")
            else:
                print("[Ошибка] Название не может быть пустым.")
        else:
            print("[Ошибка] Задачи с таким номером не существует.")
    except ValueError:
        print("[Ошибка] Пожалуйста, введите корректный номер (цифру).")

def delete_task():
    show_tasks()
    if not tasks:
        return
    
    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"[Успех] Задача '{removed_task}' удалена!")
        else:
            print("[Ошибка] Задачи с таким номером не существует.")
    except ValueError:
        print("[Ошибка] Пожалуйста, введите корректный номер (цифру).")

def main():
    """Задача 2: Реализовать цикл приложения и выход"""
    print("Добро пожаловать в Менеджер задач (Версия 0.0.3)")
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nСпасибо за использование! До свидания.")
            break # Выход из цикла и завершение программы
        else:
            print("\n[Ошибка] Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()