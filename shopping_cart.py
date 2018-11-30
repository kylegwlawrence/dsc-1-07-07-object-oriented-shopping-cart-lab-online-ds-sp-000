class ShoppingCart():
    
    def __init__(self, emp_discount = None):
    # write your code here
        self._total = 0
        self._items = []
        self._employee_discount = emp_discount
    
    
    #define set and get methods for each
    
    # set and get total
    def set_total(self, amount):
        self._total += amount
        
    def get_total(self):
        return self._total
    
    # create method with property
    total = property(get_total, set_total)
    
    
    # set and get items in cart
    def set_items(self, item):
        self._items.append(item)
        
    def get_items(self):
        return self._items
    
    items = property(get_items, set_items)
    
    
    # set and get employee discount
    def set_employee_discount(self, emp_discount):
        self._employee_discount = emp_discount
    
    def get_employee_discount(self):
        return self._employee_discount
    
    employee_discount = property(get_employee_discount, set_employee_discount)
    
    def add_item(self, name, price, quantity=1):
        if type(quantity)!=int:
            return print("Enter an integer")
        elif quantity < 0:
            return print("Enter non-zero positive number")
        else:
            for i in range(quantity): #something weird happening here
                self._items.append({'name':name, 'price': price})
        add_amount = price*quantity
        self._total+=add_amount
        return self.total
    
    def mean_item_price(self):
        return round(self.total/len(self.items),2)
    
    def median_item_price(self):
        #init price list for loop
        price_list = []
        #loop over each dict in items list
        for item in self.items:
            #add each price to price list
            price_list.append(item['price'])
        #sort price list
        price_list.sort()
        #check if odd number of items
        if len(price_list)%2 != 0:
            #get index of middle value
            median_index = int(len(price_list)/2 + 0.5 -1)
            #return median rounded to 2 decimals
            return price_list[median_index]
        else:
            #first middle index - sub 1 for 0-based indexing and convert to int
            first_val = int(price_list[len(price_list)/2-1])
            #second middle index, int already converted
            second_val = first_val+1
            #return median rounded to 2 decimals
            return round(price_list[first_val]+price_list[second_val]/2,2)
    
    def apply_discount(self):
        #check if there is a discount
        if self._employee_discount == None:
            #print bad news
            return print("Sorry, there is no discount to apply to your cart :(")
        else:
            #multiply total by inverse of discount and round
            return round(self.total*(100 - self._employee_discount)/100,2)
        
    def item_names(self):
        #init list
        list_of_item_names = []
        #loop over each dict in items list
        for item in self.items:
            #sppend item name to new list
            list_of_item_names.append(item['name'])
        return list_of_item_names
    
    def void_last_item(self):
        if len(self.items)==0:
            return print("There are no items in your cart!")
        else:
            #subract price of last item in list from total
            self._total+= -1*self._items[-1]['price']
            #remove last item from list
            self._items.pop()
            
            
            
            
        
        
        
