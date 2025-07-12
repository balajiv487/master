class Solution:
    def destincation_city(self,paths:list[list[str]]):
        outgoing_cnt={}
        for path in paths:
            print(path)
            i,j=path
            outgoing_cnt[i]=outgoing_cnt.get(i,0)+1
            print(outgoing_cnt[i])
            outgoing_cnt[j]=outgoing_cnt.get(j,0)
            print(outgoing_cnt[j])
            print(outgoing_cnt)

        for city in outgoing_cnt:
            if outgoing_cnt[city]==0:
                print(city)
sol=Solution()
paths=[['London','New York'],['New York','Lima'],['Lima','Sao Paulo']]

sol.destincation_city(paths)