"""
Root of Number
Many times, we need to re-implement basic functions without using any standard library functions already implemented.
For example, when designing a chip that requires very little memory space.
In this question we’ll implement a function root that calculates the n’th root of a number.
The function takes a nonnegative number x and a positive integer n, and returns the positive n’th root of x within an error of 0.001
(i.e. suppose the real root is y, then the error is: |y-root(x,n)| and must satisfy |y-root(x,n)| < 0.001).
Don’t be intimidated by the question. While there are many algorithms to calculate roots that require prior knowledge in numerical analysis
(some of them are mentioned here), there is also an elementary method which doesn’t require more than guessing-and-checking.
Try to think more in terms of the latter.
Make sure your algorithm is efficient, and analyze its time and space complexities.
input:  x = 7, n = 3
output: 1.913
input:  x = 9, n = 2
output: 3
"""

"""
Solution:
We can use Bisection method to find the roots of the given equation by repeatedly dividing the interval..

Time Complexity: like binary search, O(logX)
Space Complexity: O(1)

"""


def solution(x, n):
    if n == 0:
        return

    low, high = 0, max(1, x)
    while low <= high:
        mid = (low + high) / 2.0
        power = mid ** n
        if abs(power - x) < 0.001:
            return mid
        if power < x:
            low = mid
        else:
            high = mid
    return 0


def main():
    print(solution(x=7, n = 3))
    # assert solution(x=7, n = 3) == 1.913
    print(solution(x=9, n=2))
    # assert solution(x=9, n = 2) == 3


if __name__ == '__main__':
    main()
