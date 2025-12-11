#!/usr/bin/env python3

import sys
from pathlib import Path
from collections import Counter

# Добавляем конкретные пути
current_dir = Path(__file__).parent
lib_dir = current_dir.parent / "lib"  # src/lib
sys.path.insert(0, str(lib_dir))
sys.path.insert(0, str(current_dir))

# Импортируем модули
from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def generate_report(
    input_file: str = "data/lab04/input.txt",
    output_file: str = "data/lab04/report.csv",
    encoding: str = "utf-8",
) -> None:

    try:
        # Чтение входного файла
        text = read_text(input_file, encoding=encoding)

        # Анализ текста
        freq = frequencies_from_text(text)
        sorted_counts = sorted_word_counts(freq)
        top_words = top_n(freq, 5)

        # Вывод статистики в консоль
        total_words = sum(freq.values())
        unique_words = len(freq)

        print(f"Всего слов: {total_words}")
        print(f"Уникальных слов: {unique_words}")
        print("Топ-5:")
        for word, count in top_words:
            print(f"  {word}: {count}")

        # Сохранение отчёта в CSV
        header = ("word", "count")
        write_csv(sorted_counts, output_file, header=header)
        print(f"\nОтчёт сохранён в: {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{input_file}' не найден.")
        sys.exit(1)
    except UnicodeDecodeError as e:
        print(f"Ошибка декодирования: {e}")
        print("Попробуйте указать другую кодировку с помощью --encoding")
        sys.exit(1)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")
        sys.exit(1)


def main():
    if len(sys.argv) > 1:
        # Базовая поддержка аргументов командной строки
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else "data/lab04/report.csv"
        generate_report(input_file, output_file)
    else:
        # Использование путей по умолчанию
        generate_report()


if __name__ == "__main__":
    main()
