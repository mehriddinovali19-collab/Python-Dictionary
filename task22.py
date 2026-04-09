def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}
    for student in students:
        group_name = student["group"]
        student_name = student["name"]
        if group_name in group:
            group[group_name].append(student_name)
        else:
            group[group_name] = [student_name]
    return group
data = [
    {"name": "Ali", "group": "A"},
    {"name": "Soli", "group": "A"},
    {"name": "Vali", "group": "B"},
    {"name": "Karim", "group": "B"},
]

print(group_students(data))