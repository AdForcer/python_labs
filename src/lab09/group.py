import csv
from pathlib import Path
from typing import List, Optional
from datetime import datetime

from lab08.models import Student


class Group:
    """Класс для работы с хранилищем студентов в CSV-формате"""
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы с указанием пути к CSV-файлу
        
        Args:
            storage_path: Путь к CSV-файлу с данными студентов
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self) -> None:
        """Создаёт файл с заголовком, если его ещё нет"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self) -> List[dict]:
        """Читает все записи из CSV файла"""
        students_data = []
        
        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    students_data.append(row)
        except FileNotFoundError:
            self._ensure_storage_exists()
            return []
        
        return students_data
    
    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде списка объектов Student
        
        Returns:
            Список объектов Student
        """
        students_data = self._read_all()
        students = []
        
        for data in students_data:
            try:
                student = Student.from_dict(data)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(f"Ошибка при загрузке студента {data.get('fio', 'Unknown')}: {e}")
                continue
        
        return students
    
    def add(self, student: Student) -> None:
        """
        Добавляет нового студента в CSV
        
        Args:
            student: Объект Student для добавления
        """
        # Проверяем, нет ли уже студента с таким ФИО
        existing_students = self.list()
        for existing in existing_students:
            if existing.fio.lower() == student.fio.lower():
                raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        # Добавляем студента в файл
        with open(self.path, 'a', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writerow(student.to_dict())
    
    def find(self, substr: str) -> List[Student]:
        """
        Находит студентов по подстроке в ФИО
        
        Args:
            substr: Подстрока для поиска в ФИО
            
        Returns:
            Список найденных студентов
        """
        all_students = self.list()
        substr_lower = substr.lower()
        
        return [
            student for student in all_students 
            if substr_lower in student.fio.lower()
        ]
    
    def remove(self, fio: str) -> bool:
        """
        Удаляет запись(и) с данным ФИО
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если удаление прошло успешно, False если студент не найден
        """
        all_students = self.list()
        fio_lower = fio.lower()
        
        # Фильтруем студентов, оставляем только тех, у кого ФИО не совпадает
        remaining_students = [
            student for student in all_students 
            if student.fio.lower() != fio_lower
        ]
        
        # Если количество студентов не изменилось, значит студент не найден
        if len(remaining_students) == len(all_students):
            return False
        
        # Записываем обновлённый список обратно в файл
        self._write_all(remaining_students)
        return True
    
    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет поля существующего студента
        
        Args:
            fio: ФИО студента для обновления
            **fields: Поля для обновления (fio, birthdate, group, gpa)
            
        Returns:
            True если обновление прошло успешно, False если студент не найден
        """
        all_students = self.list()
        fio_lower = fio.lower()
        updated = False
        
        for student in all_students:
            if student.fio.lower() == fio_lower:
                # Обновляем указанные поля
                if 'fio' in fields:
                    student.fio = fields['fio']
                if 'birthdate' in fields:
                    student.birthdate = fields['birthdate']
                if 'group' in fields:
                    student.group = fields['group']
                if 'gpa' in fields:
                    student.gpa = float(fields['gpa'])
                
                # Проверяем валидность обновлённого объекта
                try:
                    # Создаём временный объект для валидации
                    Student(
                        fio=student.fio,
                        birthdate=student.birthdate,
                        group=student.group,
                        gpa=student.gpa
                    )
                except ValueError as e:
                    raise ValueError(f"Ошибка валидации обновлённых данных: {e}")
                
                updated = True
                break
        
        if updated:
            self._write_all(all_students)
        
        return updated
    
    def _write_all(self, students: List[Student]) -> None:
        """
        Записывает всех студентов в CSV файл
        
        Args:
            students: Список объектов Student для записи
        """
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            
            for student in students:
                writer.writerow(student.to_dict())
    
    def get_by_fio(self, fio: str) -> Optional[Student]:
        """
        Получает студента по точному ФИО
        
        Args:
            fio: ФИО студента
            
        Returns:
            Объект Student или None если не найден
        """
        all_students = self.list()
        fio_lower = fio.lower()
        
        for student in all_students:
            if student.fio.lower() == fio_lower:
                return student
        
        return None
    
    def count(self) -> int:
        """
        Возвращает количество студентов в группе
        
        Returns:
            Количество студентов
        """
        return len(self.list())
    
    def clear(self) -> None:
        """Очищает хранилище (оставляет только заголовок)"""
        self._ensure_storage_exists()
        # Перезаписываем файл только с заголовком
        with open(self.path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['fio', 'birthdate', 'group', 'gpa'])