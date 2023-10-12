'''
0 пн  7  пн
1 вт  8  вт
2 ср  9  ср
3 чт  10 чт
4 пт  11 пт
5 сб  12 сб
6 вс  13 вс
'''

from datetime import date, timedelta

def NextWD(data, sDW):
    days = []
    tDW = data.weekday()
    for i in range(0, len(sDW)):
        if tDW <= sDW[i]:
            day = data + timedelta(sDW[i] - tDW)
            days += [day]
    return days #datetime.date(2023, 10, 7)

def HorLW(data):
    numW = (data.isocalendar()[1])
    return numW % 2 != 0

hiWeek = {'ist_lekc': [0,  7], 'org_lekc': [0,  7], 'angl':[0,  7], 'matan_lekc': [1,  8], \
          'diskr_lekc':[1,  8], 'matan':[1,  8, 9], 'prog.sh':[1, 4,  8, 11], \
          'prog.fl':[1, 3,  8, 10], 'lita_lekc':[2,  9], 'lita': [2 ], \
          'aig': [3,  9, 10], 'aig_lekc':[3, 10], 'diskr': [ 11], \
          'prog_lekc': [4,  11], 'org': [5,  12], 'ist': [5,  12] }           
          
loWeek = {'ist_lekc': [0,  7], 'org_lekc': [0,  7], 'angl':[0,  7], 'matan_lekc': [1,  8], \
          'diskr_lekc':[1,  8], 'matan':[1, 2,  8], 'prog.sh':[1, 4,  8, 11], \
          'prog.fl':[1, 3,  8, 10], 'lita_lekc':[2,  9], 'lita': [ 9], \
          'aig': [2, 3,  10], 'aig_lekc':[3, 10], 'diskr': [4 ], \
          'prog_lekc': [4,  11], 'org': [5,  12], 'ist': [5,  12] }

def immediateDate(data, curWeek, predmet):
    dates = []
    
    if predmet not in hiWeek:
        print('не правильное название')
        return dates
    if curWeek not in [1, 0]:
        print('неделя может быть только верхней - 1 или нижней - 0')
        return dates
    if not isinstance(data, type(date.today())):
        print('не тот формат даты')
        return dates

    if curWeek:
        sDW = hiWeek.get(predmet)
        dates += NextWD(data, sDW)    
    else:
        sDW = loWeek.get(predmet)
        dates += NextWD(data, sDW)
    
    if len(dates) == 0:
        try:
            data7 = data + timedelta(7)
            dates += immediateDate(data7, not(curWeek), predmet)
        except:
            print('нет таких дат')
            return dates 
    return dates