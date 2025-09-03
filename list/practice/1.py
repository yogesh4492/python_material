def reverse_list_recursive(input_list):

    if not input_list:  # Base case: empty list
        return []
    return reverse_list_recursive(input_list[1:]) + [input_list[0]]

# Example usage:
my_list = [1, 2, 3, 4, 5]
reverse_list_recursive(my_list)