### python by moshiurr007 --> intermediate_level ###

# quick sort algorithm implementation #

def quick_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    pivot = arr[0]

    less = []
    equal = []
    greater = []

    for num in arr:
        if num < pivot:
            less.append(num)
        elif num > pivot:
            greater.append(num)
        else:
            equal.append(num)
    
    return quick_sort(less) + equal + quick_sort(greater)

print(quick_sort([10, 3, 7, 14, 5, 18, 2, 21]))

# works with strings too and sorts them alphabetically
print(quick_sort(["mango", "guava", "litchi", "grapes", "apple", "tangerine", "jackfruit"]))