# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999]. 
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь. 
# Проверку года на високосность вынести в отдельную защищённую функцию.



#    если номер года не делится на четыре, это обычный год;
#   в противном случае, если номер года не делится на 100, это високосный год;
#   в противном случае, если номер года не делится на 400, это обычный год;
#   в противном случае это високосный год.

#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import sys
def visocosnost(year:int)-> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0: return True
    else: return False

def date_is_fine(date:str) -> bool:
    try:
        day , month , year = map(int , (date.lower().split('.')))
    except Exception:
        return None
    if 0 < day < 32 and 0 < month < 13 and 0 < year < 10000:
        if month in [4 , 6 , 9 , 11] and day < 31: 
            return True
        elif month == 2: 
            if visocosnost(year):
                if day <= 29:
                    return True
            else: 
                if day <= 28 : 
                    return True
                else:
                    return False
        else:
            return False
                       
    return False 
if __name__ =='__main__':
    arguments = [el for el in sys.argv][1:]
    try:
        print(date_is_fine(arguments[0]))
    except Exception:
        print('Введенные данные командной строки неверны')
        print('Введите данные в формате date_is_fine.py дд.мм.уууу')
        
    