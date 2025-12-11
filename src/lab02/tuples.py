def format_record(rec: tuple[str, str, float]) -> str:

    fio, group, gpa = rec

    if not isinstance(fio, str):
        return "ФИО должно быть строкой"

    if not isinstance(group, str):
        return "Группа должна быть строкой"

    if not isinstance(gpa, (int, float)):
        return "GPA должно быть числом"

    if len(fio) == 0:
        return "ФИО не может быть пустым"

    if len(group) == 0:
        return "Группа не может быть пустой"

    if gpa < 0:
        return "GPA не может быть отрицательным"

    fio_parts = " ".join(fio.split()).split()

    if len(fio_parts) < 2:
        return "ValueError"
    else:
        if len(fio_parts) == 2:
            initials = f"{fio_parts[1].upper()[0]}."
        else:
            initials = f"{fio_parts[1].upper()[0]}. {fio_parts[2].upper()[0]}."

    last_name = fio_parts[0]

    gpa_formatted = f"{gpa:.2f}"

    return f"{last_name} {initials}, гр. {group}, GPA {gpa_formatted}"


print("Проверки format_record")
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
