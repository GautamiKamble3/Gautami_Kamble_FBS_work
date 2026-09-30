# 2. Create another package “TY” which has a class TYMarks (Theory, Practical).

class TYMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def __str__(self):
        return f'Theory Marks : {self.theory} | Practical Marks : {self.practical}'
