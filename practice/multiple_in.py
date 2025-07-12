class Father:
    def habit(self):
        print(f"I like Gardening")
class Mother:
    def activity(self):
        print(f"I like cooking")
class Child(Mother,Father):
    def sports(self):
        print(f"I like sports")
c=Child()
c.activity()
c.habit()
c.sports()

a=["hi","how","are","you"]
itr=iter(a)
print(next(itr))