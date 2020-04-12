import math

list = []
list1 = []
d = {}
with open('azs.txt') as azs_file:
    for line in azs_file.readlines():
        list.append(line.split())
print(list)
number_kolonok = len(list)

for i in range(number_kolonok):
    a = list[i]
    key = a[0]
    val = a[1]
    d[key] = val
    b = a[2:]
    for m in range(len(b)):
        key = b[i]
        val = a[0]
        if (key in d) == False:
            d[key] = val
        ELIF!!!!
        val = ''
    for t in range(len(b)):
        key = int(a[0])
        val += b[t]
    d[key] = val

file_out = open('output.txt', 'w')
file_out.close()

with open('input.txt') as inp_file:
    for line in inp_file.readlines():
        list1.append(line.split())

number_car = len(list)
file_out = open('output.txt', 'a')
for i in range(number_car):
    f = list1[i]
    time = f[0]
    litr = int(f[1])
    time_zapravki = math.ceil(litr / 10)
    marka = f[2]
    print('В ', time, 'новый клиент:', time, ' ', marka, ' ', litr, ' ', time_zapravki,
          ' встал в очередь к автомату №', file=file_out)
    for z in range(number_kolonok):
        ii = str(z)
        print('Автомат №', z, ' максимальная очередь: ', d[ii], ' Марки бензина:', d[z], ' -> ', KOL - BO
        ZVIZDOCHEK)
        number_car = len(list)

        file_out.close()
