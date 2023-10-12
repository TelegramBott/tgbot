from datetime import date, timedelta
from timeFromName import HorLW
import calendar

highweek = {'Monday': ['История (лекция-120) (8:00-9:35)\n',
                       'ОРГ (лекция-120) (9:50-11:25)\n',
'Ин. яз. факультатив (11:55-13:30)\n', 'Ин. яз. факультатив (13:45-14:30)'],\
            'Tuesday': ['Мат. анализ (лекция-212) (9:50-11:25)\n',\
                        'МЛиДМ (лекция-212) (11:55-13:30)\n',\
                        'Мат. анализ (пратика-310) (13:45-15:20)\n',\
                        'ОАиП Е.В. Ширяева (практика-117) | \
ОАиП А.М. Филимонова (практика-102)(15:50-17:25)'],\
            'Wednesday': ['ЛиТА (лекция-120) (8:00-9:35)\n',\
                          'ЛиТА (семинар-304) (9:50-11:25)'],\
                          'Thursday': ['ОАиП А.М. Филимонова (практика-117) (9:50-11:25)\n',\
                                       'АлГем (лекция-211) (11:55-13:30)\n',\
                                       'АлГем (практика-206) (13:45-15:20)'],\
                          'Friday': ['ОАиП (лекция-211) (8:50-9:35)\n',\
                                     'ОАиП (лекция-211) (9:50-11:25)\n',\
                                     'ОАиП Е.В. Ширяева (практика-117) (13:45-15:20)'],\
                          'Saturday': ['ОРГ (семинар-325) (8:00-9:35)\n',\
                                       'История (семинар-306) (9:50-11:25)'] }


lowweek = {'Monday': ['История (лекция-120) (8:00-9:35)\n',
                       'ОРГ (лекция-120) (9:50-11:25)\n',
'Ин. яз. факультатив (11:55-13:30)\n', 'Ин. яз. факультатив (13:45-14:30)'],\
            'Tuesday': ['Мат. анализ (лекция-212) (9:50-11:25)\n',\
                        'МЛиДМ (лекция-212) (11:55-13:30)\n',\
                        'Мат. анализ (пратика-310) (13:45-15:20)\n',\
                        'ОАиП Е.В. Ширяева (практика-117) | \
ОАиП А.М. Филимонова (практика-102)(15:50-17:25)'],\
            'Wednesday': ['ЛиТА (лекция-120) (8:00-9:35)\n',\
                          'Мат. анализ (практика-304) (9:50-11:25)\n',\
                          'АлГем (практика-304) (11:55-13:30)'],\
           'Thursday': ['ОАиП А.М. Филимонова (практика-117) (9:50-11:25)\n',\
                                       'АлГем (лекция-211) (11:55-13:30)\n',\
                                       'АлГем (практика-206) (13:45-15:20)'],\
                          'Friday': ['ОАиП (лекция-211) (8:50-9:35)\n',\
                                     'ОАиП (лекция-211) (9:50-11:25)\n',\
                                     'МЛиДМ (практика-305) (11:55-13:30)\n',\
                                     'ОАиП Е.В. Ширяева (практика-117) (13:45-15:20)'],\
                          'Saturday': ['ОРГ (семинар-325) (8:00-9:35)\n',\
                                       'История (семинар-306) (9:50-11:25)'] }

def schedule(DoW, HorL):
    if HorL:
        days_list = highweek.get(DoW)
    else:
        days_list = lowweek.get(DoW)
    subjects_str = ''
    for i in range(len(days_list)):
        subjects_str += days_list[i]
    return subjects_str

def todaySc():
    return schedule(calendar.day_name[(date.today() + timedelta(days=1)).weekday()], HorLW(date.today()))

def tomorSc():
    return schedule((calendar.day_name[(date.today() + timedelta(days=1)).weekday()]), HorLW((date.today()+timedelta(1))))