import datetime


# Функция, возвращает все плодородные поля, которые окружают поле, принимает позицию поля
def get_neighbours(x, y):
    result_neighbours = []
    list_neighbours = [
        (y, x + 1),
        (y, x - 1),
        (y + 1, x),
        (y - 1, x),
        (y + 1, x + 1),
        (y + 1, x - 1),
        (y - 1, x - 1),
        (y - 1, x + 1),
    ]
    for element in list_neighbours:
        if data_drop_list.__contains__(element):
            result_neighbours.append(element)
    return result_neighbours


if __name__ == '__main__':

    # вводные данные
    data_const_list = list()  # Список с постоянными данными
    data_drop_list = list()  # Список с переменными данными, которые в итоге мы все выбросим
    results = [0, 0]  # Результат 0-индекс это соотношение плодородной почвы к общей площади, 1-индекс это общая площадь

    # Цикл заполняющий множества, которые определены выше
    for i in range(100):
        for j in range(100):
            data_drop_list.append((i, j))
            data_const_list.append((i, j))

    start = datetime.datetime.now()
    # Находим все регионы
    while data_drop_list:

        # Инициализируем регион
        region = set()
        # Берем начальную точку с этой точки начнем поиск всех ее соседей, потом поиск соседов соседей и т. д. :)
        start_point = data_drop_list[0]
        # Запихиваем ее в множество
        all_neighbours = {start_point}

        # определяем ее положение, что бы в дальнейшем рассчитать площадь полученного региона
        size = [
            start_point[1],  # x_max
            start_point[1],  # x_min
            start_point[0],  # y_max
            start_point[0]  # y_min
        ]

        # начинаем поиск всех крайних соседей
        while all_neighbours:

            temp_field = all_neighbours.pop()

            # x_max
            if temp_field[1] > size[0]:
                size[0] = temp_field[1]

            # x_min
            if temp_field[1] < size[1]:
                size[1] = temp_field[1]

            # y_max
            if temp_field[0] > size[2]:
                size[2] = temp_field[0]

            # y_min
            if temp_field[0] < size[3]:
                size[3] = temp_field[0]

            data_drop_list.remove(temp_field)
            all_neighbours.update(get_neighbours(temp_field[1], temp_field[0]))
            region.add(temp_field)

        # Рассчитываем площадь региона
        x = size[0] - size[1] + 1
        y = size[2] - size[3] + 1
        area_region = x * y

        # Находим внутренних соседей, если они есть
        for i in range(y):
            temp_y = size[3] + i
            for j in range(x):
                temp_x = size[1] + j
                inner_point = (temp_y, temp_x)
                if data_const_list.__contains__(inner_point):
                    region.add(inner_point)

        count_one = len(region)  # Узнаем количество плодородной земли

        # Записываем результат, если он удачный
        if count_one > 1:
            purchase_efficiency = count_one / area_region
            if purchase_efficiency > results[0]:
                results = [purchase_efficiency, area_region]
            elif purchase_efficiency == results[0] and count_one > results[1]:
                results = [purchase_efficiency, area_region]

    # Выводим результат
    print(results[1], ' - ', datetime.datetime.now() - start)
