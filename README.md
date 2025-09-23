# python_labs
Repo for my uni :0
Don't look at this it's boring and not cool :L

# Лабалоторная номер №1

## Задание 1
```python 
Name = input('Имя: \n')
Age = int(input('Возраст: \n'))
print(f'Привет, {Name}! Через год тебе будет {Age+1}')
```
## Задание 2
```python 
Number_A = float(input('a: ').replace(',','.'))
Number_B = float(input('b: ').replace(',','.'))
print(f'{sum([Number_A,Number_B]):.2f}',f'{sum([Number_A,Number_B])/len([Number_A,Number_B]):.2f}')
```
## Задание 3
```python
price, discount, vat = [float(input('\n')) for _ in range(3)]
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f'База после скидки: {base:.2f} ₽\nНДС:               {vat_amount:.2f} ₽\nИтого к оплате:    {total:.2f} ₽')
```
## Задания 4
```python
m = int(input())
print(f'{m//60}:{(m - (m//60)*60):02d}')
```
## Задание 5
```python
Full_Name = input('ФИО: ')
Full_Name = Full_Name.split()
print(f'{Full_Name[0][0]}{Full_Name[1][0]}{Full_Name[2][0]}.\nДлина (символов): {sum([len(x) for x in Full_Name])}')
```

![alt text](https://github.com/AdForcer/python_labs/tree/main/images/lab01/Task_1.png?raw=true)