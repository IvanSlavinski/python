""" архивирование кортежа кортежей и списка в один, затем конвертация в словарь - функция zip! """
#flats = ((1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16), (17, 18, 19, 20))
flats = list()
temp = list()
for i in range(1, 21):
    temp.append(i)
    if len(temp) == 4:
        flats.append(tuple(temp))
        temp = list()
    else:
        continue
print(flats)
flats = tuple(flats)
floors = tuple(range(1, 6))

dict_floors_flats = dict(zip(flats, floors))
print(dict_floors_flats)

flat_number = int(input("Enter a flat number:"))
for key, value in dict_floors_flats.items():
    if flat_number in key:
        print(f"The {flat_number} flat is on the {value} floor")




