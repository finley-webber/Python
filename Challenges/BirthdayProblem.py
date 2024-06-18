import random

def setup():
    numOfP = 0
    birthday = 0
    while True:
        numOfP = int(input("Enter the number of people you want to compare your birthday: "))
        birthday = str(input("Enter your birthday (DD:MM): "))
        if len(birthday) != 5 or birthday[2] != ":":
            print("Error: Enter a valid birthday")
        else:
            return([numOfP, birthday])

def factorial(nop):
    num = 1
    for x in range(1, nop+1):
        num = num * x
    return num

def indice(num, index):
    ret = 1
    for _ in range(1, index + 1):
        ret = ret * num
    return ret

def genAge_day(month):
    day_range = 1
    match month:
        case 2:
            day_range = 28
        case 4 | 6 | 8 | 11:
            day_range = 30
        case _:
            day_range = 31

    return random.randint(1, day_range)

def genAge():
    month = random.randint(1, 12)
    day = genAge_day(month)
    if (day < 10):
        day = "0" + str(day)
    if (month < 10):
        month = "0" + str(month)
    return  str(day) + ":" + str(month)

class Person():
    age = ""
    def __init__(self):
        self.age = genAge()

def checkForBirthday(birthday, birthdayList):
    for x in birthdayList:
        if x == birthday:
            return True
    return False

def calc():
    jesus = setup()
    listOfPeople = []
    for _ in range(jesus[0]): listOfPeople.append(Person().age)
    print("Another person has your birthday!") if checkForBirthday(jesus[1], listOfPeople) else print("You have a unique birthday!")
    return((1 - (factorial(365) / factorial(365 - jesus[0]))   /   indice(365, jesus[0])) * 100)

print(str(calc()) + "% chance")

