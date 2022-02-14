###################################################################################################
print()
print()
###################################################################################################
# Answer 1
print("QUESTION 1")
var = input("Enter something: ")     # input
var = var.lower()

# for string without space
if var.find(" ") < 0:
    letter_list = list(var)          # changed the string in a list of all characters 
    letter_set = set(list(var))      # converted the list into set so that repetition of words could be avoided
                                     
    for item in letter_set:          # loop for occurrences
        print("The occurrences of ", item, "is", letter_list.count(item))

# for string with space
else:
    words_list = var.split(" ")      # split string into words 
    words_set = set(var.split(" "))  # list into set  
    
    for item in words_set:           # loop for occurrences
        print("The occurrences of ", item, "is", words_list.count(item))

print()
print()

###################################################################################################
# Answer 2
print("QUESTION 2")
# input date 
day = int(input("day : "))
month = int(input("month : "))
year = int(input("year : "))


def next_day(day):
    day += 1
    print("next date is :", day, ".", month, ".", year)


def next_month(day, month):
    day = 1
    month += 1
    print("next date is :", day, ".", month, ".", year)


def next_year(day, month , year):
    day = 1
    month = 1
    year += 1
    print("next date is :", day, ".", month, ".", year)


# for date month year out of range
if not(1<=day<=31):
    print("wrong day")
if not(1<=month<=12):
    print("wrong month")
if not(1800<=year<=2025):
    print("wrong year")

# month with 31 days

if (1<=day< 31) and (month in (1, 3, 5, 7, 8, 10, 12)) and (1800<=year<=2025):
    next_day(day)
elif (day == 31) and (month == 12):
    next_year(day, month, year)
elif (day == 31) and (month in (1, 3, 5, 7, 8, 10, 12)):
    next_month(day, month)
    # quit()

# month with 30 days

elif (1<=day< 30) and (month in (4, 6, 9, 11)) and (1800<=year<=2025):
    next_day(day)
elif (day == 30) and (month in (4, 6, 9, 11)):
    next_month(day, month)

# Feb in a leap year (29 days)

elif (1<=day< 29) and (month == 2) and (1800<=year<=2025) and (year % 4 == 0):
    next_day(day)
    # quit()
elif (day == 29) and (month == 2) and (year % 4 == 0):
    next_month(day, month)

# Feb in a non leap year (28 days)

elif (1<=day< 28) and (month == 2) and (1800<=year<=2025):
    next_day(day)
elif (day == 28) and (month == 2):
    next_month(day, month)

# some other invalid dates

if (day == 31) and (month in (4, 6, 9, 11)):
    print("this date does not exist")

if (day in (31, 30)) and (month == 2) and (year % 4 == 0):         # for leap year
    print("this date does not exist")

if (day in (31, 30, 29)) and (month == 2) and (year % 4 != 0):    # for non leap year
    print("this date does not exist")

print()
print()

###################################################################################################
# Answer 3
print("QUESTION 3")
# input elements list 
num = []
list_elements = int(input("How many numbers do you want in the list : "))

for i in range(list_elements):
    k = int(input("Enter number : "))
    num.append(k)

# output elements list 
output = []

for j in num:
    output.append((j, j*j))
print(output)

print()
print()

###################################################################################################
# Answer 4
print("QUESTION 4")
points = int(input("enter your grade :"))

while not(4<=points<=10):
    print("wrong grade this do not exist")
    points = int(input("enter your grade :"))


def grade(points):
    grades = {10:"A+", 9:"A", 8:"B+", 7:"B", 6:"C+", 5:"C", 4:"D", }
    return grades.get(points)


def performance(points):
    remarks = {10:"Outstanding", 9:"Excellent", 8:"Very Good", 7:"Good", 6:"Average", 5:"Below Average", 4:"Poor", }
    return remarks.get(points)


print("Your grade is '", grade(points),"' and ", performance(points), "performance")

print()
print()

###################################################################################################
# Answer 5
print("QUESTION 5")
for rows in range(0, 5+1):
    print(" "*rows, end="")
    for letter in range(0, 11 - 2*rows):
        print(chr(65+letter), end="")
    print()

print()
print()

###################################################################################################
# Answer 6
print("QUESTION 6")

loop_condition = input("do u want to enter the name of student (Y or N) : ")

record = dict()

while True:
    if loop_condition == 'y': 
        SID = int(input("Enter SID : "))
        name = input("Enter name : ")
        record.update(({SID:name}))
        loop_condition = input("do u want to enter the name of student (Y or N) : ")
    elif loop_condition == 'n':
        break
    else:
        print("enter a valid answer")
        loop_condition = input("do u want to enter the name of student (Y or N) : ")

# Part A 
print("a) ", record, end="\n\n")
# Part B 
record_sid = dict()
keys = list(record.keys())
keys.sort()
# print(keys)
for k in keys:
    record_sid.update({k:record.get(k)})
print("b) ", record_sid, end="\n\n")

# Part C
record_name = dict()
value = list(record.values())
value.sort()

# print(value)
for x in value:
    record_name.update({list(record.keys())[list(record.values()).index(x)]:x})

print("c) ", record_name, end="\n\n")

# Part D

sid = int(input("enter sid of the student : "))

if sid in record.keys():
    print("Name of the required student is", record[sid])
else:
    print("The SID is not present in the given Data")

print()
print()

###################################################################################################
# Answer 7
print("QUESTION 7")

fib_num = [0, 1]

while True:
    
    terms = int(input("How many terms u want in fibonacci series : "))  # input
    
    if terms <= 0:                                                     # for invalid terms
        print("Enter a valid number") 
    
    elif terms == 1:                                                    # for 1 term result and quit
        print("The terms in the series are\n", fib_num[0])
        print("The avg of the terms is 0")
        # quit()
    
    elif terms >= 2:                                                    # for other no. of terms we add terms in the list 
        for i in range(0, terms-2):
            fib_num.append(fib_num[i]+fib_num[i+1])
        print("The terms in the series are")

        for j in fib_num:                                               # we print list
            print(j, end=" ")

        avg = sum(fib_num)/len(fib_num)
        print("\nThe avg of the terms is ", avg)                        # avg
        break

print()
print()

###################################################################################################
# Answer 8
print("QUESTION 8")
# Answer 8
set1 = {1, 2, 3, 4, 5}                     # given set
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}

inter_1_2 = set1.intersection(set2)       # intersection sets
inter_2_3 = set2.intersection(set3)
inter_3_1 = set3.intersection(set1)
inter_1_2_3 = set1.intersection(set2, set3)

# Part A 
set_a = set1.symmetric_difference(set2)   
print("a)", set_a)

# Part B
set_b = (set1-set2-set3).union((set2-set1-set3), (set3-set2-set1))
print("b)", set_b)

# Part C
set_c = inter_1_2.union(inter_2_3, inter_3_1) - inter_1_2_3
print("c)", set_c)

# Part D
set_d = set()
for i in range(1, 11):
    if i in set1:
        continue
    set_d.add(i)
print("d)", set_d)

# Part E
set_e = set()
for j in range(1, 11):
    if j in set1.union(set2, set3):
        continue
    set_e.add(j)
print("e)", set_e)


print()
print()
