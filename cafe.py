## from collections import Counter # unsuccessful attempt
menu = ["coffee", "tea", "lager", "cider", "ale"]

##coffee = 0
##tea = 0
##lager = 0
##cider = 0
##ale = 0
items_value = 0

stock = {"coffee": 21,      # 25.20
         "tea": 22,         # 22
         "lager": 21,       # 42
         "cider": 23,       # 50.6
         "ale": 24}         # 60
price = {"coffee": 1.20,
         "tea": 1.00,
         "lager": 2.00,
         "cider": 2.20,
         "ale": 2.50}

# FOR MYSELF: 
# Word "value" could be ANY !!!
# "FOR LOOP" LOGIC:
# Perhaps, if FOR loop used requesting values from dictionary, then
# it takes VALUE automatically (and ignores KEY).

# WORKS!!! (30,31) <----

# for value in stock:
#     items_value += stock[value] * price[value]

## items_value = (Counter(stock) + Counter(price)) # unsuccessful attempt

# WORKS!!! (37) <----

items_value = sum(stock[item] * price[item] for item in menu) # WORKS!

## items_value = dict(stock.items() + price.items() # unsuccessful attempt

print(f"All items value in Cafe is: £{items_value:.2f}")

# found "{item_value:.2f}" trick/conversion here:
# https://pythonhow.com/how/limit-floats-to-two-decimal-points/#:~:text=The%20format%20function%20takes%20a,float%20with%20two%20decimal%20points. 