def select_sort(items: list) -> list:
    for parent_index in range(len(items) - 1):
        min_item_index = parent_index

        for child_index in range(parent_index + 1, len(items)):
            if items[child_index] < items[min_item_index]:
                min_index = child_index

        items[parent_index], items[min_item_index] = items[min_item_index], items[parent_index]

    return items

if __name__ == '__main__':
    nums_5 = [5, 2, 1, 4, 3]
    nums_10 = [10, 8, 5, 2, 1, 7, 4, 3, 9, 6]
    nums_100 = [*range(50, 101), *range(10, 50), *range(1, 10)]

    print(select_sort(nums_5))
    print(select_sort(nums_10))
    print(select_sort(nums_100))
