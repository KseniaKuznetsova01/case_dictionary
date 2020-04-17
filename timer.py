time_zap = 4
time_start = '00:01'
part_1 = time_start[:2]
part_2 = time_start[3:]
time_res = ''
pol = int(time_start[3:]) + time_zap
if pol > 60:
    if int(time_start[:2]) < 23:
        part_1 = str(int(time_start[:2]) + 1)
        part_2 = str((int(time_start[:2]) + pol) - 60)
    elif int(time_start[:2]) == 23:
        part_2 = str(pol - 60)
        part_1 = '00'
    if len(part_2) == 1:
        part_2 = '0' + part_2
    time_res = part_1 + ':' + part_2
else:
    time_res = time_start[:3] + str(pol)
