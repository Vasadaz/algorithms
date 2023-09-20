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

def search_num_recursive(sort_nums: list[int], hidden_num: int) -> int|None:
    min_limit = 0
    max_limit = len(sort_nums) - 1

    if min_limit > max_limit:
        return None

    middle_limit = max_limit // 2
    num = sort_nums[middle_limit]

    if num == hidden_num:
        return num
    elif num > hidden_num:
        return search_num_recursive(sort_nums[:middle_limit], hidden_num)
    elif num < hidden_num:
        return search_num_recursive(sort_nums[middle_limit + 1:], hidden_num)


def test_searching(function):
    nums_100 = [num for num in range(1, 101)]
    print(function(nums_100, 1))
    print(function(nums_100, 100))
    print(function(nums_100, 101))
    print(function(nums_100, 26))
    print(function(nums_100, 50))
    print(function(nums_100, 49))
    del nums_100


if __name__ == '__main__':
    test_searching(search_num)
    test_searching(search_num_recursive)