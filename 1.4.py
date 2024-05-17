import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]
# Tag each product based on keywords in the description
# Your code here

electronics = r"\b(screen|memory)\b"
apparel = r"\b(size|medium|small|large)\b"
kitchen = r"\b(kitchen|knife)\b"


for description in descriptions:
    if re.findall(electronics, description):
        print(f"Electronics: {description}")
    
    if re.findall(apparel, description):
        print(f"Apparel: {description}")

    if re.findall(kitchen, description):
        print(f"Kitchen: {description}")

    
    

