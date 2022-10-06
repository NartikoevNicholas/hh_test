import random

n_list = [random.randint(0, 10000) for i in range(10000)]
m_list = [random.randint(0, 10000) for i in range(10000)]
s = 200000000

def get_new_list(condition_break, list_price):
    result = []
    summa = 0
    for i in range(len(list_price)):
        summa += list_price[i]
        if condition_break >= summa:
            result.append([summa, i+1])
        else:
            break
    return result


def get_count_resume(last_list, full_list, condition_break):
    result = last_list[1]
    temp_s = condition_break - last_list[0]
    if temp_s == 0:
        return result
    for i in range(len(full_list)):
        if full_list[-i-1][0] <= temp_s:
            return result + full_list[-i-1][1]
    return result


a_list = get_new_list(s, n_list)
b_list = get_new_list(s, m_list)

first_count = 0
if a_list:
    first_count = get_count_resume(a_list[-1], b_list, s)

second_count = 0
if b_list:
    second_count = get_count_resume(b_list[-1], a_list, s)

print(max(first_count, second_count))
