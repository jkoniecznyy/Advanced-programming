def sayHi(name: str, surname: str) -> str:
    return f'Czesc {name} {surname}!'


def multiply(nr1: int, nr2: int) -> int:
    return nr1 * nr2


def evenCheck(number: int) -> bool:
    return number % 2 == 0


def task4(nr1: int, nr2: int, nr3: int) -> bool:
    return nr1 + nr2 >= nr3


def findInList(numbers: list, number: int) -> bool:
    return number in numbers


def mergeLists(list1: list, list2: list) -> list:
    result = set()

    for l1 in list1:
        result.add(l1)

    for l2 in list2:
        result.add(l2)

    result = list(result)
    for i, r in enumerate(result):
        if type(r) is int or type(r) is float or type(r) is complex:
            result[i] = r ** 3

    return result


print("Task1")
result = sayHi('Johnny', 'Silverhand')
print(result)

print("Task2")
print(multiply(6, 8))

print("Task3")
result = evenCheck(55)
print("Liczba parzysta" if result else "Liczba nieparzysta")
result = evenCheck(60)
print("Liczba parzysta" if result else "Liczba nieparzysta")

print("Task4")
print(task4(1, 2, 8))
print(task4(1, 2, 1))

print("Task5")
fil = findInList([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print('The number was in the list' if fil
      else 'The number was not in the list')
fil = findInList([1, 2, 3, 4, 5, 6, 7, 8, 9], 30)
print('The number was in the list' if fil
      else 'The number was not in the list')

print("Task6")
print(mergeLists([1, 2, 3, 4, 8, 'try', b'me'],
                 [2, 3, 4, 5, 6, 7, 8, 9.9, 100, 6.7, 2j]))
