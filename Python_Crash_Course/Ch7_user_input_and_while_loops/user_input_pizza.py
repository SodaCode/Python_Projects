prompt = "\nPlease enter the pizza toppings you want:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"We\'ll add {toppings} to your pizza!")