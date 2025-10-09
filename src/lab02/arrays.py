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

#проверки
print('Проверка max_min')
print(max_min([3, -1, 5, 5, 0]))
print(max_min([42]))
print(max_min([-5, -2, -9]))
print(max_min([]))
print(max_min([-5, -2, -9]))

def unique_sorted(Array):
    if len(Array) == 0:
        return []
    
    tmp_Array = []

    for i in range(len(Array)):
        tmp_Array.append([Array[i], Array.count(Array[i])]) 

    """
    Матрица c элементом и числом повторений элемента в массиве, число повторенний пригодится для того, 
    чтобы пропускать элементы (мы знаем их кол-во) после сортировки.
    Пример: [(1,3),(1,3),(1,3),(2,2),(2,2)]
    На элементе ноль мы можем перескочить на 3 шага, на элемент 3 (который уже отличен).
    Таким образом я реализовал set() ибо непонятно, какими функция можно пользоваться или нет.
    Решил по приколу не использовать sort() и set() в этой функции, так как это бы было больно просто.
    Как работает бабл сорт и остальная часть объяснять не буду, достаточно просто код прочесть >:)
    """
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

#проверки
print('\nПроверки unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

def flatten(Array):
    New_Array = []
    for NestedArray in Array:
        if isinstance(NestedArray, (tuple, list)): #проверка на то, массив это или нет
            for Element in NestedArray:
                New_Array.append(Element) 
                '''
                Добавление эллементов в новый массив 
                (ибо, если это tuple, то я не смогу его поменять, а на память пофег)
                '''
        else: return "TypeError"

    return New_Array

#проверки
print('\nПроверки flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))