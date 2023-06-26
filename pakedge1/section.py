
import sys
import random
def rand_num_and_number_of_check(a1:int,a2:int,a3:int):
    number = random.randint(a1,a2)
    return number * a3

def arguments_list_of_tree() -> list:
    if len(sys.argv) >= 4:
        arguments = list(map(int,[el for el in sys.argv][1:]))
        return arguments
    else: 
        return None
if __name__ == '__main__':
    arguments = arguments_list_of_tree()
    if arguments != None:
        print(rand_num_and_number_of_check(arguments[0],arguments[1],arguments[2]))