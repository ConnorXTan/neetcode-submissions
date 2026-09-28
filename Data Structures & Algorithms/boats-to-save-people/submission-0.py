class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        amount = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if (people[l] + people[r] <= limit):
                amount += 1
                l += 1
                r -= 1
            else:
                amount += 1
                r -= 1
        return(amount)
        
