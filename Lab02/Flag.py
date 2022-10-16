import os
import time
import csv

def esc(code):
    return f'\u001b[{code}m'


GREEN = esc(42)
END = esc(0)
YELLOW = esc(43)
RED = esc(41)
WHITE = esc(47)
count_less_150 = 0
count_more_150 = 0
N = int(input("How many times to repeat the drawing?"))


def Flag():  #This function makes flah
    for i in range(3):
        print(WHITE + ' ' * 30 + END)
    for i in range(3):
        print(RED + ' ' * 30 + END)
    return ''


def Pattern(N):   
    print(('0' * 100) * N)    
    print(('0' * 100) * N)
    print(('1' * 100) * N)
    print(('1' * 100) * N)
    print(('0' * 40) * N + ('1' * 20) * N  +('0' * 40) * N )
    print(('0' * 40) * N + ('1' * 20) * N  +('0' * 40) * N )
    print(('0' * 40) * N + ('1' * 20) * N  +('0' * 40) * N )
    print(('0' * 40) * N + ('1' * 20) * N  +('0' * 40) * N )
    print(('0' * 40) * N + ('1' * 20) * N  +('0' * 40) * N )
    print(('1' * 100) * N)
    print(('1' * 100) * N)

    print(('0' * 10) * N + ('1' * 20) * N  +('0' * 40) * N +('1' * 20) * N + ('0' * 10) )
    print(('0' * 10) * N + ('1' * 20) * N  +('0' * 40) * N +('1' * 20) * N + ('0' * 10) )
    print(('0' * 10) * N + ('1' * 20) * N  +('0' * 40) * N +('1' * 20) * N + ('0' * 10) )
    print(('0' * 10) * N + ('1' * 20) * N  +('0' * 40) * N +('1' * 20) * N + ('0' * 10) )
    print(('0' * 10) * N + ('1' * 20) * N  +('0' * 40) * N +('1' * 20) * N + ('0' * 10) )
    print(('1' * 100) * N)
    print(('1' * 100) * N)
    print(('0' * 100) * N)
    print(('0' * 100) * N)



def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j]) + ' '
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + ' ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)

 

array_plot = [[0 for col in range(10)] for row in range(10)]  

result = [0 for i in range(10)]   

for i in range(10):   
    result[i] = i * 1 / 3

step = round(abs((result[9] - result[0])) / 9, 1)   


with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    books = csv.reader(csvfile, delimiter=';')

    big = 0
    small = 0
    z = -1
    for row in list(books)[1:]:
        year = row[6][:4]

        if int(year) <= 2017:
            small += 1
        else:
            big += 1

all = big + small

a = small * 100 // all
b = big * 100 // all + 1






time.sleep(1)
os.system("cls")

print("Flag of Poland")
print(Flag())

time.sleep(1)

print("\n" * 2 + "Drawing")
Pattern(N)


array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)


print("Until 2017    " + RED + '  ' * a + END + ' ' + str(a) + '%')
print()
print("After 2017  " + RED + '  ' * b + END + ' ' + str(b) + '%')
print()