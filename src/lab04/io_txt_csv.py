import csv
from pathlib import Path
from typing import Iterable, Sequence, Union


def read_text(path: Union[str, Path], encoding: str = "utf-8") -> str:

    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: Union[str, Path], header: tuple[str, ...] = None
) -> None:

    p = Path(path)
    rows_list = list(rows)

    # Проверка согласованности длин строк
    if rows_list:
        first_len = len(rows_list[0])
        for i, row in enumerate(rows_list):
            if len(row) != first_len:
                raise ValueError(
                    f"Строка {i} имеет длину {len(row)}, ожидалось {first_len}"
                )

    # Создание родительских директорий
    ensure_parent_dir(p)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows_list)


def ensure_parent_dir(path: Union[str, Path]) -> None:

    # Создает родительские директории, если их нет :()
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
