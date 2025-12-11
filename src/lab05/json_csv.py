# src/lab05/json_csv.py
import json
import csv
from pathlib import Path
from typing import List, Dict, Any


def json_to_csv(json_path: str, csv_path: str) -> None:

    json_file = Path(json_path)
    csv_file = Path(csv_path)

    # Проверка существования файла
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")

    # Чтение JSON
    try:
        with json_file.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка парсинга JSON: {e}")

    # Валидация данных
    if not data:
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    # Получение всех уникальных ключей (порядок - алфавитный)
    all_keys = set()
    for item in data:
        all_keys.update(item.keys())
    fieldnames = sorted(all_keys)

    # Запись CSV
    csv_file.parent.mkdir(parents=True, exist_ok=True)

    with csv_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            # Заполняем отсутствующие поля пустыми строками
            complete_row = {key: row.get(key, "") for key in fieldnames}
            # Конвертируем все значения в строки
            complete_row = {
                k: str(v) if v is not None else "" for k, v in complete_row.items()
            }
            writer.writerow(complete_row)


def csv_to_json(csv_path: str, json_path: str) -> None:

    csv_file = Path(csv_path)
    json_file = Path(json_path)

    # Проверка существования файла
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")

    # Чтение CSV
    rows = []
    try:
        with csv_file.open("r", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            # Проверка наличия заголовка
            if reader.fieldnames is None:
                raise ValueError("CSV файл не содержит заголовка")

            for row in reader:
                rows.append(row)

    except csv.Error as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")

    # Валидация данных
    if not rows:
        raise ValueError("CSV файл пустой или содержит только заголовок")

    # Запись JSON
    json_file.parent.mkdir(parents=True, exist_ok=True)

    with json_file.open("w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
