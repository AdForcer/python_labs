"""
Реализация структур данных Stack и Queue.
"""
from collections import deque
from typing import Any, Optional


class Stack:
    """
    Структура данных "Стек" (LIFO - Last In, First Out).
    Реализована на основе встроенного списка Python.
    """
    
    def __init__(self) -> None:
        """Инициализация пустого стека."""
        self._data: list[Any] = []
    
    def push(self, item: Any) -> None:
        """
        Добавить элемент на вершину стека.
        
        Args:
            item: Элемент для добавления
            
        Time complexity: O(1) амортизированно
        """
        self._data.append(item)
    
    def pop(self) -> Any:
        """
        Снять верхний элемент стека и вернуть его.
        
        Returns:
            Верхний элемент стека
            
        Raises:
            IndexError: Если стек пуст
            
        Time complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """
        Вернуть верхний элемент без удаления.
        
        Returns:
            Верхний элемент или None, если стек пуст
            
        Time complexity: O(1)
        """
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """
        Проверить, пуст ли стек.
        
        Returns:
            True если стек пуст, иначе False
            
        Time complexity: O(1)
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        
        Returns:
            Количество элементов
            
        Time complexity: O(1)
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление стека."""
        return f"Stack({self._data})"


class Queue:
    """
    Структура данных "Очередь" (FIFO - First In, First Out).
    Реализована на основе collections.deque для оптимальной производительности.
    """
    
    def __init__(self) -> None:
        """Инициализация пустой очереди."""
        self._data: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Добавить элемент в конец очереди.
        
        Args:
            item: Элемент для добавления
            
        Time complexity: O(1)
        """
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """
        Взять элемент из начала очереди и вернуть его.
        
        Returns:
            Элемент из начала очереди
            
        Raises:
            IndexError: Если очередь пуста
            
        Time complexity: O(1)
        """
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """
        Вернуть первый элемент без удаления.
        
        Returns:
            Первый элемент или None, если очередь пуста
            
        Time complexity: O(1)
        """
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """
        Проверить, пуста ли очередь.
        
        Returns:
            True если очередь пуста, иначе False
            
        Time complexity: O(1)
        """
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        
        Returns:
            Количество элементов
            
        Time complexity: O(1)
        """
        return len(self._data)
    
    def __repr__(self) -> str:
        """Строковое представление очереди."""
        return f"Queue({list(self._data)})"