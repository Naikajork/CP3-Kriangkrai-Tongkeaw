class Customer:
    name = ""
    lastName = ""
    age = 0
    def addCart(self):
        print("Added products to", self.name,self.lastName,"'s cart")

customer1 = Customer()
customer1.name = "Kriangkrai"
customer1.lastName = "T"
customer1.addCart()

customer2 = Customer()
customer2.name = "Alex"
customer2.lastName = 'Furguson'
customer2.addCart()

customer3 = Customer()
customer3.name = "Bruno"
customer3.lastName = "Fernandez"
customer3.addCart()

customer4 = Customer()
customer4.name = "Devid"
customer4.lastName = "Degia"
customer4.addCart()
