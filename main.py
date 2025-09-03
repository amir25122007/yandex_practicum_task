from array import array

def main() -> None:
    weights_of_robots: array = array(
        'b', sorted(list(map(int, input().split())))
    )
    limit: int = int(input())
    # используем метод двух индексов
    left_index: int = 0
    right_index: int = len(weights_of_robots) - 1
    c: int = 0

    while left_index < right_index:
        if (weights_of_robots[left_index] + weights_of_robots[right_index]) <= limit:
            c += 1
            left_index += 1
            right_index -= 1
        elif weights_of_robots[left_index] >= limit:
            c += (right_index - left_index + 1)
            break
        elif weights_of_robots[right_index] >= limit:
            c += 1
            right_index -= 1
        elif (weights_of_robots[left_index] + weights_of_robots[right_index]) > limit:
            c += 1
            right_index -= 1
    if right_index == left_index:
        c += 1
    print(c)

if __name__ == "__main__":
	main()
