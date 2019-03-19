def sum_array(array):

    '''Return sum of all items in array'''

    if len(array)==0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

################################

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)

fibonacci(5)

#############################

def factorial(n):

    '''Return n!'''
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

factorial(3)


#################################
def reverse(word):

    '''Return word in reverse'''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]


reverse("sdfgfdgd")

reverse("helloooooo")

###################################

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    out = items.copy()
    for i in range(len(out)):
        for j in range(len(out)-1-i):
            if out[j] > out[j+1]:
                out[j], out[j+1] = out[j+1], out[j]     # Swap!

    return out

#####################################
def merge_sort(items):

    '''Return array of items, sorted in ascending order'''

    len_i = len(items)
    if len_i == 1:
        return items

    mid_point = int(len_i / 2)
    i1 = merge_sort(items[:mid_point])
    i2 = merge_sort(items[mid_point:])

    return i1 +i2

#####################################
def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)
    index=0
    if len_i <= 1:
        # Logic Error
        # identified with test run [1,5,4,3, 2, 6, 5, 4, 3, 8, 6, 5, 3, 1]
        # len <= 1
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large

    ########################################
