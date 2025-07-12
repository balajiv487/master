class Solution:
    def smallNumberThanCurrent(self, num:list[int])->list[int]:
        output=[]
        for i in range(len(num)):
            print("i:", i)
            print(f"num[{i}] is :{num[i]}")
            cnt=0
            for j in range(len(num)):
                print("j:", j)
                print(f"num[{j}] is :{num[j]}")
                if i !=j and num[j]<num[i]:
                    cnt+=1
                    print(f"cnt: {cnt}")
            output.append(cnt)
        return output

sol=Solution()
num=[8,1,2,2,3]
print(sol.smallNumberThanCurrent(num))
