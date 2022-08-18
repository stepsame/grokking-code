"""
question:
Given an array, find the average of all  subarrays of ‘K’ contiguous elements in it.
"""

"""
new words:
contiguous
brute-force algorithm
complexity
slide
"""

def find_average_of_subarrays(k, array):
    result = []
    window_sum, window_start = 0.0, 0
    for window_end in range(len(array)):
        # add the next element
        window_sum += array[window_end]
        # slide the window, no need to slide if we've not hit the required window size of 'k'
        if window_end >= k - 1:
            result.append(window_sum / k)  # calculate the average
            window_sum -= array[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


def main():
    result = find_average_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    assert result == [2.2, 2.8, 2.4, 3.6, 2.8]
    print("Averages of subarrays of size K: " + str(result))


if __name__ == '__main__':
    main()
