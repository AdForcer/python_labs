"""
Интерактивное тестирование структур данных.
"""
if __name__ == "__main__":
    print("Тестирование импорта...")
    
    try:
        from src.lab10.structures import Stack, Queue
        from src.lab10.linked_list import SinglyLinkedList
        
        print("✓ Импорт успешен!")
        print("\nПример использования:")
        
        # Тест стека
        print("\n1. Тестирование Stack:")
        s = Stack()
        s.push(1)
        s.push(2)
        print(f"   Стек: {s}")
        print(f"   Peek: {s.peek()}")
        print(f"   Pop: {s.pop()}")
        print(f"   Размер: {len(s)}")
        
        # Тест очереди
        print("\n2. Тестирование Queue:")
        q = Queue()
        q.enqueue('A')
        q.enqueue('B')
        print(f"   Очередь: {q}")
        print(f"   Peek: {q.peek()}")
        print(f"   Dequeue: {q.dequeue()}")
        print(f"   Размер: {len(q)}")
        
        # Тест связного списка
        print("\n3. Тестирование SinglyLinkedList:")
        ll = SinglyLinkedList()
        ll.append(1)
        ll.append(2)
        ll.prepend(0)
        print(f"   Список: {ll}")
        print(f"   Размер: {len(ll)}")
        
        print("\n✓ Все тесты пройдены!")
        
    except ImportError as e:
        print(f"✗ Ошибка импорта: {e}")
        print("\nУбедитесь, что файлы расположены в правильной структуре:")
        print("python_labs/")
        print("├── src/")
        print("│   └── lab10/")
        print("│       ├── __init__.py")
        print("│       ├── structures.py")
        print("│       ├── linked_list.py")
        print("│       ├── benchmarks.py")
        print("│       └── demo.py")