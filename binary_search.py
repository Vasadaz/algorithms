def search_num(sort_nums: list[int], hidden_num: int) -> tuple[int | None, int]:
    min_limit = 0
    max_limit = len(sort_nums) - 1
    steps_count = 0

    while min_limit <= max_limit:
        steps_count += 1
        middle = (min_limit + max_limit) // 2
        num = sort_nums[middle]

        if num == hidden_num:
            return num, steps_count
        elif num > hidden_num:
            max_limit = middle - 1
        else:
            min_limit = middle + 1

    return None, steps_count


if __name__ == '__main__':
    nums_100 = [num for num in range(1, 101)]
    print(search_num(nums_100, 1))  # (1, 6)
    print(search_num(nums_100, 100))  # (100, 7)
    print(search_num(nums_100, 101))  # (None, 7)
    print(search_num(nums_100, 26))  # (26, 6)
    del nums_100

    nums_10000 = [num for num in range(1, 10001)]
    print(search_num(nums_10000, 1))  # (1, 13)
    print(search_num(nums_10000, 10000))  # (10000, 14)
    print(search_num(nums_10000, 10001))  # (None, 14)
    print(search_num(nums_10000, 26))  # (26, 12)
    del nums_10000

    nums_100000000 = [num for num in range(1, 100000001)]
    print(search_num(nums_100000000, 1))  # (1, 26)
    print(search_num(nums_100000000, 100000000))  # (100000000, 27)
    print(search_num(nums_100000000, 100000001))  # (None, 27)
    print(search_num(nums_100000000, 26))  # (26, 25)
    del nums_100000000
