
def printNames(names):
    for name in names:
        print(name)


def multiplyBy2(numbers):
    newNumbers = []
    for number in numbers:
        newNumbers.append(number * 2)
    return newNumbers


def multiplyBy2Comprehension(numbers):
    return [number * 2 for number in numbers]


def printEven(numbers):
    for number in range(len(numbers)):
        if numbers[number] % 2 == 0:
            print(numbers[number])


def printEvenIndexes(numbers):
    for index in range(0, len(numbers), 2):
        print(numbers[index])


cpNames = ['Johnny', 'V', 'Jackie [*]', 'Judy', 'Panam']
someNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
printNames(cpNames)
print(multiplyBy2(someNumbers))
print(multiplyBy2Comprehension(someNumbers))
print('printEven')
printEven(someNumbers)
print('printEvenIndexes')
printEvenIndexes(someNumbers)
