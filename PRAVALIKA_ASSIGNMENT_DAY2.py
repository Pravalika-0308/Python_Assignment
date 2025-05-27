inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]
#1 Total revenue
total_revenue=0.0
i=len(inventory)

for item in inventory:
    total_revenue+=item[2]*item[3]
print(total_revenue)

#2 List Low stock item if stock is less than 5
low_stock=[]
for item in inventory:
    if(item[4]<5):
        low_stock.append(item[0])
print(low_stock)

#3. calculte the categorywise Revenue
fruit_revenue=0.0
vegetable_revenue=0.0
dairy_revenue=0.0
bakery_revenue=0.0
for item in inventory:
    if item[1] == 'Fruit':
        fruit_revenue+=item[2]*item[3]
    elif item[1] == 'Vegetable':
        vegetable_revenue+=item[2]*item[3]
    elif item[1] == 'Bakery':
        bakery_revenue+= item[2]*item[3]
    else:
        dairy_revenue+= item[2]*item[3]
    
print('fruit revenue is : ',fruit_revenue)
print('vegetable revenue is : ',vegetable_revenue)
print('bakery revenue is : ',bakery_revenue)
print('diary revenue is : ',dairy_revenue)
    












