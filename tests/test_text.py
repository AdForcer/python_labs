# tests/test_text.py
import pytest
import sys
sys.path.append('src')  # Добавляем папку src в путь поиска
from lib.text import normalize, tokenize, count_freq, top_n

class TestNormalize:
    """Тесты для функции normalize"""
    
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ с Цифрами 123", "тест с цифрами 123"),
        ]
    )
    def test_normalize_basic(self, source, expected):
        """Базовые тесты нормализации"""
        assert normalize(source) == expected
    
    def test_normalize_without_casefold(self):
        """Тест с отключенным casefold"""
        assert normalize("ПрИвЕт Мир", casefold=False) == "ПрИвЕт Мир"
        assert normalize("ёжик", yo2e=True, casefold=False) == "ежик"
    
    def test_normalize_without_yo2e(self):
        """Тест с отключенной заменой ё->е"""
        assert normalize("ёжик", yo2e=False) == "ёжик"


class TestTokenize:
    """Тесты для функции tokenize"""
    
    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello world!", ["hello", "world"]),
            ("тест, с. пунктуацией!", ["тест", "с", "пунктуацией"]),
            ("", []),
            ("   ", []),
            ("word-with-hyphen", ["word-with-hyphen"]),
            ("multiple-hyphen-word-example", ["multiple-hyphen-word-example"]),
            ("цифры123 и символы_подчёркивания", ["цифры123", "и", "символы_подчёркивания"]),
            ("смесь English и русский", ["смесь", "English", "и", "русский"]),
        ]
    )
    def test_tokenize_basic(self, source, expected):
        """Базовые тесты токенизации"""
        assert tokenize(source) == expected


class TestCountFreq:
    """Тесты для функции count_freq"""
    
    def test_count_freq_basic(self):
        """Базовый тест подсчета частот"""
        tokens = ["яблоко", "яблоко", "груша", "яблоко", "груша", "банан"]
        result = count_freq(tokens)
        expected = {"яблоко": 3, "груша": 2, "банан": 1}
        assert result == expected
    
    def test_count_freq_empty(self):
        """Тест с пустым списком"""
        assert count_freq([]) == {}
    
    def test_count_freq_single_token(self):
        """Тест с одним токеном"""
        assert count_freq(["слово"]) == {"слово": 1}
    
    def test_count_freq_case_sensitive(self):
        """Тест чувствительности к регистру"""
        tokens = ["Word", "word", "WORD"]
        result = count_freq(tokens)
        expected = {"Word": 1, "word": 1, "WORD": 1}
        assert result == expected


class TestTopN:
    """Тесты для функции top_n"""
    
    def test_top_n_basic(self):
        """Базовый тест top_n"""
        freq = {"яблоко": 5, "груша": 3, "банан": 4, "апельсин": 2}
        result = top_n(freq, 3)
        expected = [("яблоко", 5), ("банан", 4), ("груша", 3)]
        assert result == expected
    
    def test_top_n_tie_breaker(self):
        """Тест обработки одинаковых частот (сортировка по алфавиту)"""
        freq = {"яблоко": 3, "груша": 3, "банан": 3, "апельсин": 2}
        result = top_n(freq, 4)
        expected = [("банан", 3), ("груша", 3), ("яблоко", 3), ("апельсин", 2)]
        assert result == expected
    
    def test_top_n_default_n(self):
        """Тест с дефолтным значением n=5"""
        freq = {f"word{i}": i for i in range(10)}
        result = top_n(freq)
        expected = [("word9", 9), ("word8", 8), ("word7", 7), ("word6", 6), ("word5", 5)]
        assert result == expected
    
    def test_top_n_n_larger_than_dict(self):
        """Тест когда n больше размера словаря"""
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 10)
        expected = [("b", 2), ("a", 1)]
        assert result == expected
    
    def test_top_n_empty_dict(self):
        """Тест с пустым словарем"""
        assert top_n({}) == []
        assert top_n({}, 5) == []


class TestIntegration:
    """Интеграционные тесты для всех функций"""
    
    def test_full_workflow(self):
        """Полный пайплайн обработки текста"""
        text = "Привет, мир! Мир привет. Ещё один тест-пример."
        
        # Нормализация
        normalized = normalize(text)
        assert normalized == "привет, мир! мир привет. еще один тест-пример."
        
        # Токенизация
        tokens = tokenize(normalized)
        assert tokens == ["привет", "мир", "мир", "привет", "еще", "один", "тест-пример"]
        
        # Подсчет частот
        freq = count_freq(tokens)
        assert freq == {"привет": 2, "мир": 2, "еще": 1, "один": 1, "тест-пример": 1}
        
        # Топ N
        top = top_n(freq, 2)
        assert top == [("мир", 2), ("привет", 2)]