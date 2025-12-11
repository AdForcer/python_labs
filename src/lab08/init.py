"""
Модуль для работы со студентами (Лабораторная работа 8)

Использование:
    python -m lab08.main
"""

from .models import Student
from .serialize import students_to_json, students_from_json

__version__ = "1.0.0"
__all__ = [
    'Student',
    'students_to_json', 
    'students_from_json'
]