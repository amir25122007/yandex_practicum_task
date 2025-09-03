from array import array

def main(string):
    '''Используя метод двух индексов для массива ищем
    наименьшее колво коробок'''
    weights_of_robots: array = array(
        'b', sorted([int(i) 
                     for i in string.split()])
    )
    limit: int = int(input())

    left_index: int = 0
    right_index: int = len(weights_of_robots) - 1
    amount_of_boxes: int = 0

    while left_index < right_index:
        if (weights_of_robots[left_index] + 
            weights_of_robots[right_index]) <= limit:
            amount_of_boxes += 1
            left_index += 1
            right_index -= 1
        else:
            amount_of_boxes += 1
            right_index -= 1
    if right_index == left_index:
        amount_of_boxes += 1
    print(amount_of_boxes)

if __name__ == "__main__":
    main(input())
