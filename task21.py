def count_names(names: list[str]) -> dict[str, int]:
    result = {}
    for name in names:
        if name in result:
            result[name] += 1
        else:
            result[name] = 1
    return result 

names = ["Ali", "Vali", "Ali", "Olim", "Vali", "Ali"]
print(count_names(names))