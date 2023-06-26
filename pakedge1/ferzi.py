# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях. 
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга. 
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.



# проверка по вертикалям и горизонталям если есть совпадающие цифры то ферзи бъют друг друга
import random


def gorizont_vertic(polozhenie:dict) -> bool:
    for key , vol in polozhenie.items():
        for key1 , vol1 in polozhenie.items():
            if key == key1 and vol == vol1: continue
            if key == key1: return False
            if vol == vol1: return False
    return True

# проверка по диагоналям х+1,у+1;x-1,y+1;x-1,y-1;x+1,y-1
                            #####################################    
                            #                                   # При достижении границ х=0 or y=0 or x=8 or y=8
                            # F(x-1,y-1)              F(x+1,y-1)# работа поисковика сбрасывается
                            #             F(x,y)                # 
                            # F(x-1,y+1)              F(x+1,y+1)#
                            #####################################
            #     1 2 3 4 5 6 7 8
            # 1   #   #   #   #
            # 2     #   #   #   #
            # 3   #   #   #   #
            # 4     #   #   #   #
            # 5   #   #   #   #
            # 6     #   #   #   #
            # 7   #   #   #   #
            # 8     #   #   #   #
def good_diagonal(polozhenie: dict):
    if polozhenie == None or len(polozhenie) <= 1 : return None
    x = list(x for x in polozhenie.keys())
    y = list(y for y in polozhenie.values())
    for i in range(len(polozhenie)):
        for j in range(i + 1 , len(polozhenie)):
            if abs(x[i] - x[j]) == abs(y[i] - y[j]):
                return False                       
    return True        

def good_polozhenie_ferzei(polozhenie:dict) -> bool:
    if not gorizont_vertic(polozhenie): return False
    if not good_diagonal(polozhenie): return False
    return True






# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
def generator_of_polozhenie_ferzei(n:int=8): # n -  кол-во клеток на поле
    if n == None or n <= 0: n = 8
    list_x = []
    list_y = []
    end = False
    while not end:
        x = random.randint(1,n)
        y = random.randint(1,n)
        if x not in list_x: list_x.append(x)
        if y not in list_y: list_y.append(y)
        if len(list_x) == len(list_y) == n: end = True
    dict_of_polozhenie = {}
    for i in range(n):
        dict_of_polozhenie[list_x[i]] = list_y[i]
    return dict_of_polozhenie      

def get_list_of_good_polozhenie_ferzei(n:int=4):# n- колличество успешных положений, поумолчанию 4
    count = 1
    list_of_good_polozhenie_ferzei = []
    while count < n:
        list_of_new_polozhenie = generator_of_polozhenie_ferzei()
        if good_polozhenie_ferzei(list_of_new_polozhenie):
            if list_of_new_polozhenie not in list_of_good_polozhenie_ferzei:
                list_of_good_polozhenie_ferzei.append(list_of_new_polozhenie)
                count += 1
    return list_of_good_polozhenie_ferzei
# DEBUG
if __name__ == '__main__':
    bed_polozenie =   {8:3,7:8,1:1,3:5,5:7,2:4,4:2,9:1}
    good_polozhenie = {1:1,7:2,5:3,8:4,2:5,4:6,6:7,3:8}
    print('словарь с плохим положением ферзей')
    print(bed_polozenie)
    print(good_polozhenie_ferzei(bed_polozenie))
    print('словарь с хорошим положением ферзей')
    print(good_polozhenie)
    print(good_polozhenie_ferzei(good_polozhenie))
    print('Генератор случайных положений ферзей')
    print(generator_of_polozhenie_ferzei())
    print('генератор списка словарей хороших положений ферзей')
    print(get_list_of_good_polozhenie_ferzei())