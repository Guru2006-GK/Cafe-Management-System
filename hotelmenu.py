#Define the menu of restaurant 
menu = {
    'Pizza' :40,
    'Pasta' :45,
    'Burger':69,
    'Salad' :50,
    'Coffee':20, 
}

#Greet
print("Welcome to SUVARNA NAGARA Restaurant!")
print("Burger: RS69\nCoffee: Rs20\nPasta: Rs45\nPizza: Rs40\nSalad: Rs50")

order_total = 0
#80+70=150
item_1 = input("Enter the name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has succesfully added to your order")
    
else:
    print(f"Sorry, {item_1} is not available in the menu.")
    
    another_order = input("Do you want to order another item? (yes/no)")
    if another_order =="yes":
        item_2 = input("Enter the name of item you want to order =")
        if item_2 in menu:
            order_total += menu[item_2]
            print(f"Your item {item_2} has succesfully added to your order")
        else:
            print(f"Sorry, {item_2} is not available in the menu.")
            
print(f"Your total order amount To pay is :Rs{order_total}")
