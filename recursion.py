def count_items(items:list) -> int:
    if not items:
        return 0

    return 1 + count_items(items[:-1])

def get_max_1(nums:list[int|float]) -> int|float:
    if count_items(nums) == 1:
        return nums[0]

    num_1 = nums[-1]
    num_2 = get_max_1(nums[:-2])

    if num_1 > num_2:
        return num_1

    return num_2

def get_max_2(nums:list[int|float]) -> int|float:
    if count_items(nums) == 2:
        return nums[0] if nums[0] > nums[1] else nums[1]

    num = get_max_2(nums[:-1])

    return nums[-1] if nums[-1] > num else num

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

def sum_nums(nums:list[int|float]) -> int|float:
    if not nums:
        return 0

    return nums[-1] + sum_nums(nums[:-1])


if __name__ == '__main__':
    my_nums = [i for i in range(997)]

    print('Count:', count_items(my_nums))
    print('Max 1:', get_max_1(my_nums))
    print('Max 2:', get_max_2(my_nums))
    print('Search:', search_num_recursive(my_nums, 996))
    print('Sum:', sum_nums(my_nums))
