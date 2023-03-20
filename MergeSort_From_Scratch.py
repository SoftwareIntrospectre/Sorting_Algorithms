"""
    Take a list as input, sort it recursively

    New challenge: Sort it into descending order instead. How would that work?
"""

# not worth the effort. Too confusing. Scrapping this.
# def merge_sort_choice():
#     """
#         Takes user input, and returns one of two values for Ascending or Descending
#     """
#     result = -1

#     try:
#         user_input = int(input('Please select 1 for Ascending Merge Sort or 2 for Descending Merge Sort.\n'))    

#     except:
#         print("Invalid choice.")
#         return result

#     else:
#         if user_input == 1:
#             result = user_input
#             print(f"You chose {result}. List will be sorted in Ascending order.\n")
#             return result

#         elif user_input == 2:
#             result = user_input
#             print(f"You chose {result}. List will be sorted in Descending order.\n")
#             return result 


def merge_sort_ascending(array):

    #sort_choice = merge_sort_choice()

    # if sort_choice == 1:
    #     is_sorted_ascending = verify_sorted_ascending(array)
    #     if is_sorted_ascending:
    #         return array

    is_sorted_ascending = verify_sorted_ascending(array)

    if is_sorted_ascending:
        return array
    
        
    else:
        left_half, right_half = split_array(array)

        left = merge_sort_ascending(left_half)
        right = merge_sort_ascending(right_half)

        return merge_ascending(left, right)

# YES! I DID IT!!!!
def merge_sort_descending(array):
    is_sorted_descending = verify_sorted_descending(array)

    if is_sorted_descending:
        return array
    
    else:
        left_half, right_half = split_array(array)

        left = merge_sort_descending(left_half)
        right = merge_sort_descending(right_half)

        return merge_descending(left,right)

# success!
def split_array(array):

    midpoint = len(array) // 2

    left_half = array[:midpoint]
    right_half = array[midpoint:]

    return left_half, right_half


def merge_ascending(left,right):
    arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1

        else:
            arr.append(right[j])
            j += 1


    while i < len(left):
        arr.append(left[i])
        i += 1
    
    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr

# same logic, except I append left[i] if left[i] > right[j]. Logic is the same otherwise.
# I figured this out on my own. So proud of this! (Almost gave up too, but perservered a bit longer)
def merge_descending(left,right):
    arr = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr.append(left[i])
            i += 1

        else:
            arr.append(right[j])
            j += 1

    while i < len(left):
        arr.append(left[i])
        i += 1

    while j < len(right):
        arr.append(right[j])
        j += 1

    return arr
        
# success!
def verify_sorted_ascending(array):

    n = len(array)
    
    # returns True if the list has 1 element or 0 elements (already sorted)
    if n == 0  or n == 1:
        return True

    return array[0] < array[1] and verify_sorted_ascending(array[1:])
    
# success!!
def verify_sorted_descending(array): 

    n = len(array)
    
    # returns True if the list has 1 element or 0 elements (already sorted)
    if n == 0  or n == 1:
        return True

    return array[0] > array[1] and verify_sorted_descending(array[:n - 1])
