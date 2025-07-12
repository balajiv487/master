class Solution:
    def interprt(self,command:str):
        return command.replace("()","o").replace("(al)","al")
