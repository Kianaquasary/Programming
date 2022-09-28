import csv
import random
import sys

def LineReader():
  with open('books-en.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    enteries_count = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            enteries_count += 7

        line_count += 1
        enteries_count += 7
    print(f'Processed {line_count} lines.')
    print(f'Processed {enteries_count} enteries.')


def BookReader():
  with open('books-en.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    numberOfBooks = 0

    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1


        counter = 0
        for c in row["Book-Title"] :  
            counter+=1  
        if counter > 30 :
              numberOfBooks +=1
        
    print(f'number of records that have a string longer than 30 characters is {numberOfBooks} books.')



def BookPrice():
  with open('books-en.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    booksUpToo = 0
    price = 0
    
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
            booksPrice = 0

        #if(int(row["Price"])).is_integer():
        if row["Price"].isnumeric():
            booksPrice = row["Price"]
            if int(booksPrice) >200:
                booksUpToo +=1

    print(f'number of records more than 200 rubels are {booksUpToo} books.')


def Random(n):
    
    with open("books-en.csv", "r") as student_csv_file:
        csv_reader = csv.reader(student_csv_file)
        next(csv_reader)
        return(random.choice([line[n] for line in csv_reader]) )




LineReader()
BookReader()
BookPrice()

with open('readme.txt', 'w',encoding="utf-8") as f:

    for x in range(0, 20):
        
        a = Random(1)
        b = Random(2)
        c = Random(3)
        автор = "<автор>: "
        название =" - <название>: "
        год = " - <год>: "

        lines = [str(автор),str(Random(1)),str(название), str(Random(2)),str(год) , str(Random(3))]
        print(lines)
        f.writelines(lines)
        f.write('\n')