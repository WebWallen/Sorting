# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # Step 1: loop through n - 1 elements
    for i in range(0, len(arr) - 1):
        # Step 2: assign i as the current index
        cur_index = i
        # Step 3: loop through rest of array after incrementing
        for j in range(i + 1, len(arr)):
            # Step 4: conditional logic to compare i and j (don't forget to use square brackets when array is involved) 
            if arr[j] < arr[cur_index]:
                # Step 5: If j is smaller than i, assign it to current index
                cur_index = j
        # Step 6: Specify what happens after reassignment
        if i != cur_index:
            # Step 7: restart the loop and start comparing again with new index
            arr[i], arr[cur_index] = arr[cur_index], arr[i]
    return arr

arr = [1, 4, 7, 3, 0, 8, 9, 3]
print(selection_sort(arr))


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr