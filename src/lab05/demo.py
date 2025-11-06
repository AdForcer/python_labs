#!/usr/bin/env python3

import sys
from pathlib import Path


src_path = Path(__file__).parent.parent
sys.path.append(str(src_path))

from lab05.json_csv import json_to_csv, csv_to_json
from lab05.csv_xlsx import csv_to_xlsx


def main():
    #Пути к файлам
    samples_dir = Path("data/samples")
    out_dir = Path("data/out")
    
    #Создаем выходную директорию
    out_dir.mkdir(parents=True, exist_ok=True)

    
    try:
        #JSON → CSV
        json_to_csv(
            samples_dir / "people.json",
            out_dir / "people_from_json.csv"
        )
        
        #CSV → JSON
        csv_to_json(
            samples_dir / "people.csv",
            out_dir / "people_from_csv.json"
        )
        
        #CSV → XLSX (из people.csv)
        csv_to_xlsx(
            samples_dir / "people.csv",
            out_dir / "people.xlsx"
        )
        
        #CSV → XLSX (из cities.csv)
        csv_to_xlsx(
            samples_dir / "cities.csv",
            out_dir / "cities.xlsx"
        )
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())