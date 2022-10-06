n, m = map(lambda x: int(x), input().split(' '))

arr_data = []
list_solution = []
for i in range(m):
    arr_data.append(input().split(' '))


def get_true_neighbours(row_index, column_index, max_row, max_column):
    result = []
    if row_index - 1 >= 0:
        result.append([row_index - 1, column_index])  # верхний сосед
        if column_index + 1 <= max_column:
            result.append([row_index - 1, column_index + 1])  # правый верхний сосед
        if column_index - 1 >= 0:
            result.append([row_index - 1, column_index - 1])  # левый верхний сосед
    if row_index + 1 <= max_row:
        result.append([row_index + 1, column_index])  # нижний сосед
        if column_index + 1 <= max_column:
            result.append([row_index + 1, column_index + 1])  # правый нижний сосед
        if column_index - 1 >= 0:
            result.append([row_index + 1, column_index - 1])  # левый нижний сосед
    if column_index - 1 >= 0:
        result.append([row_index, column_index - 1])  # левый сосед
    if column_index + 1 <= max_column:
        result.append([row_index, column_index + 1])  # правый сосед
    return result


def get_new_point(old_point, new_point):
    for i in new_point:
        if old_point.__contains__(i):
            for j in new_point:
                if old_point.__contains__(j) is False:
                    old_point.append(j)
    return old_point


for i in range(m):
    for j in range(n):
        if int(arr_data[i][j]):
            list_solution.append(get_true_neighbours(i, j, m-1, n-1))

for i in range(len(list_solution)):
    for j in range(len(list_solution)):
        if i != j:
            list_solution[i] = get_new_point(list_solution[i], list_solution[j])
            pass
