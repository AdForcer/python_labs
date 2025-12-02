import argparse
import sys
from pathlib import Path
from collections import Counter
import re


def read_text_file(filepath: str) -> str:
    """Чтение текстового файла с проверкой ошибок"""
    path = Path(filepath)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {filepath}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except IOError as e:
        raise IOError(f"Ошибка чтения файла: {e}")


def cat_command(input_file: str, number_lines: bool = False) -> None:
    """
    Реализация команды cat - вывод содержимого файла
    
    Args:
        input_file: путь к входному файлу
        number_lines: добавлять нумерацию строк
    """
    try:
        path = Path(input_file)
        if not path.exists():
            print(f"Ошибка: файл '{input_file}' не найден", file=sys.stderr)
            sys.exit(1)
        
        with open(path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            for i, line in enumerate(lines, 1):
                if number_lines:
                    # Убираем символ новой строки, потом добавляем обратно
                    line_content = line.rstrip('\n')
                    print(f"{i:6d}\t{line_content}")
                else:
                    print(line, end='')
                    
    except Exception as e:
        print(f"Ошибка при выполнении cat: {e}", file=sys.stderr)
        sys.exit(1)


def stats_command(input_file: str, top_n: int = 5) -> None:
    """
    Реализация команды stats - анализ частот слов
    
    Args:
        input_file: путь к входному файлу
        top_n: количество топ-слов для вывода
    """
    try:
        text = read_text_file(input_file)
        
        # Очистка текста и подсчет слов (функции из lab03)
        words = re.findall(r'\b[a-zA-Zа-яА-ЯёЁ]+\b', text.lower())
        
        if not words:
            print("Файл не содержит слов для анализа")
            return
        
        word_counts = Counter(words)
        
        print(f"Всего слов: {len(words)}")
        print(f"Уникальных слов: {len(word_counts)}")
        print(f"\nТоп-{top_n} самых частых слов:")
        print("-" * 30)
        
        for word, count in word_counts.most_common(top_n):
            percentage = (count / len(words)) * 100
            print(f"{word:<20} {count:>6} ({percentage:.2f}%)")
            
    except Exception as e:
        print(f"Ошибка при выполнении stats: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Основная функция CLI для работы с текстом"""
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для работы с текстом: cat и stats",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  %(prog)s cat --input data/samples/people.csv -n
  %(prog)s stats --input data/samples/example.txt --top 10
  
Пути относительно корня проекта python_labs/
        """
    )
    
    subparsers = parser.add_subparsers(
        dest="command",
        title="подкоманды",
        description="доступные команды",
        help="дополнительная информация по команде",
        required=True
    )
    
    # Подкоманда cat
    cat_parser = subparsers.add_parser(
        "cat",
        help="вывести содержимое файла построчно"
    )
    cat_parser.add_argument(
        "--input",
        dest="input_file",
        required=True,
        help="путь к входному файлу (например: data/samples/people.csv)"
    )
    cat_parser.add_argument(
        "-n", "--number",
        action="store_true",
        help="нумеровать строки вывода"
    )
    
    # Подкоманда stats
    stats_parser = subparsers.add_parser(
        "stats",
        help="проанализировать частоты слов в тексте"
    )
    stats_parser.add_argument(
        "--input",
        dest="input_file",
        required=True,
        help="путь к текстовому файлу"
    )
    stats_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="количество топ-слов для вывода (по умолчанию: 5)"
    )
    
    args = parser.parse_args()
    
    try:
        if args.command == "cat":
            cat_command(args.input_file, args.number)
        elif args.command == "stats":
            stats_command(args.input_file, args.top)
        else:
            parser.print_help()
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\nОперация прервана пользователем")
        sys.exit(130)
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()