def find_pe(prices,eps,index):
    pe=prices[index]/eps[index]
    return pe

prices = [100, 150, 200]
eps = [5, 10, 0]

#print(find_pe(prices, eps, 0))

#########array#############

s_p=[298,305,320,301,292]
for i in range(len(s_p)):
    if s_p[i]==301:
        print(s_p[i])

s_p.insert(1,1999)
print(s_p)