"""
Bracket Match
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa.
For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets
at the end, so you’d return 2.
Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets
you’d need to add to the input in order to make it correctly matched.
input:  text = “(()”
output: 1
input:  text = “(())”
output: 0
input:  text = “())(”
output: 2
"""

"""
Solution:

two variables, open unpair count, close unpair count
when we met a open bracket, open plus one, when we met a close bracket, open minus one if grater than zero; otherwise, close plus one.

Time Complexity:
O(N)

Space Complexity:
O(1)

"""


def solution(input_bracket):
    open_unpaired_count, close_unpaired_count = 0, 0
    for i in input_bracket:
        if i == '(':
            open_unpaired_count += 1
        elif i == ')':
            if open_unpaired_count > 0:
                open_unpaired_count -= 1
            else:
                close_unpaired_count += 1
        else:
            pass
    return open_unpaired_count + close_unpaired_count


def main():
    assert solution("(()") == 1
    assert solution("(())") == 0
    assert solution("())(") == 2
    assert solution(")(") == 2


if __name__ == '__main__':
    main()
