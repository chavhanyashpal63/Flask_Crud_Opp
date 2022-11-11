

class Product:

    def __init__(self,pid=0,prnm='',pqty=0,prc=0.0,pven=''):
        self.prodId = int(pid)
        self.prodName = prnm
        self.prodPrice = float(prc)
        self.prodQty = int(pqty)
        self.prodVendor = pven

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)