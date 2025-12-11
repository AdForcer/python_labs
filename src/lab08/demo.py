#!/usr/bin/env python3
"""
Главный скрипт для демонстрации работы модуля lab08
Запуск: python main.py (из папки lab08)
"""

import sys
import os
from pathlib import Path

# Импортируем напрямую из текущей директории
try:
    from models import Student
    from serialize import students_to_json, students_from_json
except ImportError:
    # Альтернативный способ импорта
    import sys
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from models import Student
    from serialize import students_to_json, students_from_json

def demonstrate_student_class():
    """Демонстрация работы класса Student"""
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА Student")
    print("=" * 50)
    
    # Создаем примеры студентов
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна Сергеевна", "2001-03-22", "SE-02", 4.8),
        Student("Сидоров Алексей Петрович", "1999-11-30", "SE-03", 3.9),
    ]
    
    for student in students:
        print("\n" + "-" * 30)
        print(student)  # Используется __str__
        print(f"Возраст (метод age()): {student.age()} лет")
        print(f"Краткая форма: {student.short_str()}")
        
        # Демонстрация сериализации/десериализации
        student_dict = student.to_dict()
        print(f"\nСловарь (to_dict): {student_dict}")
        
        # Создаем нового студента из словаря
        new_student = Student.from_dict(student_dict)
        print(f"Восстановлен из словаря: {new_student.short_str()}")
    
    return students

def demonstrate_serialization():
    """Демонстрация сериализации и десериализации"""
    print("\n" + "=" * 50)
    print("СЕРИАЛИЗАЦИЯ И ДЕСЕРИАЛИЗАЦИЯ")
    print("=" * 50)
    
    # Определяем пути относительно текущего файла
    current_dir = Path(__file__).parent
    project_root = current_dir.parent.parent
    
    input_path = project_root / "data" / "lab08" / "students_input.json"
    output_path = project_root / "data" / "lab08" / "students_output.json"
    
    try:
        # Чтение из файла
        print(f"\nЧтение студентов из файла: {input_path}")
        loaded_students = students_from_json(str(input_path))
        
        print("\nЗагруженные студенты:")
        for student in loaded_students:
            print(f"  - {student.short_str()}")
        
        # Добавляем нового студента
        new_student = Student("Новиков Павел Дмитриевич", "2003-01-14", "SE-04", 4.0)
        loaded_students.append(new_student)
        
        # Сохранение в файл
        print(f"\nСохранение студентов в файл: {output_path}")
        students_to_json(loaded_students, str(output_path))
        
        return loaded_students
        
    except Exception as e:
        print(f"Ошибка при работе с файлами: {e}")
        return []

def demonstrate_validation():
    """Демонстрация валидации данных"""
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ")
    print("=" * 50)
    
    test_cases = [
        ("Некорректный ФИО", "иванов иван", "2000-01-01", "SE-01", 4.0),
        ("Некорректный ФИО (2 слова)", "Иванов Иван", "2000-01-01", "SE-01", 4.0),
        ("Некорректная дата (формат)", "Иванов Иван Иванович", "01-01-2000", "SE-01", 4.0),
        ("Некорректная дата (значение)", "Иванов Иван Иванович", "2000-13-45", "SE-01", 4.0),
        ("Дата в будущем", "Иванов Иван Иванович", "2030-01-01", "SE-01", 4.0),
        ("GPA вне диапазона (отрицательный)", "Иванов Иван Иванович", "2000-01-01", "SE-01", -1.0),
        ("GPA вне диапазона (больше 5)", "Иванов Иван Иванович", "2000-01-01", "SE-01", 6.0),
        ("Пустая группа", "Иванов Иван Иванович", "2000-01-01", "", 4.0),
        ("Группа с пробелами", "Иванов Иван Иванович", "2000-01-01", "  ", 4.0),
        ("Корректные данные (граница 0)", "Тестов Тест Тестович", "2000-01-01", "TEST-01", 0.0),
        ("Корректные данные (граница 5)", "Тестов Тест Тестович", "2000-01-01", "TEST-01", 5.0),
    ]
    
    for description, fio, birthdate, group, gpa in test_cases:
        print(f"\nТест: {description}")
        print(f"  Данные: {fio}, {birthdate}, {group}, {gpa}")
        try:
            student = Student(fio, birthdate, group, gpa)
            print(f"  ✓ Успешно создан: {student.short_str()}")
        except ValueError as e:
            print(f"  ✗ Ошибка валидации: {e}")

def main():
    """Основная функция демонстрации"""
    try:
        # Демонстрация основных возможностей
        demonstrate_student_class()
        loaded_students = demonstrate_serialization()
        
        if loaded_students:
            # Демонстрация валидации
            demonstrate_validation()
        
        print("\n" + "=" * 50)
        print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ Произошла ошибка: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())