import copy


def get_indices(nums, target):
    sorted_nums = sorted(nums, reverse=True)

    summ = 0
    indices = []
    for elem in sorted_nums:
        if elem > target or summ + elem > target:
            continue

        if summ + elem <= target:
            summ += elem
            indices.append(nums.index(elem))

        if summ == target:
            break

    return sorted(indices)


indices = get_indices([3, 2, 4], 6)
print(indices)  # prints [1, 2]
