scores = {"math": 90, "english": 85, "science": 92}


def total_score(scores_dict):
    total = 0
    for score in scores_dict.values():
        total += score
    return total 

print(total_score(scores))