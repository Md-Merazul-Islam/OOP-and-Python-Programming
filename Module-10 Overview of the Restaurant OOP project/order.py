class Order :
    def __init__(self,customer,item) -> None:
        self.customer = customer
        self.items = item
        total = 0
        for item in item:
            total+= item.price
        self.bill = total
        