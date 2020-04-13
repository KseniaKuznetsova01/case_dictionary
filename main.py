import math

list = []
list1 = []
d = {}
with open('azs.txt') as azs_file:               # достали из файла азс, сделали список
    for line in azs_file.readlines():
        list.append(line.split())
print(list)
number_kolonok = len(list)

for i in range(number_kolonok):               # создаем словарь
    a = list[i]
    key = a[0]
    val = a[1]
    d[key] = val                            # номер колонки(строковый формат) - максимальное кол-во машин в очереди
    b = a[2:]
    for m in range(len(b)):
        key = b[m]
        val = a[0]
        if key not in d:  # марка безина(ключ) - номер колонки(значение)
            d[key] = val
        elif key in d:
            d[key] += val  # если марка бенза есть - чтоб было два номера колонки(значение)
        val = ''
    for t in range(len(b)):                  # номер колонки(формат инта) - марка бенза(значение
        key = int(a[0])
        val += b[t]
    d[key] = val

file_out = open('output.txt', 'w')
file_out.close()

with open('input.txt') as inp_file:  # список из файла инпут
    for line in inp_file.readlines():
        list1.append(line.split())

number_car = len(list)
file_out = open('output.txt', 'a')
for i in range(number_car):  # присваиваем переменным данные из инпута, время, кол-во литров
    f = list1[i]  # время заправки и марку(ниже вывод данных моделирования в файл аутпут)
    time = f[0]
    litr = int(f[1])                                  # Нужно такой же принт для момента когда чел валит с заправки
    time_zapravki = math.ceil(
        litr / 10)  # звездочки (т.е. создать живую очередь к автоматам и отказывать если там много людей)
    marka = f[2]  # и просуммировать то, что продали
    print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № '.format(time, time, marka, litr, time_zapravki),
          file=file_out)
    for z in range(number_kolonok):
        ii = str(z)
        print('Автомат №', z, ' максимальная очередь: ', d[ii], ' Марки бензина:', d[z], ' -> ')
        number_car = len(list)

        file_out.close()


# СЛОВАРИ

list = [['1', '3', 'АИ-80'], ['2', '2', 'АИ-92'], ['3', '4', 'АИ-92', 'АИ-95', 'АИ-98']]
d = {}
d1 = {}
for i in list:
    d[i[0]] = i[1:]
    for elem in i:
        if elem[:2] == 'АИ':
            d1[elem] = i[0], i[1]
a = tuple(list[1][:2])
print(a)
d1['АИ-92'] += a
print(d)
print(d1)
