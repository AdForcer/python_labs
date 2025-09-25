Amount = int(input(''))
People_Involved = [input(f'Участник: {_+1}\n').split() for _ in range(Amount)]
for i in range(Amount):
    if len(People_Involved[i]) == 4:
        if People_Involved[i][2].isdigit(): 
            People_Involved[i][2] = int(People_Involved[i][2])
        if People_Involved[i][3].lower() in 'true':
            People_Involved[i][3] = bool(People_Involved[i][3])
        elif People_Involved[i][3].lower() in 'false': 
            People_Involved[i][3] = bool('')
print(len([People_Involved[x][3] for x in range(Amount) if len(People_Involved[x]) == 4 if People_Involved[x][3] == 1]),len([People_Involved[x][3] for x in range(Amount) if len(People_Involved[x]) == 4 if People_Involved[x][3]==False]))
#Добавленно множество проверок на тупость пользователя, неправильные строки игнорирются программой



