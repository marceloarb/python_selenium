  
class Mathdojo:
    def __init__(self):
        self.result=0
    def add(self,num,*nums):
        print(nums)
        for x in range(len(nums)):
            self.result = self.result  + nums[x]
        self.result = self.result + num
        print(self.result)
        return self
    
    def sub(self,num,*nums):
        for x in range(len(nums)):
            self.result = self.result  - nums[x]
        self.result = self.result - num
        print(self.result)
        return self



marcelo=Mathdojo()
marcelo.add(2,2,3,4,5,6,3,4,4).sub(1,2,3,4,5)