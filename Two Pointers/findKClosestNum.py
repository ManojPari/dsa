# def findClosestElements(arr, k, x):
#         left = 0
#         right = len(arr) - k
        
#         while left < right:
#             mid = left + (right - left) // 2
#             if x - arr[mid] > arr[mid + k] - x:
#                 left = mid + 1
#             else:
#                 right = mid
        
#         return arr[left:left + k]
# nums = [1,2,3,4,5]
# k = 4
# x = 3
# findClosestElements(nums, k, x)

def isPalindrome(s) -> bool:
        s = s.lower()
        string = ''
        for i in s:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 48 and ord(i) <= 57):
                string += i
        print(string)
        return string == string[::-1]
s = "Marge, let's \"[went].\" I await {news} telegram."
isPalindrome(s)