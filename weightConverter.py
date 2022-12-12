print("hello, I am Ayesha")
print("welcome you to Weight Converter Program")
weight = int(input(" Please enter your weight: "))
unit = input(" (l)bs or (k)gs: ")
if unit.upper == "L":
    converted = weight * 0.45
    print("You are", converted, "kilos")
else:
    converted = weight / 0.45
    print("You are", converted, "pounds")
