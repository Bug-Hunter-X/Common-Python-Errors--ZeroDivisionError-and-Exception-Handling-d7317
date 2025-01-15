def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Correct usage
my_list = [10, 20, 30]
average = calculate_average(my_list)
print(f"Average: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"Average of empty list: {average_empty}")

def process_data(data):
    try:
        value = int(data.get('value', 0)) # Use get() with default value
    except ValueError as e:
        print(f"Error converting value to integer: {e}")
        return None
    # Further processing of the value
    result = value * 2
    return result

data_input = {'value': '10'}
processed_value = process_data(data_input)
print(f"Processed value: {processed_value}")

data_input_missing = {}
processed_value_missing = process_data(data_input_missing)
print(f"Processed value (missing key): {processed_value_missing}")

data_input_invalid = {'value': 'abc'}
processed_value_invalid = process_data(data_input_invalid)
print(f"Processed value (invalid value): {processed_value_invalid}") 