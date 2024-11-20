class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = sum(accounts[0])

        if len(accounts) == 1:
            return richest
        else:
            for account in accounts[1:]:
                wealth = sum(account)
                richest = wealth if wealth > richest else richest

        return richest