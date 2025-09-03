def reverse_list_recursive(input_list):
    def helper(lst, index):
        if index < 0:  # Base case
            return []
        return [lst[index]] + helper(lst, index - 1)

    return helper(input_list, len(input_list) - 1)


# Example usage:
my_list = [1, 2, 3, 4, 5]
print(reverse_list_recursive(my_list))  # [5, 4, 3, 2, 1]

