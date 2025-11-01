# Лабалоторная номер № 2

## Задание 1 (arrays.py)
### 1. функция max_min
```python
def max_min(Array):

    if len(Array) == 0:
        return "ValueError"
    
    mmax = Array[0]
    mmin = Array[-1]

    for i in range(len(Array)):
        if Array[i] > mmax:
            mmax = Array[i]
        if Array[i] < mmin:
            mmin = Array[i]

    return (mmin,mmax)
```
![Картинка 8](../../images/lab02/1.1.png)
### 2. функция unique_sorted
```python
def unique_sorted(Array):

    if len(Array) == 0:
        return []
    
    tmp_Array = []

    for i in range(len(Array)):
        tmp_Array.append([Array[i], Array.count(Array[i])]) 

    New_Array = []

    for i in range(len(tmp_Array)-1):
        for j in range(len(tmp_Array)-1-i):
            if tmp_Array[j][0] > tmp_Array[j+1][0]:
                tmp_Array[j][0], tmp_Array[j+1][0] = tmp_Array[j+1][0], tmp_Array[j][0]

    i = 0

    while True:
        skip = tmp_Array[i][1]
        New_Array.append(tmp_Array[i][0])
        i+=skip
        if len(tmp_Array)<=i:
            break

    for i in range(len(New_Array)-1):
        for j in range(len(New_Array)-1-i):
            if New_Array[j] > New_Array[j+1]:
                New_Array[j], New_Array[j+1] = New_Array[j+1], New_Array[j]

    return New_Array
```
![Картинка 9](../../images/lab02/1.2.png)
### 3. функция flatten
```python
def flatten(Array):

    New_Array = []
    
    for NestedArray in Array:
        if isinstance(NestedArray, (tuple, list)): #проверка на то, массив это или нет
            for Element in NestedArray:
                New_Array.append(Element) 
        else: return "TypeError"

    return New_Array
```
![Картинка 9](../../images/lab02/1.3.png)

## Задание 2 (matrix.py)
### Дополнительная функция для проверки прямоугольности матрицы
```python
def square_matrix_check(matrix: list[list[float | int]]) -> bool:

    width = len(matrix[0])

    for i in range(len(matrix)):
        if len(matrix[i]) != width:
            return 0
    else:
        return 1
```
### 1. функция transpose
```python
def transpose(mat: list[list[float | int]]) -> list[list]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [[mat[i][j] for i in range(len(mat))] for j in range(len(mat[0]))]
```
![Картинка 10](../../images/lab02/2.1.png)
### 2. функция row_sums
```python 
def row_sums(mat: list[list[float | int]]) -> list[float]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [sum(row) for row in mat]
```
![Картинка 11](../../images/lab02/2.2.png)
### 3. функция
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:

    if square_matrix_check(mat) == 0:
        return "ValueError"
    
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(len(mat[0]))]
```
![Картинка 12](../../images/lab02/2.3.png)
## Задание 3 (tuples.py)
```python
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
    
    fio_parts = ' '.join(fio.split()).split()
    
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
```
![Картинка 13](../../images/lab02/3.1.png)