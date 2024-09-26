def calculate_average(numbers):
    if not numbers:  # Check if the list is empty
        return 0
    return sum(numbers) / len(numbers)

# Sample data
data = [10, 20, 30, 40, 50]
average = calculate_average(data)

print(f"The average of {data} is: {average}")
