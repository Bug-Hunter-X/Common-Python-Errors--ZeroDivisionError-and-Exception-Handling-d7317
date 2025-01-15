def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
my_list = []
average = calculate_average(my_list)
print(f"Average: {average}")

#Another example with potential issues
def process_data(data):
    try:
        value = int(data['value'])
    except (KeyError, ValueError) as e:
        print(f"Error processing data: {e}")
        return None
    # Further processing of the value
    result = value * 2
    return result

data_input = {}
processed_value = process_data(data_input)
print(f"Processed value: {processed_value}")