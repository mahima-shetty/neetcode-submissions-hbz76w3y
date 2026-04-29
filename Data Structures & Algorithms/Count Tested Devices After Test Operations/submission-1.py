class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        tested = 0
        for bat in batteryPercentages:
            if bat > tested:
                tested += 1
        return tested

