"""
Deletion Distance
The deletion distance of two strings is the minimum number of characters you need to delete in the two strings in order to get the same string.
For instance, the deletion distance between "heat" and "hit" is 3:
By deleting 'e' and 'a' in "heat", and 'i' in "hit", we get the string "ht" in both cases.
Given the strings str1 and str2, write an efficient function deletionDistance that returns the deletion distance between them.
input:  str1 = "dog", str2 = "frog"
output: 3
input:  str1 = "some", str2 = "some"
output: 0
input:  str1 = "some", str2 = "thing"
output: 9
input:  str1 = "", str2 = ""
output: 0
"""
from timeit import timeit

"""
Solution:
In order to determine the minimum number of delete operations needed,
 we can make use of the length of the longest common sequence among the two given strings s1 and s2, say given by lcs.
If we can find this lcs value, we can easily determine the required result as m + n - 2*lcs.
Here, m and n refer to the length of the two given strings s1 and s2.

The above equation works because in case of complete mismatch(i.e. if the two strings can't be equalized at all), 
the total number of delete operations required will be m + n.
Now, if there is a common sequence among the two strings of length lcs,
we need to do lcs lesser deletions in both the strings leading to a total of 2lcs lesser deletions,
which then leads to the above equation.

LCS Solution 1:
In order to find the length of the longest common sequence,
we make use of a recursive function lcs(s1,s2,i,j) which returns the length of the longest common sequence
 among the strings s1 and s2 considering their lengths upto i and j respectively.
For evaluating the function, we check if the characters s1[m-1] and s2[n-1] for equality.
If they match, we can consider the corresponding strings upto 1 lesser lengths
 since the last characters have already been considered and add 1 to the result to be returned for strings of 1 lesser lengths.
Thus, we make the function call lcs(s1, s2, i-1, j-1).

If the last characters don't match, we have two options,
 either we can consider the second last character of s1 and the last character of s2,
  or we can consider the second last character of s2 and the last character of s1.
We need to consider the larger result obtained out of the two considerations for getting the required length.

Thus, the function call lcs(s1,s2,m,n) returns the required lcs value.

Time Complexity: O(2^max(m,n)). Size of recursion tree will be 2^(m+n). Here, m and n refer to the lengths of s1 and s2 respectively.

LCS Solution 2:
We can observe that in the last approach, while determining the lcs value, a lot of redundant function calls are made,
 since the same mm and nn values to be used for the function calls could be obtained going through many different paths.
We can remove this redundancy by making use of a memo array to store the value to be returned for these function calls
 if they have been called once with the corresponding parameters.
Thus, memo[i][j] is used to store the result for the function call lcs(s1,s2,i,j).
Thus, by returning the already stored values from the memo array, we can prune the search space to a great extent.

Time Complexity: O(m*n). memo array of size m*n needs to be filled once. Here, m and n refer to the length of the strings s1 and s2 respectively.
Space Complexity: O(m*n). memo array of size m*n is used. Also, The depth of the recursion tree will go upto max(m,n)

LCS Solution 3:
Another method to obtain the value of lcs is to make use of Dynamic Programming.
We make use of a 2-D dp, in which dp[i][j] represents the length of the longest common subsequence
 among the strings s1 and s2 considering their lengths upto (i-1)th index and (j-1)th index only respectively.
We fill the dp array in row-by-row order.

In order to fill the entry for dp[i][j], we can have two cases:
    1.The characters s1[i-1] and s2[j-1] match with each other.
     In this case, the entry for dp[i][j] will be one more than the entry obtained for the strings
     considering their lengths upto one lesser index,
     since the matched character adds one to the length of LCS formed till the current indices.
    Thus, the dp[i][j] entry is updated as dp[i][j] = 1 + dp[i-1][j-1].
    Note that dp[i-1][j-1] has been used because the matched character belongs to both s1 and s2.
    2.The characters s1[i-1] and s2[j-1] don't match with each other.
     In this case, we can't increment the current entry as compared to entries corresponding to the previous indices,
     but we need to replicate the previous entry again to indicate that the length of LCS upto the current indices also remains the same.
    But, which entry to pick up? Now, since the current character hasn't matched, we have got two options.
    We can remove the current character from consideration from either s1 or s2
    and use the corresponding dp entries given by dp[i-1][j] and dp[i][j-1] respectively.
    Since we are considering the length of LCS upto the current indices
     we need to pick up the larger entry out of these two to update the current dp entry.
     
Time complexity : O(m*n). We need to fill in the dp array of size m*n. Here, mm and nn refer to the lengths of s1 and s2.
Space complexity : O(m*n). dp array of size m*n is used.
"""


def lcs(s1, s2, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if memo[m][n] > 0:
        return memo[n][n]
    if s1[m - 1] == s2[n - 1]:
        memo[m][n] = 1 + lcs(s1, s2, m - 1, n - 1, memo)
    else:
        memo[m][n] = max(lcs(s1, s2, m, n - 1, memo), lcs(s1, s2, m - 1, n, memo))
    return memo[m][n]


def lcs_dp(s1, s2, m, n):
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


def solution(s1, s2):
    m, n = len(s1), len(s2)
    # memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # lcs_result = lcs(s1, s2, m, n, memo)
    lcs_result = lcs_dp(s1, s2, m, n)
    return m + n - 2 * lcs_result


def main():
    # print(timeit("solution('heat', 'hit')", globals=globals()))
    assert solution('heat', 'hit') == 3


if __name__ == '__main__':
    main()
