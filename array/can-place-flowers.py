class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        planted = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # empty on the end
                if i == 0 and flowerbed[i+1] == 0 or i == len(flowerbed) - 1 and flowerbed[i-1] == 0:
                    flowerbed[i] = 1
                    planted += 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    planted += 1
        return n <= planted

        