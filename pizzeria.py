import random
speciality_toppings = ['Pepperoni','Mushrooms','Onions','Sausage','Bacon','Extra cheese','Black olives','Green peppers','Pineapple','Spinach']
# sizes = {'10" Small': 7.80, '12" Medium':9.29, '14" Large':11.29, '16" X-Large':14.49}
sizes = {'Small':7.80, 'Medium':9.29, 'Large':11.29, 'X-Large':14.49}

#Exercise 12 - Expanded
class PizzaPie:
    def __init__(self, order, size, number_of_toppings):
        self.order = order
        self.size = size
        self.number_of_toppings = number_of_toppings
        self.toppings = []
        # self.price = price
        print(f'Creating {size} pizza #{order} with {number_of_toppings} toppings.')
    
    def __repr__(self): #String representation of this PizzaPie.
        self.get_price()
        if self.toppings:
            pass
            return (f'Pizza #{self.order}: {self.size} with {self.toppings} - ${self.price}')
        else:
            pass
            return (f'Pizza #{self.order}: {self.size} with Nothing on it - ${self.price}')
    
    # def get_num_toppings(self):
    #     return self.number_of_toppings

    def get_price(self):
        self.price = (round(sizes[self.size] + (self.number_of_toppings * 1.45), 2))

    #     print(self.price)


# pizzas = []

# pizzas.append(PizzaPie(1, 7)) #Initializes a PizzaPie with 7 toppings.
# pizzas.append(PizzaPie(2, 3)) #Initializes a PizzaPie with 3 toppings.

# print(pizzas[0].number_of_toppings)
# print(pizzas[0].get_num_toppings())




def get_number_of_pizzas(): #Ask user how many pizzas they would like to order.
    print('How many pizzas do you want to order?')
    return random.randint(1,9) #int(input())


def get_size_of_pizza(order_number):
    print(f'\nHow big is pizza {order_number}?')
    return random.choice(list(sizes.keys())) #input()



def get_number_of_toppings(order_number): #Asks user how many toppings they want on this order.
    print(f'How many toppings for pizza {order_number}?')
    return random.randint(0,9) #int(input())


def choose_toppings(topping_number): #Asks user which topping(s) they want.
    print(f'What\'s your topping #{topping_number}?')
    return speciality_toppings[random.randint(0,9)] #input()


# def calculate_total_cost():
#     for pizza in range (1, pizzaPies):
#         print
#         pass
    


def display_orders(pizzaPies): #Displays a list of order_number with each toppings.
    if pizzaPies: #If pizzaPies exist, there is at least 1 order.
        print('\nHeres your order!')

        for pizza in pizzaPies:
            print(pizza.__repr__()) #String representation of this PizzaPie.
        
    else: #Else pizzaPies does not exist, and there are 0 orders.
        print('What, you don\'t like pizza?')



def order_pizza():
    pizzaPies = [] #This will store all PizzaPie objects.
    print('**Panucci\'s Pizza : We make your pizza and we make it hot!**\n')
    pizzas = get_number_of_pizzas() #Asks user how many pizzas they want.
    
    for pizza in range(1, pizzas+1): #Loops through the number of pizzas ordered.
        size = get_size_of_pizza(pizza)
        # print(f'So a that\'s a {size} pizza eh?')

        toppings = get_number_of_toppings(pizza) #Gets number of toppings for this pizza..
        # print(f'So that\'s {toppings} toppings for pizza {pizza} eh?')

        # cost = calculate_cost(size, toppings)
        
        pizzaPies.append(PizzaPie(pizza, size, toppings)) #Initializes a PizzaPie with x toppings.

        # print(pizzaPies[pizza-1].toppings)
        
        for topping in range(1, toppings+1):
            # current_topping = choose_toppings(topping)

            pizzaPies[pizza-1].toppings.append(choose_toppings(topping))
            # print(current_topping)

        # print(pizzaPies[pizza-1].toppings)        

    display_orders(pizzaPies) #Displays the order.

order_pizza() #Starts the pizza-ordering process.