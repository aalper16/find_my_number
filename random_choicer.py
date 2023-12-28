import random as rd  

numlist = []
print('numaralar yükleniyor...')
for i in range(9999999):
    first3 = str(rd.randint(500, 600))
    sec3 = str(rd.randint(0, 1000))
    first2 = str(rd.randint(0, 100))
    sec2 = str(rd.randint(0, 100))
    if len(sec3) == 2:
        fsec3 = '0' + sec3
    elif len(sec3) == 1:
        fsec3 = '00' + sec3
    else:
        fsec3 = sec3

    
    num = first3, fsec3, first2, sec2
    numlist.append(num)



for nums in numlist:
    print(nums)