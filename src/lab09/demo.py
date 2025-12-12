#!/usr/bin/env python3
"""
Демонстрация работы класса Group с CRUD-операциями
"""

import sys
import os
from pathlib import Path

# Получаем абсолютный путь к текущему файлу
current_file = Path(__file__).resolve()
# Поднимаемся на два уровня вверх к корню проекта (python_labs)
project_root = current_file.parent.parent.parent

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.insert(0, str(project_root))
# Также добавляем src для импорта lab08
sys.path.insert(0, str(project_root / "src"))

from src.lab09.group import Group
from src.lab08.models import Student


def main():
    """Основная функция демонстрации"""
    
    # Создаём путь к файлу данных относительно корня проекта
    data_path = project_root / "data" / "lab09" / "students.csv"
    
    # Убедимся, что директория существует
    data_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Создаём объект Group с указанием пути к CSV файлу
    print(f"Используем файл: {data_path}")
    group = Group(str(data_path))
    
    print("=" * 50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ CRUD-ОПЕРАЦИЙ")
    print("=" * 50)
    
    # 1. Добавление студентов
    print("\n1. ДОБАВЛЕНИЕ СТУДЕНТОВ:")
    print("-" * 30)
    
    try:
        student1 = Student(
            fio="Иванов Иван Иванович",
            birthdate="2003-10-10",
            group="БИВТ-21-1",
            gpa=4.3
        )
        group.add(student1)
        print(f"✓ Добавлен студент: {student1.fio}")
        print(f"  Группа: {student1.group}, GPA: {student1.gpa}")
    except ValueError as e:
        print(f"✗ Ошибка при добавлении студента 1: {e}")
    
    try:
        student2 = Student(
            fio="Петров Петр Петрович",
            birthdate="2002-05-15",
            group="БИВТ-21-1",
            gpa=3.8
        )
        group.add(student2)
        print(f"\n✓ Добавлен студент: {student2.fio}")
        print(f"  Группа: {student2.group}, GPA: {student2.gpa}")
    except ValueError as e:
        print(f"\n✗ Ошибка при добавлении студента 2: {e}")
    
    try:
        student3 = Student(
            fio="Сидорова Анна Ивановна",
            birthdate="2003-03-20",
            group="БИВТ-21-2",
            gpa=4.7
        )
        group.add(student3)
        print(f"\n✓ Добавлен студент: {student3.fio}")
        print(f"  Группа: {student3.group}, GPA: {student3.gpa}")
    except ValueError as e:
        print(f"\n✗ Ошибка при добавлении студента 3: {e}")
    
    print(f"\nВсего студентов в базе: {group.count()}")
    
    # 2. Вывод всех студентов
    print("\n\n2. СПИСОК ВСЕХ СТУДЕНТОВ:")
    print("-" * 30)
    students = group.list()
    
    if not students:
        print("В базе нет студентов")
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.fio}")
            print(f"   Дата рождения: {student.birthdate}")
            print(f"   Группа: {student.group}")
            print(f"   GPA: {student.gpa:.2f}")
            print(f"   Возраст: {student.age()} лет")
            if i < len(students):
                print()
    
    # 3. Поиск студентов
    print("\n\n3. ПОИСК СТУДЕНТОВ:")
    print("-" * 30)
    
    search_queries = ["Иван", "Петр", "Анна", "Смирнов"]
    
    for query in search_queries:
        print(f"\nПоиск по подстроке '{query}':")
        found = group.find(query)
        
        if found:
            for student in found:
                print(f"  ✓ Найден: {student.fio} ({student.group}, GPA: {student.gpa})")
        else:
            print(f"  ✗ Не найдено студентов с подстрокой '{query}'")
    
    # 4. Обновление студента
    print("\n\n4. ОБНОВЛЕНИЕ ДАННЫХ СТУДЕНТА:")
    print("-" * 30)
    
    student_to_update = "Иванов Иван Иванович"
    print(f"Обновление данных для: {student_to_update}")
    
    updated = group.update(
        student_to_update,
        gpa=4.5,  # Повысим GPA
        group="БИВТ-21-2"  # Переведём в другую группу
    )
    
    if updated:
        print("✓ Данные успешно обновлены:")
        student = group.get_by_fio(student_to_update)
        if student:
            print(f"  Новый GPA: {student.gpa}")
            print(f"  Новая группа: {student.group}")
    else:
        print(f"✗ Студент '{student_to_update}' не найден")
    
    # 5. Получение студента по точному ФИО
    print("\n\n5. ПОЛУЧЕНИЕ СТУДЕНТА ПО ФИО:")
    print("-" * 30)
    
    test_fios = ["Иванов Иван Иванович", "Несуществующий Студент"]
    
    for fio in test_fios:
        student = group.get_by_fio(fio)
        if student:
            print(f"✓ Найден студент: {student.fio}")
            print(f"  Полная информация:\n{student}")
        else:
            print(f"✗ Студент '{fio}' не найден")
    
    # 6. Удаление студента
    print("\n\n6. УДАЛЕНИЕ СТУДЕНТА:")
    print("-" * 30)
    
    student_to_remove = "Петров Петр Петрович"
    print(f"Попытка удаления: {student_to_remove}")
    
    removed = group.remove(student_to_remove)
    if removed:
        print("✓ Студент успешно удалён")
    else:
        print(f"✗ Студент '{student_to_remove}' не найден")
    
    # 7. Итоговый список
    print("\n\n7. ИТОГОВЫЙ СПИСОК СТУДЕНТОВ:")
    print("-" * 30)
    
    final_students = group.list()
    if not final_students:
        print("В базе нет студентов")
    else:
        print(f"Всего студентов: {len(final_students)}")
        for i, student in enumerate(final_students, 1):
            print(f"\n{i}. {student.short_str()}")
            print(f"   Возраст: {student.age()} лет")
    
    # 8. Проверка работы с неверными данными
    print("\n\n8. ПРОВЕРКА ВАЛИДАЦИИ ДАННЫХ:")
    print("-" * 30)
    
    print("Попытка добавить студента с неверными данными:")
    try:
        invalid_student = Student(
            fio="Некорректное Имя",  # Нет отчества
            birthdate="2025-01-01",  # Дата в будущем
            group="",
            gpa=6.0  # GPA больше 5
        )
        group.add(invalid_student)
    except ValueError as e:
        print(f"✗ Ошибка валидации (ожидаемо): {e}")
    
    # 9. Информация о файле
    print("\n\n9. ИНФОРМАЦИЯ О ХРАНИЛИЩЕ:")
    print("-" * 30)
    
    if data_path.exists():
        print(f"Файл данных: {data_path}")
        print(f"Размер файла: {data_path.stat().st_size} байт")
        
        # Чтение сырых данных из файла
        print("\nСодержимое файла (сырые данные):")
        print("-" * 20)
        with open(data_path, 'r', encoding='utf-8') as f:
            for line_num, line in enumerate(f, 1):
                print(f"{line_num}: {line.strip()}")
    else:
        print("Файл данных не найден")
    
    print("\n" + "=" * 50)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 50)


if __name__ == "__main__":
    main()