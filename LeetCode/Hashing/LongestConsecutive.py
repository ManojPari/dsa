from ast import List
from collections import Counter
import math
def maxPoints(points) -> int:
        if len(points) < 3:
            return len(points)
        max_count = 0
        for i in range(len(points)):
            slope_dict = {}
            same_point_count = 0
            
            for j in range(len(points)):
                if i == j:
                    continue
                
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                if dx == 0 and dy == 0:
                    same_point_count += 1
                    continue
                
                gcd_val = math.gcd(dx, dy)
                slope = (dx // gcd_val, dy // gcd_val)
                
                slope_dict[slope] = slope_dict.get(slope, 0) + 1
            
            same_line_points = max(slope_dict.values(), default=0) + same_point_count
             max_count = max(max_count, same_line_points)
        print(max_count)
        return max_count
nums = [[1,1],[2,2],[3,3]]
maxPoints(nums)