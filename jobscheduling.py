input_list = [190,90,80,60,50,40,30,20,10]  # Including repeated numbers
print("Slots:", input_list)



def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def remove_duplicates(sorted_arr):
    unique_arr = []
    for num in sorted_arr:
        if num not in unique_arr:
            unique_arr.append(num)
    return unique_arr

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


bubble_sort(input_list)
sorted_list = remove_duplicates(input_list)

print("Sorted list without duplicates:", sorted_list)

total_sum = sum_list(sorted_list)
print("Sum of numbers:", total_sum)