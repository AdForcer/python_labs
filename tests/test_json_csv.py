# tests/test_json_csv.py
import pytest
import sys
import json
import csv
from pathlib import Path

sys.path.append('src')

from lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""
    
    def test_json_to_csv_basic(self, tmp_path):
        """Базовый тест конвертации JSON -> CSV"""
        # Создаем тестовый JSON файл
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"
        
        data = [
            {"name": "Алиса", "age": 22, "city": "Москва"},
            {"name": "Боб", "age": 25, "city": "Санкт-Петербург"},
            {"name": "Чарли", "age": 30, "city": "Казань"}
        ]
        
        json_file.write_text(json.dumps(data, ensure_ascii=False, indent=2), 
                            encoding="utf-8")
        
        # Выполняем конвертацию
        json_to_csv(str(json_file), str(csv_file))
        
        # Проверяем результат
        assert csv_file.exists()
        
        with csv_file.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) == 3
        assert set(rows[0].keys()) == {"age", "city", "name"}  # алфавитный порядок
        assert rows[0]["name"] == "Алиса"
        assert rows[0]["age"] == "22"
        assert rows[0]["city"] == "Москва"
    
    def test_json_to_csv_missing_fields(self, tmp_path):
        """Тест с отсутствующими полями в некоторых записях"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"
        
        data = [
            {"name": "Алиса", "age": 22},
            {"name": "Боб", "city": "Москва"},
            {"name": "Чарли", "age": 30, "city": "Казань", "job": "Developer"}
        ]
        
        json_file.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        json_to_csv(str(json_file), str(csv_file))
        
        with csv_file.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        # Должны быть все поля из всех записей
        assert set(rows[0].keys()) == {"age", "city", "job", "name"}
        
        # Проверяем заполнение пустыми строками
        assert rows[0]["city"] == ""  # У Алисы нет города
        assert rows[0]["job"] == ""   # У Алисы нет работы
    
    def test_json_to_csv_empty_list(self, tmp_path):
        """Тест с пустым списком в JSON"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"
        
        json_file.write_text("[]", encoding="utf-8")
        
        with pytest.raises(ValueError, match="Пустой JSON"):
            json_to_csv(str(json_file), str(csv_file))
    
    def test_json_to_csv_invalid_json(self, tmp_path):
        """Тест с некорректным JSON"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"
        
        json_file.write_text("{invalid json", encoding="utf-8")
        
        with pytest.raises(ValueError, match="Ошибка парсинга JSON"):
            json_to_csv(str(json_file), str(csv_file))
    
    def test_json_to_csv_not_list(self, tmp_path):
        """Тест когда JSON не список"""
        json_file = tmp_path / "test.json"
        csv_file = tmp_path / "test.csv"
        
        json_file.write_text('{"name": "Alice"}', encoding="utf-8")
        
        with pytest.raises(ValueError, match="JSON должен содержать список"):
            json_to_csv(str(json_file), str(csv_file))
    
    def test_json_to_csv_file_not_found(self, tmp_path):
        """Тест когда файл не существует"""
        json_file = tmp_path / "nonexistent.json"
        csv_file = tmp_path / "test.csv"
        
        with pytest.raises(FileNotFoundError):
            json_to_csv(str(json_file), str(csv_file))


class TestCsvToJson:
    """Тесты для функции csv_to_json"""
    
    def test_csv_to_json_basic(self, tmp_path):
        """Базовый тест конвертации CSV -> JSON"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"
        
        # Создаем CSV файл
        csv_data = """name,age,city
Алиса,22,Москва
Боб,25,Санкт-Петербург
Чарли,30,Казань"""
        
        csv_file.write_text(csv_data, encoding="utf-8")
        
        # Выполняем конвертацию
        csv_to_json(str(csv_file), str(json_file))
        
        # Проверяем результат
        assert json_file.exists()
        
        with json_file.open(encoding="utf-8") as f:
            data = json.load(f)
        
        assert len(data) == 3
        assert data[0] == {"name": "Алиса", "age": "22", "city": "Москва"}
        assert data[1] == {"name": "Боб", "age": "25", "city": "Санкт-Петербург"}
    
    def test_csv_to_json_empty_file(self, tmp_path):
        """Тест с пустым CSV файлом"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"
        
        csv_file.write_text("", encoding="utf-8")
        
        with pytest.raises(ValueError, match="CSV файл не содержит заголовка"):
            csv_to_json(str(csv_file), str(json_file))
    
    def test_csv_to_json_only_header(self, tmp_path):
        """Тест с CSV содержащим только заголовок"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"
        
        csv_file.write_text("name,age,city", encoding="utf-8")
        
        with pytest.raises(ValueError, match="CSV файл пустой"):
            csv_to_json(str(csv_file), str(json_file))
    
    def test_csv_to_json_invalid_csv(self, tmp_path):
        """Тест с некорректным CSV"""
        csv_file = tmp_path / "test.csv"
        json_file = tmp_path / "test.json"
        
        # CSV с разным количеством полей в строках
        csv_file.write_text("name,age\nАлиса,\"незакрытая кавычка", encoding="utf-8")
        
        with pytest.raises(ValueError, match="Ошибка чтения CSV"):
            csv_to_json(str(csv_file), str(json_file))
    
    def test_csv_to_json_file_not_found(self):
        """Тест когда файл не существует"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")


class TestRoundTrip:
    """Тесты полного цикла конвертации JSON -> CSV -> JSON"""
    
    def test_round_trip_basic(self, tmp_path):
        """Полный цикл конвертации"""
        # Исходные данные
        original_data = [
            {"name": "Алиса", "age": 22, "city": "Москва"},
            {"name": "Боб", "age": 25, "city": "Санкт-Петербург"},
            {"name": "Чарли", "age": 30, "city": "Казань", "job": "Developer"}
        ]
        
        # Сохраняем исходный JSON
        json_file1 = tmp_path / "original.json"
        json_file1.write_text(json.dumps(original_data, ensure_ascii=False, indent=2), 
                             encoding="utf-8")
        
        # Конвертируем JSON -> CSV
        csv_file = tmp_path / "converted.csv"
        json_to_csv(str(json_file1), str(csv_file))
        
        # Конвертируем CSV -> JSON
        json_file2 = tmp_path / "final.json"
        csv_to_json(str(csv_file), str(json_file2))
        
        # Загружаем результат
        with json_file2.open(encoding="utf-8") as f:
            final_data = json.load(f)
        
        # Проверяем, что данные совпадают (с учетом преобразования типов)
        assert len(final_data) == len(original_data)
        
        for original, final in zip(original_data, final_data):
            for key in original:
                # Все значения в CSV/JSON становятся строками
                assert str(original[key]) == final[key]
    
    def test_round_trip_with_special_chars(self, tmp_path):
        """Тест с специальными символами"""
        original_data = [
            {"имя": "Иван", "описание": "Строка с запятыми, кавычками \" и переносами\nстрок"},
            {"имя": "Мария", "описание": "Ещё один тест"}
        ]
        
        json_file1 = tmp_path / "original.json"
        csv_file = tmp_path / "converted.csv"
        json_file2 = tmp_path / "final.json"
        
        json_file1.write_text(json.dumps(original_data, ensure_ascii=False), 
                             encoding="utf-8")
        
        json_to_csv(str(json_file1), str(csv_file))
        csv_to_json(str(csv_file), str(json_file2))
        
        with json_file2.open(encoding="utf-8") as f:
            final_data = json.load(f)
        
        assert len(final_data) == 2
        # CSV корректно обрабатывает кавычки и переносы строк
        assert final_data[0]["имя"] == "Иван"