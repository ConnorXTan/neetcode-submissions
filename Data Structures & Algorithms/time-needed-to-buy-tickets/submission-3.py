class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = 0
        for i in range(tickets[k]):
            for ticket in range(len(tickets)):
                if tickets[ticket] > 0:
                    tickets[ticket] -= 1
                    count += 1
                if tickets[k] == 0:
                    return count
        return(count)