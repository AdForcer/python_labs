import argparse
import sys
from pathlib import Path

# Для корректного импорта модулей из lab05
try:
    # Если запускаем из корня проекта python_labs/
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from src.lab05.csv_xlsx import csv_to_xlsx
except ImportError:
    # Если запускаем из директории src/lab06/
    import sys
    import os

    # Добавляем родительскую директорию в путь
    sys.path.insert(
        0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    )
    from src.lab05.json_csv import json_to_csv, csv_to_json
    from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    """Основная функция CLI для конвертации данных"""
    parser = argparse.ArgumentParser(
        description="Конвертер данных между форматами JSON, CSV и XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования (относительно корня проекта python_labs/):
  python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people.csv
  python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people.json
  python -m src.lab06.cli_convert csv2xlsx --in data/samples/cities.csv --out data/out/cities.xlsx
  
Аргументы:
  --in     Входной файл (обязательный)
  --out    Выходной файл (обязательный)
        """,
    )

    subparsers = parser.add_subparsers(
        dest="command",
        title="доступные команды конвертации",
        description="выберите команду для выполнения",
        help="дополнительная справка по командам",
        required=True,
    )

    # Команда json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="конвертировать JSON файл в CSV формат"
    )
    json2csv_parser.add_argument(
        "--in", dest="input_file", required=True, help="путь к входному JSON файлу"
    )
    json2csv_parser.add_argument(
        "--out", dest="output_file", required=True, help="путь для сохранения CSV файла"
    )

    # Команда csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="конвертировать CSV файл в JSON формат"
    )
    csv2json_parser.add_argument(
        "--in", dest="input_file", required=True, help="путь к входному CSV файлу"
    )
    csv2json_parser.add_argument(
        "--out",
        dest="output_file",
        required=True,
        help="путь для сохранения JSON файла",
    )

    # Команда csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="конвертировать CSV файл в XLSX (Excel) формат"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input_file", required=True, help="путь к входному CSV файлу"
    )
    csv2xlsx_parser.add_argument(
        "--out",
        dest="output_file",
        required=True,
        help="путь для сохранения XLSX файла",
    )

    args = parser.parse_args()

    # Если команда не указана, показываем справку
    if not args.command:
        parser.print_help()
        return

    try:
        if args.command == "json2csv":
            print(f"Конвертация JSON в CSV:")
            print(f"  Входной файл: {args.input_file}")
            print(f"  Выходной файл: {args.output_file}")

            # Создаем директорию для выходного файла, если её нет
            output_path = Path(args.output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            json_to_csv(args.input_file, args.output_file)
            print("✓ Конвертация успешно завершена!")

        elif args.command == "csv2json":
            print(f"Конвертация CSV в JSON:")
            print(f"  Входной файл: {args.input_file}")
            print(f"  Выходной файл: {args.output_file}")

            # Создаем директорию для выходного файла, если её нет
            output_path = Path(args.output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            csv_to_json(args.input_file, args.output_file)
            print("✓ Конвертация успешно завершена!")

        elif args.command == "csv2xlsx":
            print(f"Конвертация CSV в XLSX:")
            print(f"  Входной файл: {args.input_file}")
            print(f"  Выходной файл: {args.output_file}")

            # Создаем директорию для выходного файла, если её нет
            output_path = Path(args.output_file)
            output_path.parent.mkdir(parents=True, exist_ok=True)

            csv_to_xlsx(args.input_file, args.output_file)
            print("✓ Конвертация успешно завершена!")

        else:
            parser.print_help()
            sys.exit(1)

    except FileNotFoundError as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        print("Проверьте правильность пути к файлу", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка данных: {e}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nКонвертация прервана пользователем")
        sys.exit(130)
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
