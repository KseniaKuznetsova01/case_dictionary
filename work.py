import math

zv = ''

d = {'1': (3, 'АИ-80'), '2': (2, 'АИ-92'), '3': (4, 'АИ-92')}
d1 = {'АИ-92': (3, 4, 2, 2), 'АИ-95': (3, 4), 'АИ-80': (1, 3), 'АИ-98': (3, 4)}
list = [['1', '3', 'АИ-80'], ['2', '2', 'АИ-92'], ['3', '4', 'АИ-92', 'АИ-95', 'АИ-98']]
list1 = [['00:01', '10', 'АИ-80'], ['00:04', '45', 'АИ-95'], ['00:12', '40', 'АИ-92'], ['00:41', '30', 'АИ-98'],
         ['00:54', '25', 'АИ-98'], ['01:05', '25', 'АИ-92'], ['01:16', '45', 'АИ-92'], ['01:25', '50', 'АИ-98'],
         ['01:26', '15', 'АИ-98'],
         ['01:39', '40', 'АИ-80'], ['01:44', '30', 'АИ-95'], ['01:53', '20', 'АИ-92']]

kol_avtom = len(d) + 1
avtomat = 0
oz_na_1 = 0  # очередь на 1 колонку
oz_na_2 = 0  # очередь на 2 колонку
oz_na_3 = 0  # очередь на 3 колонку
oz = 0

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

                avtomat = d1['АИ-80'][0]
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
                oz = oz_na_1
            elif oz_na_1 > d1['АИ-80'][1]:
                oz_na_1 -= 1
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
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
            elif oz_na_2 > d1['АИ-92'][3] and oz_na_2 <= d1['АИ-92'][1]:
                avtomat = d1['АИ-92'][0]
                oz = oz_na_2
                print('В {} новый клиент: {} {} {} {} встал в очередь к автомату № {}'.format(time_go, time_go, toplivo,
                                                                                              kol_litr, time_zapr,
                                                                                              avtomat), file=file_out)
            elif oz_na_2 > d1['АИ-92'][1]:
                oz_na_2 -= 1
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
            elif oz_na_3 > d1['АИ-95'][1]:
                oz_na_3 -= 1
                print('В  {}  новый клиент: {} {} {} {} не смог заправить автомобиль и покинул АЗС.'.format(time_go,
                                                                                                            time_go,
                                                                                                            toplivo,
                                                                                                            kol_litr,
                                                                                                            time_zapr),
                      file=file_out)

        for avtomat_0 in list:
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
            number_car = len(list)
