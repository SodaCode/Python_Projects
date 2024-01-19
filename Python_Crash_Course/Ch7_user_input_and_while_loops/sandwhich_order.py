#make a list called sandwich_orders
sandwich_orders = ['tuna', 'cheese', 'ham', 'meat', 'pastrami', 'pastrami', 'pastrami']

#make a list of finished sandwich orders
finished_sandwhiches = []

print("The deli has run out of pastrami\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich")

    finished_sandwhiches.append(current_sandwich)

print("\nSandwiches completed: ")
for sandwich in finished_sandwhiches:
    print(f"{sandwich} sandwich")
