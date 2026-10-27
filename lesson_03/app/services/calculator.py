def calculate_average(values):
    if not values:
        return 0.0
    return sum(values) / len(values)

def calculate_min(values):
    if not values:
        raise ValueError("Список оценок пуст")
    return min(values)

def calculate_max(values):
    if not values:
        raise ValueError("Список оценок пуст")
    return max(values)
