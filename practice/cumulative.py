wave_heights=[1.0,2.0,0.3,0.5]
total=0
cumulative=[]

for i in wave_heights:
     total +=i
     cumulative.append(total)
     print(total)
     print(cumulative)