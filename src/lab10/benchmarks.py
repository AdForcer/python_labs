"""
Бенчмарки для сравнения производительности структур данных.
"""
import time
from .structures import Stack, Queue
from .linked_list import SinglyLinkedList


def benchmark_stack_operations(n: int = 10000) -> dict:
    """
    Бенчмарк операций со стеком.
    
    Args:
        n: Количество операций
        
    Returns:
        Словарь с временами выполнения операций
    """
    results = {}
    
    # Push операция
    stack = Stack()
    start = time.perf_counter()
    for i in range(n):
        stack.push(i)
    end = time.perf_counter()
    results['push'] = end - start
    
    # Pop операция
    start = time.perf_counter()
    for _ in range(n):
        stack.pop()
    end = time.perf_counter()
    results['pop'] = end - start
    
    return results


def benchmark_queue_operations(n: int = 10000) -> dict:
    """
    Бенчмарк операций с очередью.
    
    Args:
        n: Количество операций
        
    Returns:
        Словарь с временами выполнения операций
    """
    results = {}
    
    # Enqueue операция
    queue = Queue()
    start = time.perf_counter()
    for i in range(n):
        queue.enqueue(i)
    end = time.perf_counter()
    results['enqueue'] = end - start
    
    # Dequeue операция
    start = time.perf_counter()
    for _ in range(n):
        queue.dequeue()
    end = time.perf_counter()
    results['dequeue'] = end - start
    
    return results


def benchmark_linked_list_operations(n: int = 1000) -> dict:
    """
    Бенчмарк операций с односвязным списком.
    
    Args:
        n: Количество операций
        
    Returns:
        Словарь с временами выполнения операций
    """
    results = {}
    
    # Append операция
    linked_list = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(n):
        linked_list.append(i)
    end = time.perf_counter()
    results['append'] = end - start
    
    # Prepend операция
    linked_list = SinglyLinkedList()
    start = time.perf_counter()
    for i in range(n):
        linked_list.prepend(i)
    end = time.perf_counter()
    results['prepend'] = end - start
    
    # Insert в начало
    linked_list = SinglyLinkedList()
    for i in range(n):
        linked_list.append(i)
    
    start = time.perf_counter()
    linked_list.insert(0, -1)
    end = time.perf_counter()
    results['insert_beginning'] = end - start
    
    # Insert в середину
    start = time.perf_counter()
    linked_list.insert(n // 2, -1)
    end = time.perf_counter()
    results['insert_middle'] = end - start
    
    return results


def benchmark_list_operations(n: int = 10000) -> dict:
    """
    Бенчмарк операций с обычным списком Python для сравнения.
    
    Args:
        n: Количество операций
        
    Returns:
        Словарь с временами выполнения операций
    """
    results = {}
    
    # Добавление в конец (аналог append)
    py_list = []
    start = time.perf_counter()
    for i in range(n):
        py_list.append(i)
    end = time.perf_counter()
    results['append'] = end - start
    
    # Добавление в начало (дорогая операция!)
    py_list = []
    start = time.perf_counter()
    for i in range(n):
        py_list.insert(0, i)
    end = time.perf_counter()
    results['prepend'] = end - start
    
    # Удаление с начала (дорогая операция!)
    start = time.perf_counter()
    for _ in range(n):
        py_list.pop(0)
    end = time.perf_counter()
    results['pop_from_beginning'] = end - start
    
    return results


def run_all_benchmarks() -> None:
    """Запуск всех бенчмарков и вывод результатов."""
    print("=" * 60)
    print("БЕНЧМАРКИ СТРУКТУР ДАННЫХ")
    print("=" * 60)
    
    # Тестовые размеры
    sizes = [100, 1000, 10000]
    
    for n in sizes:
        print(f"\nРазмер данных: {n}")
        print("-" * 40)
        
        # Бенчмарк стека
        stack_results = benchmark_stack_operations(n)
        print(f"Stack.push/pop:   {stack_results['push']:.6f}s / {stack_results['pop']:.6f}s")
        
        # Бенчмарк очереди
        queue_results = benchmark_queue_operations(n)
        print(f"Queue.enq/deq:    {queue_results['enqueue']:.6f}s / {queue_results['dequeue']:.6f}s")
        
        # Бенчмарк списка Python (только для n <= 10000)
        if n <= 10000:
            list_results = benchmark_list_operations(n)
            print(f"List.append/insert0: {list_results['append']:.6f}s / {list_results['prepend']:.6f}s")
        
        # Бенчмарк связного списка (меньший размер из-за сложности O(n))
        if n <= 1000:
            ll_results = benchmark_linked_list_operations(n)
            print(f"LinkedList.append/prepend: {ll_results['append']:.6f}s / {ll_results['prepend']:.6f}s")
            print(f"LinkedList.insert_middle:  {ll_results['insert_middle']:.6f}s")


def compare_access_patterns() -> None:
    """Сравнение разных паттернов доступа."""
    print("\n" + "=" * 60)
    print("СРАВНЕНИЕ ДОСТУПА ПО ИНДЕКСУ И ПОСЛЕДОВАТЕЛЬНОГО ДОСТУПА")
    print("=" * 60)
    
    n = 10000
    
    # Массив (list) - быстрый произвольный доступ
    py_list = list(range(n))
    
    start = time.perf_counter()
    total = 0
    for i in range(0, n, 100):  # Доступ к каждому 100-му элементу
        total += py_list[i]
    end = time.perf_counter()
    print(f"List произвольный доступ: {end - start:.6f}s")
    
    # Связный список - медленный произвольный доступ
    linked_list = SinglyLinkedList()
    for i in range(n):
        linked_list.append(i)
    
    # Для связного списка доступ по индексу требует O(n) операций
    # Поэтому делаем меньше итераций
    start = time.perf_counter()
    total = 0
    values = list(linked_list)  # Преобразуем в list для доступа по индексу
    for i in range(0, min(n, 1000), 10):
        total += values[i]
    end = time.perf_counter()
    print(f"LinkedList произвольный доступ: {end - start:.6f}s")
    
    # Последовательный доступ одинаково эффективен
    print("\nПоследовательный доступ (итерация по всем элементам):")
    
    start = time.perf_counter()
    for _ in py_list:
        pass
    end = time.perf_counter()
    print(f"List: {end - start:.6f}s")
    
    start = time.perf_counter()
    for _ in linked_list:
        pass
    end = time.perf_counter()
    print(f"LinkedList: {end - start:.6f}s")


if __name__ == "__main__":
    run_all_benchmarks()
    compare_access_patterns()