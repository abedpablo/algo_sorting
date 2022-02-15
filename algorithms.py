import random

"""
selection sort, insertion sort, quick sort, merge sort, heap sort,
radix sort (LSD), radix sort (MSD),
std::sort (intro sort)*,
std::stable_sort (adaptive merge sort)**,
shell sort, bubble sort, cocktail shaker sort, gnome sort, bitonic sort and bogo sort
"""


def selection_sort(my_array):
    """
    The first value is taken and compared to the next until it reaches a value
    that is less than what is currently selected. It will continue until the
    entire list has been sorted. In other words we move each value to the end
    of the list until it is sorted.
    Look for smallest element, move to front
    n = 125
    """
    for i in range(len(my_array)):
        min_idx = i
        for j in range(i + 1, len(my_array)):
            if my_array[min_idx] > my_array[j]:
                min_idx = j

        my_array[i], my_array[min_idx] = my_array[min_idx], my_array[i]
        yield my_array


def insertion_sort(my_array):
    """
    We need to start the iteration at the beginning so we select all elements after
    the first element and make this element the "predecessor". We compare each value
    with the predecessor, if it is less than the predecessor we take note of the
    predecessor index position and compare the current value with the value preceding
    the predecessor until we either reach the end of the list (beginning) or the current
    value is bigger than the predecessor.
    Build an increasingly large sorted front portion
    n = 100
    """
    for idx in range(1, len(my_array)):
        key_elem = my_array[idx]
        predecessor = idx-1
        while predecessor >= 0 and key_elem < my_array[predecessor]:
            my_array[predecessor + 1] = my_array[predecessor]
            predecessor -= 1
        my_array[predecessor + 1] = key_elem
        yield my_array


def partition(arr, low, high):
    """
    part of quick sort
    :param arr: the array
    :param low: starting index of array
    :param high: ending index of array
    :return: return the index pivot value

    Here the last position is chosen as the pivot point. Then each element in the list is compared
    to the pivot value. If it is less than the pivot value it will move to the left. After the
    comparison it will do one last comparison of the last element and the pivot value. It will then
    return the position of where the pivot is so it can continue splitting and comparing for the
    next iteration.

    """
    pivot = arr[high]
    i = low-1
    for x in range(low, high):
        if arr[x] < pivot:
            i += 1
            arr[i], arr[x] = arr[x], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low=0, high=124):
    """
    :param arr: Array
    :param low: starting index
    :param high: ending index

    While the low and high are not the same, it will break each array into two parts choosing the
    pivot value as the last value in the array. All done in place.
    Recursively partition array based on a middle value
    n = 125
    """
    if low < high:
        piv = partition(arr, low, high)
        yield arr
        yield from quick_sort(arr, low, piv-1)
        yield from quick_sort(arr, piv+1, high)


def merge_sort(arr):
    """
    We stop the recursion when the length of the array is 1. We split each array
    in half. We then break until the length of each array is 1. Then we start sorting
    each array we the logic found in merge, bottom up. Meaning if we start with 8 values,
    we break it to 4, then 2, then 1. We compare arrays of 1 and 1 to sort the list.
    Then we compare arrays of 2 and 2 to sort. Then we compare 4 and 4 to sort and finally
    merge.

    Recursively divide the array in half and sort

    In order to make the algorithm work as a generator, each function call must report
    about the state of the whole list. Therefore, slices aren't passed with the each
    recursive call but indices instead, giving access to the same arr to all
    function execution contexts.

     Time complexity of merge sort is  O(nLogn) in all 3 cases (worst, average, and best)
     as merge sort always divides the array into two halves and takes linear time to
     merge two halves.

     n = 128
    """

    def merge(start, end):  # separate function that can take start/end indices
        if end - start > 1:
            middle = (start + end) // 2

            yield from merge(start, middle)  # don't provide slice, but index range
            yield from merge(middle, end)
            left = arr[start:middle]
            right = arr[middle:end]

            i = 0
            j = 0
            k = start

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1

            yield arr

    yield from merge(0, len(arr))


def heapify(arr, n, i):
    maximum = i
    left = 2*i+1
    right = 2*i+2
    if (left < n) and (arr[left] > arr[maximum]):
        maximum = left

    if (right < n) and (arr[right] > arr[maximum]):
        maximum = right

    if maximum != i:
        arr[i], arr[maximum] = arr[maximum], arr[i]
        heapify(arr, n, maximum)


def heap_sort(arr):
    """
    build a binary tree then sort with heap. You have built the max heap, now you need to sort
    The purpose of max heap isn't get it in order or reverse max order but to make sure that
    the root node, or any node, is greater than either of its children

    after building the max heap, the largest item is stored at the root of the heap (position 0)
    and reduces the size of the heap by 1. Then we continue to get the largest value at the root
    until the array is sorted.
    Place the values into a sorted tree structure
    n = 200
    """
    n = len(arr)
    x = n // 2-1
    for i in range(x, -1, -1):
        yield heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        yield heapify(arr, i, 0)
    yield arr


