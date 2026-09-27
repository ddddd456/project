tasks = []


def show_message(message: str, kind: str = "info") -> None:
    """
    Выводит сообщение пользователю.

    kind:
        "info"    — информационное сообщение
        "success" — успешное действие
        "error"   — ошибка
    """
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
    """Задача 1: Создать пользовательское меню."""
    print("\n=== Менеджер задач ===")
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Редактировать задачу")
    print("4. Удалить задачу")
    print("5. Выйти из программы")
    print("======================")


def show_tasks() -> None:
    """Показывает все задачи через show_collection."""
    show_collection(tasks)


def add_task() -> None:
    new_task = input("Введите текст новой задачи: ").strip()
    if new_task:
        tasks.append(new_task)
        show_message(f"Задача '{new_task}' добавлена!", "success")
    else:
        show_message("Текст задачи не может быть пустым.", "error")


def edit_task() -> None:
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для редактирования: "))
        if 1 <= task_num <= len(tasks):
            new_name = input("Введите новое название задачи: ").strip()
            if new_name:
                tasks[task_num - 1] = new_name
                show_message("Название задачи обновлено!", "success")
            else:
                show_message("Название не может быть пустым.", "error")
        else:
            show_message("Задачи с таким номером не существует.", "error")
    except ValueError:
        show_message("Пожалуйста, введите корректный номер (цифру).", "error")


def delete_task() -> None:
    show_tasks()
    if not tasks:
        return

    try:
        task_num = int(input("Введите номер задачи для удаления: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            show_message(f"Задача '{removed_task}' удалена!", "success")
        else:
            show_message("Задачи с таким номером не существует.", "error")
    except ValueError:
        show_message("Пожалуйста, введите корректный номер (цифру).", "error")


def main() -> None:
    """Задача 2: Реализовать цикл приложения и выход."""
    print("Добро пожаловать в Менеджер задач (Версия 0.0.5)")

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
            break
        else:
            show_message("Неверный выбор. Пожалуйста, попробуйте снова.", "error")


if __name__ == "__main__":
    main()
