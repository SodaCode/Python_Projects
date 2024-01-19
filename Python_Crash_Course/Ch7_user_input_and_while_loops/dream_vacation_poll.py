responses = {}

poll_active = True

while poll_active:
    name = input("What is your name?").title()
    response = input("What is your dream vacation location?")
    
    #store response in dic using name as key
    responses[name] = response

    repeat = input("Would you like someone else to respond?").lower()

    if repeat == 'no':
        poll_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} whould like to go to {response}")