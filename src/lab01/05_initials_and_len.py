Full_Name = input("ФИО: ")
Full_Name = Full_Name.split()
print(
    f"{Full_Name[0][0]}{Full_Name[1][0]}{Full_Name[2][0]}.\nДлина (символов): {sum([len(x) for x in Full_Name])+2}"
)
