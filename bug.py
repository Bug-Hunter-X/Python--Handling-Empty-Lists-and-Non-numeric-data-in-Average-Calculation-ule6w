def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = [1, 2, 3, 4, 5]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}") #This will return 0 which is a common behavior

my_list_with_zero = [1,0,3,4,5]
average_zero = calculate_average(my_list_with_zero)
print(f"The average of list with zero is: {average_zero}") #this will return correct average

my_list_with_strings = [1,2,'a',4,5]
average_string = calculate_average(my_list_with_strings) # this will raise TypeError
print(f"The average of list with string is: {average_string}")