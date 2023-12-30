conditions = {
    range(0, 5): "~4年",
    range(5, 10): "~9年",
    range(10, 15): "~14年",
    range(15, 20): "~19年",
    range(20, 25): "~24年",
    range(25, 30): "~29年",
    range(30, 35): "~34年",
    range(35, 40): "~39年"
}

def apply_condition(value):
    for condition_range, text in conditions.items():
        if value in condition_range:
            return text
    return "40年以上"

dataframe['histogram'] = dataframe['years of service'].apply(apply_condition)
