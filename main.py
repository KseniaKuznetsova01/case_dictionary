"""Case-study #10 Dictionary
Developers:
Kuznetsova K. - 0%
Panukova E. - 0%

"""
import local as lc
import math

list0 = []
list1 = []
d = {}
d1 = {}
zv = ''
kol_avtom = len(d) + 1
nezapravilsa = 0
aivos = 0
aidevvt = 0
aidevvos = 0
aidevpat = 0
avtomat = 0
oz_na_1 = 0
oz_na_2 = 0
oz_na_3 = 0
oz = 0
l = 0

with open('azs.txt') as azs_file:
    for line in azs_file.readlines():
        list0.append(line.split())
number_kolonok = len(list0)

for i in list0:
    d[i[0]] = int(i[1]), i[2]
    for elem in i:
        if elem[:2] == lc.AI:
            d1[elem] = int(i[0]), int(i[1])
a = tuple(list0[1][:2])
d1[lc.AI_92] += int(a[0]), int(a[1])

with open('input.txt', 'r') as inp_file:
    for line in inp_file.readlines():
        list1.append(line.split())

number_car = len(list0)

base_klient = {}
base = []

with open('output.txt', 'w') as file_out:
    for klient in list1:
        time_go = klient[0]
        kol_litr = klient[1]
        time_zapr = math.ceil(int(kol_litr) / 10)
        toplivo = klient[2]
        avt = d1[toplivo]
        time_start = time_go

        part_1 = time_start[:2]
        part_2 = time_start[3:]
        time_res = ''
        pol = int(time_start[3:]) + time_zapr
        if len(str(pol)) == 1:
            pol = '0' + str(pol)
            pol_ = int(pol)
        if pol_ > 60:
            if int(time_start[:2]) == 23:
                part_2 = str(pol - 60)
                part_1 = '00'
            else:
                part_1 = str(int(time_start[:2]) + 1)
                part_2 = str((int(time_start[:2]) + pol) - 60)
            if len(part_2) == 1:
                part_2 = '0' + part_2
            time_res = part_1 + ':' + part_2
        else:
            time_res = time_start[:3] + str(pol)

        if len(avt) == 2:
            avtomat1 = avt[0]

        elif len(avt) == 4:
            avtomat2 = avt[0]
            avtomat3 = avt[2]

        base_klient[time_go] = time_res, toplivo, kol_litr, time_zapr, avtomat
        base.append(base_klient)
        d = base[0]  # база данных о водителях

        for key in d:
            value = d[key]
            a = value[0]

            if (int(a[:2]) <= int(time_go[:2])) or (int(a[:2]) == int(time_go[:2])) and (int(a[3:]) < int(time_go[3:])):
                if int(a[0]) != 0 and len(str(a)) != 1:
                    print(lc.TEXT_3.format(key, a, value[1], value[2], value[3], value[4]), file=file_out)

                    if value[1] == lc.AI_80:
                        oz_na_1 -= 1
                    elif value[1] == lc.AI_92:
                        if oz_na_2 > 0:
                            oz_na_2 -= 1
                        else:
                            oz_na_3 -= 1
                    elif value[1] == lc.AI_95 or value == lc.AI_98:
                        oz_na_3 += 1

                    for avtomat_0 in list0:
                        inform = avtomat_0[0]
                        max_o = avtomat_0[1]
                        mark_benz = avtomat_0[2]
                        if len(avtomat_0) > 3:
                            mark_benz = avtomat_0[2] + ' ' + avtomat_0[3] + ' ' + avtomat_0[4]

                        if inform == lc.N1:
                            zv = oz_na_1 * lc.ZV
                        elif inform == lc.N2:
                            zv = oz_na_2 * lc.ZV
                        elif inform == lc.N3:
                            zv = oz_na_3 * lc.ZV

                        print(lc.TEXT_4.format(inform, max_o, mark_benz, zv), file=file_out)
                    d[key] = '0','', '','',''

        if toplivo == lc.AI_80:
            oz_na_1 += 1

            if oz_na_1 <= d1[lc.AI_80][1]:

                aivos += int(kol_litr)
                avtomat = d1[lc.AI_80][0]
                print(lc.TEXT_1.format(time_go, time_go, toplivo, kol_litr, time_zapr, avtomat), file=file_out)
                oz = oz_na_1

            elif oz_na_1 > d1[lc.AI_80][1]:
                oz_na_1 -= 1
                nezapravilsa += 1
                print(lc.TEXT_2.format(time_go, time_go, toplivo, kol_litr, time_zapr), file=file_out)

        elif toplivo == lc.AI_92:

            oz_na_2 += 1
            if oz_na_2 <= d1[lc.AI_92][3]:
                avtomat = d1[lc.AI_92][2]
                oz = oz_na_2
                aidevvt += int(kol_litr)
                print(lc.TEXT_1.format(time_go, time_go, toplivo, kol_litr, time_zapr, avtomat), file=file_out)

            elif oz_na_2 > d1[lc.AI_92][3] and oz_na_2 <= d1[lc.AI_92][1]:
                avtomat = d1[lc.AI_92][0]
                oz = oz_na_2
                aidevvt += int(kol_litr)
                print(lc.TEXT_1.format(time_go, time_go, toplivo, kol_litr, time_zapr, avtomat), file=file_out)

            elif oz_na_2 > d1[lc.AI_92][1]:
                oz_na_2 -= 1
                nezapravilsa += 1
                print(lc.TEXT_2.format(time_go, time_go, toplivo, kol_litr, time_zapr), file=file_out)

        elif toplivo == lc.AI_95 or toplivo == lc.AI_98:

            oz_na_3 += 1
            if oz_na_3 <= d1[lc.AI_95][1]:
                avtomat = d1[lc.AI_95][0]
                oz = oz_na_3
                print(lc.TEXT_1.format(time_go, time_go, toplivo, kol_l itr, time_zapr, avtomat), file=file_out)

                if toplivo == lc.AI_95:
                    aidevpat += int(kol_litr)
                elif toplivo == lc.AI_95:
                    aidevvos += int(kol_litr)

            elif oz_na_3 > d1[lc.AI_95][1]:
                oz_na_3 -= 1
                nezapravilsa += 1
                print(lc.TEXT_2.format(time_go, time_go, toplivo, kol_litr, time_zapr), file=file_out)

        for avtomat_0 in list0:
            inform = avtomat_0[0]
            max_o = avtomat_0[1]
            mark_benz = avtomat_0[2]
            if len(avtomat_0) > 3:
                mark_benz = avtomat_0[2] + ' ' + avtomat_0[3] + ' ' + avtomat_0[4]

            if inform == lc.N1:
                zv = oz_na_1 * lc.ZV
            elif inform == lc.N2:
                zv = oz_na_2 * lc.ZV
            elif inform == lc.N3:
                zv = oz_na_3 * lc.ZV

            print(lc.TEXT_4.format(inform, max_o, mark_benz, zv), file=file_out)
            number_car = len(list0)


with open('output.txt', 'a+') as file_out:
    print(lc.TEXT_5_80.format(aivos, math.floor(aivos * 38.95)), file=file_out)
    print(lc.TEXT_5_92.format(aidevvt, math.floor(aidevvt * 40.35)), file=file_out)
    print(lc.TEXT_5_95.format(aidevpat, math.floor(aidevpat * 42.55)), file=file_out)
    print(lc.TEXT_5_98.format(aidevvos, math.floor(aidevvos * 49.2)), file=file_out)
    print(lc.TEXT_6.format(nezapravilsa, math.floor(nezapravilsa * 44.8625)), file=file_out)
    print(lc.TEXT_7.format(math.floor(aivos * 38.95 + aidevvt * 40.35 + aidevpat * 42.55 + aidevvos * 49.2)),
          file=file_out)