def counting_sort_l(arry, position):  # part of radix
    """
    The counting sort algorithm is used with Radix sort. The sorting is done according to
    the digit represented by the 'position' variable.
    """
    arr_length = len(arry)
    count = [0]*10  # Since base 10 (0-9) we are counting how many of each value is seen in X pass
    output = [0]*arr_length

    # Iterating through each element in the array, we get the digit we want in the ones place
    # then count the number of values with the key digit
    for i in range(0, arr_length):
        index = arry[i] / position
        count[int(index % 10)] += 1

    # Iterate through each element in count array or key array to make a new array that places
    # the last position of that key within the array relative to the original array. So if
    # we see [2, ...] in count, the output is [0, 0, 0, ...] and if there are no "1"s
    # the the count will look like [2,2 ...] and if the next seen value is 2 and only seen once,
    # we will see [2, 2, 3, ...]. We weill see this until we through the 9 key. In other words
    # this count the number of elements that end with the key of interest
    for i in range(1, 10):
        count[i] += count[i-1]

    # First we get the digit of interest in the ones position, the we get the digit itself,
    # make it an int, assign index position, assign value to the position in the output,
    # then decrement the count by 1, then go down in the array by 1 to the next position until
    # we hit the "end" (in this case the beginning or index position = 0).
    i = arr_length - 1
    while i >= 0:
        idx = arry[i] / position
        output[count[int(idx % 10)] - 1] = arry[i]
        count[int(idx % 10)] -= 1
        i -= 1

    for j in range(0, arr_length):
        arry[j] = output[j]
        yield arry

    yield arry


def radix_sort_l(arry):
    """
    Radix sort is an algorithm is to sort by digit to digit from least significant (one's place)
    to the most significant (highest place). The advantage here is to sort elements when they
    are in the range fo 1 to n^2 and a comparison based algorithm would take O(n^2).
    Sort integers by last digit (ones place), then 2nd to last, etc. In other words, sort by the
    end of the string.

    time complexity best and worst case is O(n*m).
    Use n = 200
    """
    maximum_value = max(arry)
    position = 1
    while maximum_value / position > 0:
        yield from counting_sort_l(arry, position)
        position *= 10
    yield arry


def counting_sort_m(arr, low, high, length):
    # Recursive break condition
    if high <= low:
        return

    # Stores the Values
    count = [0]*11
    # temp is created to easily swap digits in arr[]
    temp = dict()

    # Store occurrences of most significant character from each integer in count[]
    for i in range(low, high+1):
        digit_at = int(arr[i] / (10 ** (length - 1))) % 10
        count[digit_at] += 1

    # Change count[] so that count[] now contains actual
    # position of this digits in temp[]
    for r in range(0, 10):
        count[r+1] += count[r]

    # Build the temp
    for j in range(low, high+1):
        digit_at = int(arr[j] / (10 ** (length - 1))) % 10
        digit = count[digit_at]
        temp[digit] = arr[j]
        count[digit_at] -= 1

    # Copy all integers of temp to arr[], so that arr[] now
    # contains partially sorted integer
    counter = 0
    for i in range(low, high+1):
        x = i-low+1
        arr[i] = temp[x]
        # logic so that the unsorted array is visible before sorting
        if counter < 2:
            yield arr
        counter += 1

    # Recursively counting_sort_m() on each partially sorted
    # integers set to sort them by their next digit
    for r in range(0, 10):
        yield from counting_sort_m(arr, low+count[r], low+count[r+1]-1, length-1)
    yield arr


def radix_sort_m(arr):
    """
    Radix sort MSD is an algorithm is to sort by digit to digit from most significant
    to the least significant digit. The advantage here is to sort elements when they
    are in the range fo 1 to n^2 and a comparison based algorithm would take O(n^2).
    The time complexity can be better than LSD, where best case is O(n) and worst is
    O(n*m) where m is equal to the length of the string. LSD best and worst case is
    O(n*m).
    n = 300
    """
    max_value = max(arr)
    max_length = len(str(abs(max_value)))
    yield from counting_sort_m(arr, 0, len(arr)-1, max_length)
    yield arr


# def find_median_intro(arr, one, two, three):
#     x = arr[one]
#     y = arr[two]
#     z = arr[three]
#
#     if x <= y <= z:
#         return two
#     if z <= y <= x:
#         return two
#     if y <= x <= z:
#         return one
#     if z <= x <= y:
#         return one
#     if y <= z <= x:
#         return three
#     if x <= z <= y:
#         return three
#
#
# def introsortUtil(array, begin, end, depthLimit):
#     size = end - begin
#     if size < 16:
#         insertion_sort(array)
#         return array
#     if depthLimit == 0:
#         array = heap_sort(array)
#         return array
#     pivot = find_median_intro(array, begin, begin + size//2, end)
#     (array[pivot], array[end]) = (array[end], array[pivot])
#
#     partitionPoint = partition(array, begin, end)
#
#     array = introsortUtil(array, begin, partitionPoint - 1, depthLimit - 1)
#     array = introsortUtil(array, partitionPoint + 1, end, depthLimit - 1)
#     return array
#
#
# def introSort_main(array):
#     n = len(array) - 1
#     depthLimit = 2 * math.floor(math.log2(n-0))
#     array = introsortUtil(array, 0, n, depthLimit)
#     return array


