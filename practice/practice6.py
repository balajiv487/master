class Solution:
    def search(self,num:list[int],target:int)->int:
        for i,num in enumerate(num):
            print(f"i is: {i,num}")
            if num==target:
                return i
        return -1
sol=Solution()
print(sol.search([1,3,5,6,7,9,10],10))