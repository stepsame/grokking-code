"""
Award Budget Cuts
The awards committee of your alma mater (i.e. your college/university) asked for your assistance with a budget allocation problem they’re facing.
Originally, the committee planned to give N research grants this year. However, due to spending cutbacks, the budget was reduced to newBudget dollars
and now they need to reallocate the grants. The committee made a decision that they’d like to impact as few grant recipients as possible by applying
a maximum cap on all grants. Every grant initially planned to be higher than cap will now be exactly cap dollars.
Grants less or equal to cap, obviously, won’t be impacted.
Given an array grantsArray of the original grants and the reduced budget newBudget,
write a function findGrantsCap that finds in the most efficient manner a cap such that the least number of recipients is impacted
and that the new budget constraint is met (i.e. sum of the N reallocated grants equals to newBudget).
input:  grantsArray = [2, 100, 50, 120, 1000], newBudget = 190
output: 47 # and given this cap the new grants array would be
           # [2, 47, 47, 47, 47]. Notice that the sum of the
           # new grants is indeed 190
"""

"""
Solution:
first, sort out this grants array by ascending order.
then, iterate the array, assume current grants is the cap, so all the other grants will be same as this grant.
So we can calculate if it's enough for us to apply grants.
If we can, then we can move to next one and the budget minus current grants.
Others, that means the cap is smaller than current grants and we can calculate it.
the cap equals left budget divided by left grants number.

Time Complexity: O(NlogN) sorting
Space Complexity: O(1)

"""


def solution(grants_array, new_budget):
    # sort the grants array
    grants_array.sort()

    new_grants = []
    left_budget = new_budget
    left_grant_num = len(grants_array)
    for i in range(len(grants_array)):
        cap = grants_array[i]
        if cap * left_grant_num >= left_budget:
            cap = left_budget // left_grant_num
            return cap
        left_budget -= grants_array[i]
        left_grant_num -= 1
    return grants_array[-1]


def main():
    assert solution(grants_array = [2, 100, 50, 120, 1000], new_budget = 190) == 47
    assert solution(grants_array = [2, 100, 50, 120, 1000], new_budget = 10000000) == 1000


if __name__ == '__main__':
    main()
