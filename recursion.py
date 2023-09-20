def sum_nums(nums:list[int|float]) -> int|float:
    if not nums:
        return 0
    return nums.pop(-1) + sum_nums(nums)


if __name__ == '__main__':
    print(sum_nums([5, 10, 20, 10]))
