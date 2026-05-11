def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheese_shop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

############################
cheese_shop("Limburger",)

cheese_shop("Limburger", "It's very funny, sir.", "It's really very, VERY funny, sir.", )

cheese_shop("Limburger",shopkeeper="Michael Palin", 
            client="John Cleese", 
            sketch="Cheese Shop Sketch")