class Page:
    
    def __init__(self, numero):
        self.numero = numero
        self.ref_bit = 0

    def __repr__(self):
        return f"{self.numero}(R={self.ref_bit})"
