# m = n
# O(M+N) # O(N)
def find_duplicates(arr1, arr2):
    i, j = 0, 0
    duplicates = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            duplicates.append(arr1[i])
            i += 1
            j += 1
    return duplicates


def binary_search(arr, element):
    low, high = 0, len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return mid
        if arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# m >> n
# O(N*LOGM) O(N)
def find_duplicates_2(arr1, arr2):
    n, m = len(arr1), len(arr2)
    duplicates = []
    for i in arr1:
        index = binary_search(arr2, i)
        if index != -1:
            duplicates.append(i)
    return duplicates


