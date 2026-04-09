def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for index in range(len(numbers)):
        number = numbers[index]
        if number in result:
            result[number] = result[number] + [index]
        else:
            result[number] = [index]
    return result

sonlar = [1, 2, 3, 2, 1]
print(group_indices(sonlar))


