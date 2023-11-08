import timeit
import random
import matplotlib.pyplot as plt
# https://www.programiz.com/dsa/merge-sort
def mergeSort(arr):
    if len(arr) > 1:

        #  r is the point where the array is divided into two subarrays
        r = len(arr) // 2
        L = arr[:r]
        M = arr[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1

# https://www.programiz.com/dsa/insertion-sort
def insertionSort(arr):
    for step in range(1, len(arr)):
        key = arr[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        arr[j + 1] = key

def hybridSort(arr, k):
    if len(arr) // 2 <= k:
        insertionSort(arr)
    else:
        mergeSort(arr)

# Function to generate a random dataset of a given size with a uniform distribution
def uniform(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Function to generate a nearly sorted dataset
def nearlySorted(size, percent_unsorted=10):
    num_unsorted = size * percent_unsorted // 100
    sorted_part = [i for i in range(1, size - num_unsorted + 1)]
    unsorted_part = [random.randint(1, size) for _ in range(num_unsorted)]
    return sorted_part + unsorted_part

# idx used for the first time insertion becomes slower than merge
idx = 0
firstIdxFound = False
# declare lists to keep track of times for each algorithm/variant
uniMergeTimeLst = []
uniInsertTimeLst = []
uniHybridTimeLst = []
k = 200
for n in range(0, 1000):
    timer1 = timeit.Timer(lambda: mergeSort(uniform(n)))
    time_taken1 = timer1.timeit(number=1)
    uniMergeTimeLst.append(time_taken1)
    timer2 = timeit.Timer(lambda: insertionSort(uniform(n)))
    time_taken2 = timer2.timeit(number=1)
    uniInsertTimeLst.append(time_taken2)

    timer3 = timeit.Timer(lambda: hybridSort(uniform(n), k))
    time_taken3 = timer3.timeit(number=1)
    uniHybridTimeLst.append(time_taken3)


# print(idx)
plt.plot(uniMergeTimeLst, label='Merge Sort (uniform)')
plt.plot(uniInsertTimeLst, label='Insertion Sort (uniform)')
plt.plot(uniHybridTimeLst, label='Hybrid Sort (uniform)')
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.title("Merge Sort vs. Insertion Sort vs. Hybrid Sort")
plt.legend()
plt.show()
