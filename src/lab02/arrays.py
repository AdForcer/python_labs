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
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
#Ради шутки не использовал set() и sort()