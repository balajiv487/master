
class Stringrev:
  def reverse_str(self,s):
      self.s=list(s)
      return "".join(self.s[::-1])


txt=Stringrev()
s=input("Enter a string:")
print(f" Reverse of {s} is {txt.reverse_str(s)}")
