from dataclasses import dataclass
from datetime import datetime, date
import re
from typing import ClassVar

@dataclass
class Student:
    """Класс, представляющий студента"""
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    # Валидационные регулярные выражения
    _date_pattern: ClassVar[re.Pattern] = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    _fio_pattern: ClassVar[re.Pattern] = re.compile(r'^[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+\s[А-ЯЁ][а-яё]+$')
    
    def __post_init__(self):
        """Валидация данных после инициализации"""
        # Валидация ФИО
        if not self._fio_pattern.match(self.fio):
            raise ValueError(f"Некорректный формат ФИО: {self.fio}. Ожидается: 'Фамилия Имя Отчество'")
        
        # Валидация даты рождения
        if not self._date_pattern.match(self.birthdate):
            raise ValueError(f"Некорректный формат даты: {self.birthdate}. Ожидается: YYYY-MM-DD")
        
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Некорректная дата: {self.birthdate}")
        
        # Проверка, что дата не в будущем
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        if birth_date > date.today():
            raise ValueError(f"Дата рождения не может быть в будущем: {self.birthdate}")
        
        # Валидация GPA
        if not (0.0 <= self.gpa <= 5.0):
            raise ValueError(f"GPA должен быть в диапазоне от 0 до 5, получено: {self.gpa}")
        
        # Валидация группы
        if not self.group or len(self.group.strip()) == 0:
            raise ValueError("Номер группы не может быть пустым")
    
    def age(self) -> int:
        """Возвращает возраст студента в полных годах"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        age = today.year - birth_date.year
        
        # Учитываем, был ли уже день рождения в этом году
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        
        return age
    
    def to_dict(self) -> dict:
        """Сериализует объект Student в словарь"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Student':
        """Десериализует объект Student из словаря"""
        # Проверяем обязательные поля
        required_fields = ['fio', 'birthdate', 'group', 'gpa']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field}")
        
        # Создаем объект Student
        return cls(
            fio=data['fio'],
            birthdate=data['birthdate'],
            group=data['group'],
            gpa=float(data['gpa'])
        )
    
    def __str__(self) -> str:
        """Возвращает строковое представление студента"""
        return f"Студент: {self.fio}\n" \
               f"Возраст: {self.age()} лет\n" \
               f"Группа: {self.group}\n" \
               f"Средний балл: {self.gpa:.2f}"
    
    def short_str(self) -> str:
        """Краткое строковое представление"""
        return f"{self.fio}, {self.group}, GPA: {self.gpa:.2f}"