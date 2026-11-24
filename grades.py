def clean_grades(values):
    return [x for x in values if isinstance(x, (int, float)) and 0 <= x <= 20]

def average(values):
    if len(values) == 0:
        return None

    return sum(values) / len(values)

def mention(avg):
    if avg is None:
        return "Aucune note"
    elif avg < 10:
        return "Insuffisant"
    elif avg < 14:
        return "Moyen"
    else:
        return "Bien"