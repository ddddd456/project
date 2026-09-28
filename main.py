import os
TASKS_FILE = "tasks.txt"
tasks = []


def show_message(message: str, kind: str = "info") -> None:
    prefixes = {
        "info": "[Инфо]",
        "success": "[Успех]",
        "error": "[Ошибка]",
    }
    prefix = prefixes.get(kind, "[Инфо]")
    print(f"{prefix} {message}")

def show_collection(collection: list) -> None:
    """Форматированно выводит коллекцию задач в консоль."""
    if not collection:
        show_message("Список задач пуст.", "info")
        return
    print("\n--- Ваш список задач ---")
    for index, task in enumerate(collection, start=1):
        print(f"{index}. {task}")
    print("------------------------")


def show_menu() -> None:
    print("\n=== Менеджер задач ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выйти из программы")
    print("======================")

def show_tasks() -> None:
    show_collection(tasks)

def load_tasks() -> None:
    """Загружает задачи из файла при запуске программы."""
    if not os.path.exists(TASKS_FILE):
        return
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as file:
            for line in file:
                task = line.strip()
                if task:
                    tasks.append(task)
        show_message(f"Загружено задач из файла: {len(tasks)}", "info")
    except Exception as e:
        show_message(f"Ошибка при загрузке задач: {e}", "error")

def save_tasks() -> None:
    """Сохраняет текущий список задач в файл."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            for task in tasks:
                file.write(task + '\n')
    except Exception as e:
        show_message(f"Ошибка при сохранении задач: {e}", "error")

def add_task() -> None:
    new_task = input("Введите текст новой задачи: ").strip()
    if new_task:
        tasks.append(new_task)
        save_tasks()
        show_message(f"Задача '{new_task}' добавлена!", "success")
    else:
        show_message("Текст задачи не может быть пустым.", "error")

def edited_task() -> None:
    """Изменяет задачу (согласно заданию: функция edited_task)."""
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для редактирования: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Введите новое название задачи: ").strip()
            if new_name:
                tasks[task_num - 1] = new_name
                save_tasks() 
                show_message("Название задачи обновлено!", "success")
            else:
                show_message("Название не может быть пустым.", "error")
        else:
            show_message("Задачи с таким номером не существует.", "error")
    except ValueError:
        show_message("Пожалуйста, введите корректный номер (цифру).", "error")


def deleted_task() -> None:
    """Удаляет задачу (согласно заданию: функция deleted_task)."""
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            save_tasks()  # Сохраняем изменения в файл
            show_message(f"Задача '{removed_task}' удалена!", "success")
        else:
            show_message("Задачи с таким номером не существует.", "error")
    except ValueError:
        show_message("Пожалуйста, введите корректный номер (цифру).", "error")


def main() -> None:
    print("Добро пожаловать в Менеджер задач (Версия 0.0.7)")
    
    # Загружаем задачи из файла при старте
    load_tasks()

    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ").strip()

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edited_task()  # Вызов переименованной функции
        elif choice == '4':
            deleted_task() # Вызов переименованной функции
        elif choice == '5':
            print("\nСпасибо за использование! До свидания.")
            break
        else:
            show_message("Неверный выбор. Пожалуйста, попробуйте снова.", "error")


if __name__ == "__main__":
    main()
