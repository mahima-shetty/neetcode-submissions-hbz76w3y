
class Solution:
    def calculateDiagonal(self, a:int, b: int) -> float:
        return math.sqrt((a*a) + (b*b))

    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_area = 0
        max_diagonal = 0

        for a , b in dimensions:
            diagonal = self.calculateDiagonal(a, b)
            area = a * b

            if max_diagonal < diagonal:
                max_diagonal = diagonal
                max_area = area
            elif max_diagonal == diagonal:
                max_area = max(max_area, area)
            
        return max_area
