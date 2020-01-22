import random

arr = [8, 4, 2, 1, 6, 9, 7, 3, 5]

def insertion_sort(arr):
    # Step 1: loop elements except first (considered sorted)
    for i in range(1, len(arr)):
        # Step 2: set up second loop comparing first/second index
        j = i - 1
        # Step 3: write conditional logic RE: the relevant comparison
        while arr[j] > arr[j + 1] and j >= 0:
            # Step 4: specify what happens when first element is bigger than second
            if arr[j] > arr[j + 1]:
                # Step 5: swap the smaller element in front of second and loop again
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Step 6: decrement the loop and repeat until everything is sorted
                j -= 1
                print(arr)
            else: 
                break
    return arr

insertion_sort(arr)

# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # Step 1: loop through n - 1 elements
    for i in range(0, len(arr) - 1):
        # Step 2: assign i as the current index
        cur_index = i
        # Step 3: increment i and start new loop so we can find the smallest number
        for j in range(i + 1, len(arr)):
            # Step 4: conditional logic to compare i and j (don't forget to use square brackets when array is involved) 
            if arr[j] < arr[cur_index]:
                # Step 5: If j is smaller than i, assign it to current index
                cur_index = j
        # Step 6: specify what happens after reassignment
        if i != cur_index:
            # Step 7: restart the loop and begin comparing again with new index
            arr[i], arr[cur_index] = arr[cur_index], arr[i]
            print(arr)
    # Step 8: return the newly sorted array
    return arr

# selection_sort(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Step 1: set up the first for loop
    for i in range(0, len(arr) - 1):
        # Step 2: initialize second loop so we have something to compare (subtract i as it's already included)
        for j in range(0, len(arr) - 1 - i):
            # Step 3: compare first element with its neighbor
            if arr[j] > arr[j + 1]:
                # Step 4: if the second is smaller, swap places
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                print(arr)
    return arr

# bubble_sort(arr)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr