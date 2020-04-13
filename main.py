import math

list = []
list1 = []
d = {}
with open('azs.txt') as azs_file:  # достали из файла азс, сделали список
    for line in azs_file.readlines():
        list.append(line.split())
number_kolonok = len(list)

# СЛОВАРИ
d1 = {}
for i in list:
    d[i[0]] = int(i[1]), i[2]
    for elem in i:
        if elem[:2] == 'АИ':
            d1[elem] = int(i[0]), int(i[1])
a = tuple(list[1][:2])
d1['АИ-92'] += int(a[0]), int(a[1])
print(d)
print(d1)



file_out = open('output.txt', 'w')
file_out.close()

with open('input.txt') as inp_file:  # список из файла инпут
    for line in inp_file.readlines():
        list1.append(line.split())

number_car = len(list)
with open('output.txt', 'a') as file_out:
    for i in range(number_car):  # присваиваем переменным данные из инпута, время, кол-во литров
        f = list1[i]  # время заправки и марку(ниже вывод данных моделирования в файл аутпут)
        time = f[0]
        litr = int(f[1])  # Нужно такой же принт для момента когда чел валит с заправки
        time_zapravki = math.ceil(
            litr / 10)  # звездочки (т.е. создать живую очередь к автоматам и отказывать если там много людей)
        marka = f[2]  # и просуммировать то, что продали
        print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time, time, marka, litr,
                                                                                      time_zapravki, d[marka]),
              file=file_out)

        for z in range(1, number_kolonok + 1):
            a = d['номер колонки']
            print('Автомат № {} максимальная очередь: {} Марки бензина: {} -> '.format(z, a[1], 'номер колонки'), file=file_out)
            number_car = len(list)
