class Page:
    
    def __init__(self, number):
        self.number = number
        self.ref_bit = 0

    def __repr__(self):
        return f"{self.number}(R={self.ref_bit})"
