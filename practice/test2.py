class Point:
    def __init__(self,x,y=2):
        self.x=x
        self.y=y

    def __str__(self):
        return "{},{}" .format(self.x,self.y)
    def euclidean_distance(self,other):
        return ((self.x-self.y)**2+(self.y-self.x)**2)*0.5
p1=Point(0,1)
p2=Point(1,1)

#print(p2.euclidean_distance(p1))
lkkewkh;oiehqo;uqnewrowqiur0qc