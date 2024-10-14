def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            upper_bound = arr[mid]
            high = mid - 1
        else:
            return (iterations, arr[mid])

    return (iterations, upper_bound)


# Тестуємо функцію
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7]
target = 5.0
result = binary_search(arr, target)
print(f"Кількість ітерацій: {result[0]}, Верхня межа: {result[1]}")
