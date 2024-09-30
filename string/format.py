price = 50
txt = f"it is very {'expensive' if price>50 else 'cheap'}"
print(txt)

fruit = "apples"
txt2 = f"I love {fruit.upper()}"
print(txt2)

txt3 = "The price is {:.2f}"
print(txt3.format(price))

txt4 = "My order is {carname} and model {model}"
print(txt4.format(carname="ford", model="mustang"))

# f strings are better
