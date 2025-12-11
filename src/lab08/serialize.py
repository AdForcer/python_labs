"""
Модуль для сериализации и десериализации студентов
"""

import json
from typing import List
from pathlib import Path

# Используем абсолютный импорт
try:
    from models import Student
except ImportError:
    # Для случая запуска напрямую
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from models import Student

def students_to_json(students: List[Student], path: str) -> None:
    """
    Сериализует список студентов в JSON файл
    
    Args:
        students: Список объектов Student
        path: Путь к файлу для сохранения
    
    Raises:
        ValueError: Если список студентов пуст
        IOError: Если возникла ошибка при записи файла
    """
    if not students:
        raise ValueError("Список студентов не может быть пустым")
    
    # Преобразуем студентов в словари
    data = [student.to_dict() for student in students]
    
    # Создаем директорию, если она не существует
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Сохраняем в JSON с красивым форматированием
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2, default=str)
        
        print(f"Данные успешно сохранены в {path}")
        print(f"Сохранено студентов: {len(students)}")
    except Exception as e:
        raise IOError(f"Ошибка при записи файла {path}: {str(e)}")

def students_from_json(path: str) -> List[Student]:
    """
    Десериализует список студентов из JSON файла
    
    Args:
        path: Путь к JSON файлу
    
    Returns:
        List[Student]: Список объектов Student
    
    Raises:
        FileNotFoundError: Если файл не найден
        ValueError: Если JSON некорректен или данные невалидны
        IOError: Если возникла ошибка при чтении файла
    """
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Некорректный JSON в файле {path}: {str(e)}")
    except Exception as e:
        raise IOError(f"Ошибка при чтении файла {path}: {str(e)}")
    
    if not isinstance(data, list):
        raise ValueError(f"Ожидается список в JSON файле, получено: {type(data)}")
    
    students = []
    errors = []
    
    for i, item in enumerate(data, 1):
        try:
            if not isinstance(item, dict):
                raise ValueError(f"Элемент {i} должен быть словарем, получено: {type(item)}")
            
            student = Student.from_dict(item)
            students.append(student)
        except Exception as e:
            errors.append(f"Студент {i}: {str(e)}")
    
    if errors:
        print("Обнаружены ошибки при загрузке:")
        for error in errors:
            print(f"  - {error}")
    
    if not students:
        raise ValueError("Не удалось загрузить ни одного студента")
    
    print(f"Загружено студентов: {len(students)}")
    if errors:
        print(f"Пропущено записей: {len(errors)}")
    
    return students