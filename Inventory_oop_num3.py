# Inventory pro v3
class Product:   # Our main class
    def __init__(self, name, price, stock):
        self._name = name
        self._price = price
        self._stock = stock

    @property
    def name(self):
        return self._name 
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        self._price = new_price
    
    @property 
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, new_stock):
        self._stock = new_stock
    
    @property
    def get_details(self):
        return self._name, self._price, self._stock
        
# Second class with an extra attribute      
class Electronic(Product):
    def __init__(self, name, price, stock, warranty_months):
        super().__init__(name, price, stock)
        self._warranty_months = warranty_months
    
    @property
    def get_details(self):
        return self._name, self._price, self._stock, self._warranty_months
      
# Third class with an extra attribute
class PerishableProduct(Product):
    def __init__(self, name, price, stock, expiration_date):
        super().__init__(name, price, stock)  
        self._expiration_date = expiration_date
    
    @property
    def get_details(self):
        return self._name, self._price, self._stock, self._expiration_date
    
# The main class 
class Inventory:
    def __init__(self, name_of_store):
        self.name_of_store = name_of_store
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
    
    def show_products(self):
        if not self.products:
            print("Nothing to show")
        else:
            print("= = P R O D U C T S = = \n")
            for i in self.products:
                print(i.get_details)
    
    def search_product(self):
        isFound = False
        if not self.products:
            print("Nothing to see")
        else:
            target = input("Insert the name of the product: ")
            for i in self.products:
                if target == i._name:
                    print("Product exist!")
                    isFound = True
                    break
            if not isFound:
                print("Product not in the list") 
                                           
my_inventory = Inventory("Mercapava")

# Menu 
while True:
    print("\n = = = M E N U = = = \n")
    print("1) Add product \t")
    print("2) Show products \t")
    print("3) Search product \t")
    print("4) Exit \t")
    try:
        option = int(input("Select yor option ( 1 - 4 ): \t "))
        
        match option:
            case 1:
                print("= = Type of product = = ")
                print("1) Normal ")
                print("2) Electronic ")
                print("3) Perishable ")
                try:
                    data = int(input("Select the type of product: (1-3) "))
                    match data:
                        
                        case 1: # Normal product 
                            name = input("Enter the name of the product: ")
                            price = int(input("Enter the price: "))
                            stock = int(input("Enter the amount: "))
                            
                            product = Product(name, price, stock)
                            
                            my_inventory.add_product(product)
                            
                            
                        case 2: # Electronic product
                            name = input("Enter the name of the product: ")
                            price = int(input("Enter the price: "))
                            stock = int(input("Enter the amount: "))
                            warranty = int(input("Months of warranty?: "))
                            
                            electronic = Electronic(name, price, stock, warranty)
                            
                            my_inventory.add_product(electronic)
                               
                        case 3: # Perishable product 
                            name = input("Enter the name of the product: ")
                            price = int(input("Enter the price: "))
                            stock = int(input("Enter the amount: "))
                            expiration = input("Expiration date of the product: ") 
                            
                            perishable = PerishableProduct(name, price, stock, expiration)
                            
                            my_inventory.add_product(perishable)
                            
                        case _:
                            print("Something went wrong!")
                except ValueError:
                    print("Invalid option!")            
                
            case 2:
                
                print("Calling products . . . \n ")
                my_inventory.show_products()
                
            case 3:
                print("Searching . . . ")
                my_inventory.search_product()
                
            case 4:
                print("Exiting of the program . . . ")
                break  
            case _: 
                print("Invalid option ") 
    except ValueError:
        print("Select a valid option")               
                            
            


       
        
        
        