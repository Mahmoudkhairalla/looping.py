def find_largest_smallest(numbers):
    if not numbers:
        return None, None

    largest = smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest

# Example list
numbers = [10, 20, 5, 40, 30, 72, 34]

largest, smallest = find_largest_smallest(numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
