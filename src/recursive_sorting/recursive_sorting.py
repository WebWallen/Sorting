arr = [8, 4, 2, 1, 6, 9, 7, 3, 5]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # Step 1: set up base case (if array is length of 1, should be returned)
    if len(arr) < 2:
        return arr
    # Step 2: divide the length of array by 2 (// for floor vs decimal)
    middle = len(arr) // 2
    # Step 3: assign the left integers to a separate variable and recursively call function to continue dividing
    left = merge_sort(arr[:middle])
    # Step 4: ditto for the right side integers (: in front = left, : at end = right)
    right = merge_sort(arr[middle:])
    # Step 5: feed the newly divided arrays into the helper function so they can be sorted
    return merge(left, right)
# Note: the above steps classify as DIVIDE and below would be considered CONQUER

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( left, right ):
    # Step 1: set up base case (if there isn't a length, the work is done, so just return)
    if not len(left) or not len(right):
        return left or right
    # Step 2: initialize emptry array so we have somewhere to put the data as it's merged
    merged_arr = []
    # Step 3: create two placeholder indexes or we won't have any data to compare
    i = 0
    j = 0
    # Step 4: specify when work is to be done (while merged arr is smaller than the combined arrays being sorted)
    while len(merged_arr) < len(left) + len(right):
            # Step 5: if left integer is smaller than it's neighbor, place it in front, increment, and repeat
        if left[i] < right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            # Step 6: if left integer is bigger than it's neighbor, it goes behind (increment + repeat) 
            merged_arr.append(right[j])
            j += 1
        # Step 7: specify what happens when we've sorted all the way down to one number
        if i == len(left) or j == len(right):
            # Step 8: place the sorted data inside the new array for this purpose
            merged_arr.extend(left[i:] or right[j:]) # sub_arr[index:]
            # Step 9: terminate the process to prevent continued operations
            break
    # Step 10: return our sorted array
    return merged_arr

print(merge_sort(arr))

# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
