def sayHi(name: str, surname: str) -> str:
    return f'Czesc {name} {surname}!'


def multiply(nr1: int, nr2: int) -> int:
    return nr1 * nr2


def evenCheck(number: int) -> bool:
    if number % 2 == 0:
        return True
    return False


def task4(nr1: int, nr2: int, nr3: int) -> bool:
    if nr1 + nr2 >= nr3:
        return True
    return False


def findInList(numbers: list, number: int) -> None:
    flag = False
    for n in numbers:
        if n == number:
            flag = True
            break
    if flag:
        print('The number was in the list')
    else:
        print('The number was not in the list')


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

    print(result)
    return result


result = sayHi('Johnny', 'Silverhand')
print(result)

print(multiply(6, 8))

result = evenCheck(6)
if result:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

print(task4(1, 2, 8))

findInList([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)

mergeLists([1, 2, 3, 4, 8, 'try', b'me'], [2, 3, 4, 5, 6, 7, 8, 6.7, 2j])
