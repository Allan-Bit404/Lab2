def displya_main_menu():
    print("display_main_menu")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")

    float_list = []
    for item in string_list:
        float_list.append(float(item))

    return float_list

def calculate_average_temperature(float_list):
    total = sum(float_list)
    average = total / len(float_list)
    return average

def calc_min_max_temperature(float_list):
    minimum = min(float_list)
    maximum = max(float_list)
    return [minimum, maximum]

def calc_median_temperature(float_list):
    sorted_list = sorted(float_list)
    n = len(sorted_list)

    # if odd number of elements
    if n % 2 == 1:
        return sorted_list[n // 2]

    # if even number of elements
    mid1 = sorted_list[n // 2 - 1]
    mid2 = sorted_list[n // 2]
    return (mid1 + mid2) / 2

def calc_average():
    print("calc_average")