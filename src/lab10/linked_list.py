"""
Реализация односвязного списка (Singly Linked List).
"""
from typing import Any, Optional, Iterator


class Node:
    """
    Узел односвязного списка.
    
    Attributes:
        value: Значение, хранящееся в узле
        next: Ссылка на следующий узел или None
    """
    
    def __init__(self, value: Any, next: Optional['Node'] = None) -> None:
        """
        Инициализация узла.
        
        Args:
            value: Значение узла
            next: Следующий узел (по умолчанию None)
        """
        self.value = value
        self.next = next
    
    def __repr__(self) -> str:
        """Строковое представление узла."""
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    Односвязный список.
    
    Поддерживает операции добавления, удаления и итерации по элементам.
    Для ускорения добавления в конец поддерживается ссылка на хвост (tail).
    """
    
    def __init__(self) -> None:
        """Инициализация пустого списка."""
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        """
        Добавить элемент в конец списка.
        
        Args:
            value: Значение для добавления
            
        Time complexity: O(1)
        """
        new_node = Node(value)
        
        if self.head is None:
            # Список пуст, новый узел становится и головой, и хвостом
            self.head = new_node
            self.tail = new_node
        else:
            # Добавляем после текущего хвоста
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """
        Добавить элемент в начало списка.
        
        Args:
            value: Значение для добавления
            
        Time complexity: O(1)
        """
        new_node = Node(value, self.head)
        self.head = new_node
        
        # Если список был пуст, новый узел становится и хвостом
        if self.tail is None:
            self.tail = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """
        Вставить элемент по указанному индексу.
        
        Args:
            idx: Индекс для вставки (должен быть в диапазоне [0, len(list)])
            value: Значение для вставки
            
        Raises:
            IndexError: Если индекс вне допустимого диапазона
            
        Time complexity: O(n) в худшем случае
        """
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size}]")
        
        # Вставка в начало
        if idx == 0:
            self.prepend(value)
            return
        
        # Вставка в конец
        if idx == self._size:
            self.append(value)
            return
        
        # Вставка в середину
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node = Node(value, current.next)
        current.next = new_node
        self._size += 1
    
    def remove(self, value: Any) -> bool:
        """
        Удалить первое вхождение значения из списка.
        
        Args:
            value: Значение для удаления
            
        Returns:
            True если элемент был найден и удалён, иначе False
            
        Time complexity: O(n)
        """
        if self.head is None:
            return False
        
        # Удаление из начала
        if self.head.value == value:
            self.head = self.head.next
            
            # Если список стал пустым
            if self.head is None:
                self.tail = None
            
            self._size -= 1
            return True
        
        # Поиск элемента для удаления
        current = self.head
        while current.next is not None and current.next.value != value:
            current = current.next
        
        # Элемент не найден
        if current.next is None:
            return False
        
        # Удаление элемента
        current.next = current.next.next
        
        # Если удалили последний элемент
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return True
    
    def remove_at(self, idx: int) -> Any:
        """
        Удалить элемент по индексу.
        
        Args:
            idx: Индекс элемента для удаления
            
        Returns:
            Значение удалённого элемента
            
        Raises:
            IndexError: Если индекс вне допустимого диапазона
            
        Time complexity: O(n) в худшем случае
        """
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range [0, {self._size - 1}]")
        
        # Удаление из начала
        if idx == 0:
            value = self.head.value
            self.head = self.head.next
            
            # Если список стал пустым
            if self.head is None:
                self.tail = None
            
            self._size -= 1
            return value
        
        # Удаление из середины или конца
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        value = current.next.value
        current.next = current.next.next
        
        # Если удалили последний элемент
        if current.next is None:
            self.tail = current
        
        self._size -= 1
        return value
    
    def __iter__(self) -> Iterator[Any]:
        """
        Возвращает итератор по значениям в списке.
        
        Yields:
            Значения узлов в порядке от головы к хвосту
        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """
        Возвращает количество элементов в списке.
        
        Returns:
            Количество элементов
        """
        return self._size
    
    def __repr__(self) -> str:
        """Строковое представление списка."""
        values = list(self)
        return f"SinglyLinkedList({values})"