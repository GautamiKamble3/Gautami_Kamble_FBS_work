#  1. create a package “SY” which has class SYMARKS (Computer Total,
# # MathsTotal, ElectronicsTotal). 

class SYMARKS:
    def __init__(self, computer, maths, electronics):
        self.computer = computer
        self.maths = maths 
        self.electronics = electronics

    def __str__(self):
        return f'Computer Total : {self.computer} | Maths Total : {self.maths} | Electronics Total : {self.electronics}'
        
