#Define the menu of restaurant
menu = {
    'Pizza' : 100,
    'Pasta' : 150,
    'Burger' : 60,
    'Coffee' : 80,

}

#Greet
print ("Welcome to Restaurant")
print ("Pizza: rs100\nPasta :rs150\nBurger: rs60\nCoffee: rs80")

order_total = 0
#80+70 = 150

item_1 = input(" Enter the name of item you want to order =")
if item_1 in menu:
    order_total +=menu[item_1] #0+50
    print(f"Your item {item_1} has been ")

else :
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes" :
    item_2 = input("Enter the name of second item =")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"Ordered item{item_2} is not avaialable!")

print(f"The total amount of item to pay is {order_total} ")


