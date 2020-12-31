responses = {}

poll = True 

while poll:
    name = input("Please enter your name ")
    question = input("If you could travel anywhere, where would you want to go? ")

    responses[name] = question

    repeat = input("Would anyone else want to have a go? 'yes/no' ")
    if repeat == "no":
        poll = False

print("\n ---Results---")
for name, response in responses.items():
    print(name.title() + " would like to go to " + response.title() + ".")
