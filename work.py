import math

list0 = []
list1 = []
d = {}
d1 = {}
zv = ''
with open('azs.txt') as azs_file:  # достали из файла азс, сделали список
    for line in azs_file.readlines():
        list0.append(line.split())
number_kolonok = len(list0)

for i in list0:
    d[i[0]] = int(i[1]), i[2]
    for elem in i:
        if elem[:2] == 'АИ':
            d1[elem] = int(i[0]), int(i[1])
a = tuple(list0[1][:2])
d1['АИ-92'] += int(a[0]), int(a[1])

kol_avtom = len(d) + 1
nezapravilsa = 0
aivos = 0
aidevvt = 0
aidevvos = 0
aidevpat = 0
avtomat = 0
oz_na_1 = 0  # очередь на 1 колонку
oz_na_2 = 0  # очередь на 2 колонку
oz_na_3 = 0  # очередь на 3 колонку
oz = 0

with open('input.txt') as inp_file:  # список из файла инпут
    for line in inp_file.readlines():
        list1.append(line.split())

number_car = len(list0)

with open('output.txt', 'w') as file_out:
    for klient in list1:
        time_go = klient[0]
        kol_litr = klient[1]
        time_zapr = math.ceil(int(kol_litr) / 10)
        toplivo = klient[2]
        print(toplivo)
        avt = d1[toplivo]
        if len(avt) == 2:
            avtomat1 = avt[0]
        elif len(avt) == 4:
            avtomat2 = avt[0]
            avtomat3 = avt[2]
        if toplivo == 'АИ-80':
            oz_na_1 += 1
            if oz_na_1 <= d1['АИ-80'][1]:  # добавить время
                aivos += int(kol_litr)
                avtomat = d1['АИ-80'][0]
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
                oz = oz_na_1
            elif oz_na_1 > d1['АИ-80'][1]:
                oz_na_1 -= 1
                nezapravilsa += 1
                print('В  {}  новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.'.format(time_go,
                                                                                                            time_go,
                                                                                                            toplivo,
                                                                                                            kol_litr,
                                                                                                            time_zapr),
                      file=file_out)

        elif toplivo == 'АИ-92':  # добавить время

            oz_na_2 += 1
            if oz_na_2 <= d1['АИ-92'][3]:
                avtomat = d1['АИ-92'][2]
                oz = oz_na_2
                aidevvt += int(kol_litr)
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
            elif oz_na_2 > d1['АИ-92'][3] and oz_na_2 <= d1['АИ-92'][1]:
                avtomat = d1['АИ-92'][0]
                oz = oz_na_2
                aidevvt += int(kol_litr)
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
            elif oz_na_2 > d1['АИ-92'][1]:
                oz_na_2 -= 1
                nezapravilsa += 1
                print('В  {}  новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.'.format(time_go,
                                                                                                            time_go,
                                                                                                            toplivo,
                                                                                                            kol_litr,
                                                                                                            time_zapr),
                      file=file_out)

        elif toplivo == 'АИ-95' or toplivo == 'АИ-98':  # добвать время

            oz_na_3 += 1
            if oz_na_3 <= d1['АИ-95'][1]:
                avtomat = d1['АИ-95'][0]
                oz = oz_na_3
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
                if toplivo == 'АИ-95':
                    aidevpat += int(kol_litr)
                elif toplivo == 'АИ-98':
                    aidevvos += int(kol_litr)

            elif oz_na_3 > d1['АИ-95'][1]:
                oz_na_3 -= 1
                nezapravilsa += 1
                print('В  {}  новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.'.format(time_go,
                                                                                                            time_go,
                                                                                                            toplivo,
                                                                                                            kol_litr,
                                                                                                            time_zapr),
                      file=file_out)

        for avtomat_0 in list0:
            inform = avtomat_0[0]
            max_o = avtomat_0[1]
            mark_benz = avtomat_0[2]
            if len(avtomat_0) > 3:
                mark_benz = avtomat_0[2] + ' ' + avtomat_0[3] + ' ' + avtomat_0[4]

            if inform == '1':
                zv = oz_na_1 * '*'
            elif inform == '2':
                zv = oz_na_2 * '*'
            elif inform == '3':
                zv = oz_na_3 * '*'

            print('Автомат № {} максимальная очередь: {} Марки бензина: {} -> {}'.format(inform, max_o, mark_benz, zv),
                  file=file_out)
            number_car = len(list0)

print('Не заправились: {}'.format(nezapravilsa))
print('АИ-80 : {}'.format(aivos))
print('АИ-92 : {}'.format(aidevvt))
print('АИ-95 : {}'.format(aidevpat))
print('АИ-98 : {}'.format(aidevvos))
