import json
import csv
from pathlib import Path

def read_json(file_path: str) -> list:

    #Читает JSON файл и возвращает данные

    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")
    
    if path.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {path.suffix}")
    
    with path.open('r', encoding='utf-8') as f:
        data = json.load(f)
    
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    
    if data and not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    return data


def read_csv(file_path: str) -> tuple[list, list]:

    #Читает CSV файл и возвращает заголовки и данные

    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path} не найден")
    
    if path.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {path.suffix}")
    
    with path.open('r', encoding='utf-8') as f:
        # Автоопределение разделителя
        sample = f.read(1024)
        f.seek(0)
        
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        
        reader = csv.reader(f, dialect)
        rows = list(reader)
    
    if not rows:
        raise ValueError("Пустой CSV файл")
    
    headers = rows[0]
    data = rows[1:]
    
    if not headers:
        raise ValueError("CSV файл не содержит заголовков")
    
    return headers, data