def shell_sort(arr):
    """
    The method starts by sorting pairs of elements far apart from each other,
    then progressively reducing the gap between elements to be compared.

    Use 128 values
    """
    gap = len(arr) // 2  # initialize the gap

    while gap > 0:
        i = 0
        j = gap

        # check the array in from left to right
        # until the last possible index of j
        while j < len(arr):

            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            i += 1
            j += 1

            # now, we look back from ith index to the left
            # we swap the values which are not in the right order.
            k = i
            while k - gap > -1:

                if arr[k - gap] > arr[k]:
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                k -= 1
            yield arr
        gap //= 2


def bubble_sort(arr):
    """
    Works by repeatedly swapping the adjacent elements if they are in wrong order.
    Worst and average case = O(n^2)
    Best case = O(n)

    use 50 values
    """
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        # very quick
            # slow
            yield arr


def cocktail_sort(arr):
    """
    Cocktail Sort traverses through elements in a given array from left and moves the largest
    element to its correct position and then from the right alternating directions.
    Worst and average case = O(n^2)
    Best case = O(n)

    use 200 values
    """
    n = len(arr)
    swap = True
    begin = 0
    end = n-1

    while swap:
        swap = False
        for i in range(begin, end):
            # Swap if the element found is greater
            # than the next element
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swap = True

        if not swap:
            break

        swap = False

        # move the end point back by one, because
        # item at the end is in its rightful spot
        end = end - 1
        # put yield here for shaker effect
        for j in range(end - 1, begin - 1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True

        # increase the starting point, because
        # the last stage would have moved the next
        # smallest number to its rightful spot.
        begin = begin + 1
        yield arr


def gnome_sort(arr):
    """
    The algorithm traverses each element in the order presented and compares
    the current element with the previous and sorts them. If sorted, take
    a "step" back and do the comparison again. This repeats until the array
    is sorted.
    Complexity = O(n^2)

    use 50 values
    """
    n = len(arr)
    idx = 0
    while idx < n:
        if idx == 0:
            idx += 1
        # If the current array element is larger or equal to the previous
        # element then go one step right
        if arr[idx] >= arr[idx - 1]:
            idx += 1
        # If the current array element is smaller than the previous element
        # then swap these two elements and go one step backwards
        else:
            arr[idx], arr[idx-1] = arr[idx-1], arr[idx]
            idx -= 1
            yield arr


def exchange(arr, i, j, order):
    if order == (arr[i] > arr[j]):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp


def bitomerge(arr, l, c, order):
    if c > 1:
        k = int(c/2)
        for x in range(l, l+k):
            exchange(arr, x, x+k, order)
        bitomerge(arr, l, k, order)
        bitomerge(arr, l+k, k, order)


def bitonic_sort(arr, l=0, c=128, order=True):
    """
    Bitonic Sort must be done if number of elements to sort are 2^n. The procedure
    of bitonic sequence fails if the number of elements are not in the aforementioned
    quantity precisely.

    A sequence is called bitonic if it is first increasing, then decreasing. In other words,
    a sequence sorted in increasing order is considered bitonic with the decreasing part
    as empty. Similarly, decreasing order sequence is considered bitonic with the increasing
    part as empty.

    To form a bitonic sequence, start by forming 4-element bitonic sequences from consecutive
    2-element sequence. Consider 4-element in sequence x0, x1, x2, x3. Sort x0 and x1 in
    ascending order and x2 and x3 in descending order. Then, concatenate the two pairs to
    form a 4 element bitonic sequence. Next, take two 4 element bitonic sequences, sorting
    one in ascending order, the other in descending order and so on, until we obtain the
    bitonic sequence.
    n = 128
    """
    if c > 1:
        k = int(c/2)
        yield from bitonic_sort(arr, l, k, True)
        yield from bitonic_sort(arr, l+k, k, False)
        bitomerge(arr, l, c, order)
        yield arr


# To check if array is sorted or not
def is_sorted(arr):
    n = len(arr)
    for i in range(0, n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# To generate permutation of the array
def shuffle(arr):
    n = len(arr)
    for i in range(0, n):
        r = random.randint(0, n - 1)
        arr[i], arr[r] = arr[r], arr[i]


def bogo_sort(arr):
    """
    The algorithm successively generates (random) permutations of its input until it finds one that is sorted.
    """
    iterations = 0
    while not is_sorted(arr):
        shuffle(arr)
        iterations += 1
        yield arr
