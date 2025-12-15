"""
Демонстрация использования структур данных.
"""
from .structures import Stack, Queue
from .linked_list import SinglyLinkedList


def demo_stack() -> None:
    """Демонстрация работы стека."""
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ СТЕКА (LIFO)")
    print("=" * 60)
    
    stack = Stack()
    print(f"Создан пустой стек: {stack}")
    print(f"Стек пуст? {stack.is_empty()}")
    
    # Добавление элементов
    print("\nДобавляем элементы 1, 2, 3...")
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f"Стек после добавлений: {stack}")
    print(f"Размер стека: {len(stack)}")
    
    # Просмотр вершины
    print(f"\nВершина стека (peek): {stack.peek()}")
    print(f"Стек после peek: {stack}")
    
    # Удаление элементов
    print("\nУдаляем элементы (pop):")
    while not stack.is_empty():
        item = stack.pop()
        print(f"  Извлечён: {item}, осталось элементов: {len(stack)}")
    
    print(f"\nСтек пуст? {stack.is_empty()}")
    
    # Обработка ошибки
    try:
        stack.pop()
    except IndexError as e:
        print(f"\nОшибка при попытке pop из пустого стека: {e}")


def demo_queue() -> None:
    """Демонстрация работы очереди."""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ОЧЕРЕДИ (FIFO)")
    print("=" * 60)
    
    queue = Queue()
    print(f"Создана пустая очередь: {queue}")
    print(f"Очередь пуста? {queue.is_empty()}")
    
    # Добавление элементов
    print("\nДобавляем элементы 'A', 'B', 'C'...")
    queue.enqueue('A')
    queue.enqueue('B')
    queue.enqueue('C')
    print(f"Очередь после добавлений: {queue}")
    print(f"Размер очереди: {len(queue)}")
    
    # Просмотр первого элемента
    print(f"\nПервый элемент (peek): {queue.peek()}")
    print(f"Очередь после peek: {queue}")
    
    # Удаление элементов
    print("\nУдаляем элементы (dequeue):")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"  Извлечён: {item}, осталось элементов: {len(queue)}")
    
    print(f"\nОчередь пуста? {queue.is_empty()}")
    
    # Обработка ошибки
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"\nОшибка при попытке dequeue из пустой очереди: {e}")


def demo_linked_list() -> None:
    """Демонстрация работы односвязного списка."""
    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ОДНОСВЯЗНОГО СПИСКА")
    print("=" * 60)
    
    linked_list = SinglyLinkedList()
    print(f"Создан пустой список: {linked_list}")
    
    # Добавление в конец
    print("\nДобавляем 1, 2, 3 в конец (append):")
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(f"Список: {linked_list}")
    print(f"Размер: {len(linked_list)}")
    
    # Добавление в начало
    print("\nДобавляем 0 в начало (prepend):")
    linked_list.prepend(0)
    print(f"Список: {linked_list}")
    
    # Вставка по индексу
    print("\nВставляем 2.5 на позицию 3 (insert):")
    linked_list.insert(3, 2.5)
    print(f"Список: {linked_list}")
    
    # Итерация по списку
    print("\nИтерация по списку:")
    for item in linked_list:
        print(f"  Элемент: {item}")
    
    # Удаление по значению
    print("\nУдаляем значение 2 (remove):")
    if linked_list.remove(2):
        print(f"Список после удаления 2: {linked_list}")
    else:
        print("Значение 2 не найдено")
    
    # Удаление по индексу
    print("\nУдаляем элемент по индексу 1 (remove_at):")
    removed = linked_list.remove_at(1)
    print(f"Удалён элемент: {removed}")
    print(f"Список после удаления: {linked_list}")
    
    # Попытка вставки с неверным индексом
    print("\nПопытка вставки с индексом 10:")
    try:
        linked_list.insert(10, 99)
    except IndexError as e:
        print(f"Ошибка: {e}")


def demo_practical_examples() -> None:
    """Практические примеры использования структур данных."""
    print("\n" + "=" * 60)
    print("ПРАКТИЧЕСКИЕ ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ")
    print("=" * 60)
    
    # Пример 1: Проверка сбалансированности скобок (Stack)
    print("1. Проверка сбалансированности скобок (Stack):")
    
    def is_balanced(expression: str) -> bool:
        """Проверяет, правильно ли расставлены скобки в выражении."""
        stack = Stack()
        brackets = {'(': ')', '[': ']', '{': '}'}
        
        for char in expression:
            if char in brackets:  # Открывающая скобка
                stack.push(char)
            elif char in brackets.values():  # Закрывающая скобка
                if stack.is_empty():
                    return False
                opening = stack.pop()
                if brackets[opening] != char:
                    return False
        
        return stack.is_empty()
    
    test_cases = [
        "((()))",
        "({[]})",
        "({[)]}",
        "((())",
        "",
    ]
    
    for expr in test_cases:
        result = is_balanced(expr)
        print(f"  '{expr}': {'сбалансировано' if result else 'несбалансировано'}")
    
    # Пример 2: Моделирование очереди печати (Queue)
    print("\n2. Моделирование очереди печати (Queue):")
    
    print_queue = Queue()
    print("  Добавляем задания в очередь печати...")
    print_queue.enqueue("Документ1.pdf")
    print_queue.enqueue("Отчет.docx")
    print_queue.enqueue("Презентация.pptx")
    
    print("  Обработка очереди печати:")
    while not print_queue.is_empty():
        job = print_queue.dequeue()
        print(f"  Печатается: {job}")
    
    # Пример 3: История посещений (SinglyLinkedList)
    print("\n3. История посещений веб-страниц (SinglyLinkedList):")
    
    history = SinglyLinkedList()
    print("  Посещаем страницы...")
    history.append("google.com")
    history.append("youtube.com")
    history.append("github.com")
    history.append("stackoverflow.com")
    
    print(f"  История: {history}")
    
    print("  Возвращаемся назад (удаляем последние):")
    history.remove_at(len(history) - 1)
    history.remove_at(len(history) - 1)
    print(f"  Текущая история: {history}")


if __name__ == "__main__":
    demo_stack()
    demo_queue()
    demo_linked_list()
    demo_practical_examples()