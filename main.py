#!/usr/bin/env python3
"""
Пример использования модуля lab08
"""

import sys
from pathlib import Path

# Добавляем src в путь для импорта
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from lab08.models import Student
from lab08.serialize import students_to_json, students_from_json

def main():
    """Основная функция демонстрации"""
    
    # Создаем примеры студентов
    students = [
        Student("Иванов Иван Иванович", "2000-05-15", "SE-01", 4.5),
        Student("Петрова Анна Сергеевна", "2001-03-22", "SE-02", 4.8),
        Student("Сидоров Алексей Петрович", "1999-11-30", "SE-03", 3.9),
    ]
    
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КЛАССА Student")
    print("=" * 50)
    
    # Демонстрация методов Student
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
    
    print("\n" + "=" * 50)
    print("СЕРИАЛИЗАЦИЯ И ДЕСЕРИАЛИЗАЦИЯ")
    print("=" * 50)
    
    # Пути к файлам
    input_path = "data/lab08/students_input.json"
    output_path = "data/lab08/students_output.json"
    
    try:
        # Чтение из файла
        print(f"\nЧтение студентов из файла: {input_path}")
        loaded_students = students_from_json(input_path)
        
        print("\nЗагруженные студенты:")
        for student in loaded_students:
            print(f"  - {student.short_str()}")
        
        # Добавляем нового студента
        new_student = Student("Новиков Павел Дмитриевич", "2003-01-14", "SE-04", 4.0)
        loaded_students.append(new_student)
        
        # Сохранение в файл
        print(f"\nСохранение студентов в файл: {output_path}")
        students_to_json(loaded_students, output_path)
        
        # Демонстрация валидации
        print("\n" + "=" * 50)
        print("ДЕМОНСТРАЦИЯ ВАЛИДАЦИИ")
        print("=" * 50)
        
        # Попытка создать студента с некорректными данными
        test_cases = [
            ("Некорректный ФИО", "иванов иван", "2000-01-01", "SE-01", 4.0),
            ("Некорректная дата", "Иванов Иван Иванович", "01-01-2000", "SE-01", 4.0),
            ("GPA вне диапазона", "Иванов Иван Иванович", "2000-01-01", "SE-01", 6.0),
            ("Пустая группа", "Иванов Иван Иванович", "2000-01-01", "", 4.0),
        ]
        
        for description, fio, birthdate, group, gpa in test_cases:
            print(f"\nТест: {description}")
            try:
                student = Student(fio, birthdate, group, gpa)
                print(f"  ✓ Успешно создан: {student.short_str()}")
            except ValueError as e:
                print(f"  ✗ Ошибка валидации: {e}")
        
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())