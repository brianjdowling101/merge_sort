import random
import time

def merge_sort(arr):
    #if array length is 1 or less it's already sorted
    if len(arr) > 1:
        # Find the middle index of the array
        mid = len(arr) // 2
        
        # Divide the array into halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively calling merge sort on both halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merging the two sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy remaining elements from left half if any
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy remaining elements from right half if any
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def empirical_analysis():
    # Define input sizes for empirical analysis
    input_sizes = [10, 100, 1000, 10000]  # input sizes
    
    # Perform empirical analysis for each input size
    for size in input_sizes:
        # Generating an array
        arr = [random.randint(0, 1000) for _ in range(size)]
        
        # Measure execution time
        start_time = time.time()
        merge_sort(arr)
        end_time = time.time()
        execution_time = end_time - start_time
        
        # Print results
        print(f"Input size: {size}, Execution time: {execution_time} seconds")

if __name__ == "__main__":
    empirical_analysis()