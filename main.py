def min_amount_of_boxes(weights_of_robots, limit):
    """Алгоритм для мин колва коробок"""

    '''Используя метод двух индексов для массива ищем
    наименьшее колво коробок: принимает список с весами роботов
    и лимит веса в одной коробке, возвращает колво коробок'''

    left_index: int = 0
    right_index: int = len(weights_of_robots) - 1
    amount_of_boxes: int = 0

    while left_index <= right_index:
        if (weights_of_robots[left_index] +
            weights_of_robots[right_index]) <= limit:
            amount_of_boxes += 1
            left_index += 1
            right_index -= 1
            continue

        amount_of_boxes += 1
        right_index -= 1

    return amount_of_boxes

if __name__ == "__main__":
    weights_of_robots: list = sorted([int(i)
                                      for i in input().split()])
    limit: int = int(input())
    print(min_amount_of_boxes(weights_of_robots, limit))
