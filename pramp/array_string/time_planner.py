"""
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur,
returns the earliest time slot that works for both of them and is of duration dur.
If there is no common time slot that satisfies the duration requirement, return an empty array.
Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two.
The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot.
The input variable dur is a positive integer that represents the duration of a meeting in seconds.
The output is also a pair represented by an epoch array of size two.
In your implementation assume that the time slots in a person’s availability are disjointed, i.e,
time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 8
output: [60, 68]
input:  slotsA = [[10, 50], [60, 120], [140, 210]]
        slotsB = [[0, 15], [60, 70]]
        dur = 12
output: [] # since there is no common slot whose duration is 12
"""

"""
Solution:
1. we need to find all overlapped availability time. 
using two points, check pointed slots if they have overlapped time, record it. move to the next slot which end time equal or smaller than overlapped end time.
2. check if overlapped time is grater than the meeting duration time.

Time Complexity: O(M+N)
Space Complexity: O(1)

"""


def solution(slotsA, slotsB, dur):
    m, n = len(slotsA), len(slotsB)
    i, j = 0, 0
    while i < m and j < n:
        start_a, end_a = slotsA[i]
        start_b, end_b = slotsB[j]
        start_overlapped = max(start_a, start_b)
        end_overlapped = min(end_a, end_b)
        if start_overlapped <= end_overlapped:
            if end_overlapped - start_overlapped >= dur:
                return [start_overlapped, start_overlapped + dur]
        if end_overlapped >= end_a:
            i += 1
        if end_overlapped >= end_b:
            j += 1

    return []


def main():
    assert solution(slotsA=[[10, 50], [60, 120], [140, 210]], slotsB=[[0, 15], [60, 70]], dur=8) == [60, 68]
    assert solution(slotsA=[[10, 50], [60, 120], [140, 210]], slotsB=[[0, 15], [60, 70]], dur=12) == []


if __name__ == '__main__':
    main()
