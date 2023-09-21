def fast_sort(items:list) -> list:
    if not items:
        return items

    pivot_item = items[0]
    less_items = []
    greater_items = []

    for item in items[1:]:
        if item < pivot_item:
            less_items.append(item)
        else:
            greater_items.append(item)

    return fast_sort(less_items) + [pivot_item] + fast_sort(greater_items)

if __name__ == '__main__':
    nums_5 = [5, 2, 1, 4, 3]
    nums_10 = [10, 8, 5, 2, 1, 7, 4, 3, 9, 6]
    nums_100 = [*range(50, 101), *range(10, 50), *range(1, 10)]

    print(fast_sort(nums_5))
    print(fast_sort(nums_10))
    print(fast_sort(nums_100))
