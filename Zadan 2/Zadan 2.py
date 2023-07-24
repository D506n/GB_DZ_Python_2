def list_numbers(step):
    temp_list = []
    step = 1
    while len(temp_list) < s:
        temp_list.append(step)
        step += 1
    return temp_list

def find_sums(s, list_sums=[]):
    step_a = 0
    step_b = 0
    result = 0
    array_results = []
    temp_array = []
    while step_a < len(list_sums):
        result = list_sums[step_a] + list_sums[step_b]
        if result == s:
            temp_array = []
            temp_array.append(list_sums[step_a])
            temp_array.append(list_sums[step_b])
            array_results.append(temp_array)
            step_b += 1
        elif step_b == len(list_sums) - 1:
            step_a += 1
            step_b = step_a
        else:
            step_b += 1
    return array_results

def check_mult(num_a, num_b, num_c):
    if num_a * num_b == num_c:
        return True
    else:
        return False

def found_result(p, list_sums=[]):
    strings = 0
    check_result = False
    result = "У этих сумм и произведений, нет общих исходных чисел"
    temp_array = []
    while strings < len(list_sums):
        temp_array = list_sums[strings]
        check_result = check_mult(temp_array[0], temp_array[1], p)
        if check_result == True:
            result = list_sums[strings]
        strings += 1
    return result

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))
list_sums = list_numbers(s)
list_sums = find_sums(s, list_sums)
print(found_result(p, list_sums))