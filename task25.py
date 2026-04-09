def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}
    for person in people:
        age = person["age"]
        name = person["name"]
        if age not in result:
            result[age] = [name]
        else:
            result[age] = result[age] + [name]
    return result
            
data = [
    {"name": "Ali", "age": 25},
    {"name": "Vali", "age": 30},
    {"name": "Soli", "age": 25},
    {"name": "Olim", "age": 39},

]
print(group_by_age(data))