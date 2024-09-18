def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1

print(linear_search([1, 2, 3, 4, 5], 3))
