def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return (iterations, arr[mid])  # Якщо знайшли точний елемент
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # Пошук верхньої межі
    if left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)

# Тестуємо функцію:
arr = [0.1, 0.5, 1.3, 2.7, 3.8, 5.2]
target = 2.7
result = binary_search(arr, target)

print(f"Ітерацій: {result[0]}, Верхня межа: {result[1]}")
