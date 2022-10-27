from multipledispatch import dispatch
#pip3 install multipledispatch

class Calculator(object):
    
    @dispatch(int,int)
    def Add(self, a,b):
        print("two args")
        return a+b

    @dispatch(int,int,int)
    def Add(self, a,b,c):
        print("three args")
        return a+b+c

    
    def PosCheck(self, x=5, y=10):
        print(f"myx {x}  and myy {y}")
        return

    def RandNumber(self):
        import random
        l=[1,2,10,20,5,6,50,80,90]
      
        while True:
            rr=random.choices(l)
            yield rr

    def CallRand(self):

        #next(self.RandNumber())

        i=10
        for rb in self.RandNumber():        
            print(f"random number is {rb}")
            i=i+1
            if i>16:
                break







