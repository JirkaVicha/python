# Love calculator
print("Welcome to Love Calculator!")
name1 = input("What is your name?\n").lower()
name2 = input("What is her name?\n").lower()


# Count letters TRUELOVE in names
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

l = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

true = t + r + u + e
love = l + o + v + e
true_love = int(str(true) + str(love))

print(f"Calculator of the True Love figure out: You potential of love is on {true_love}%")

if true_love < 20:
    print("You do not match to each other.")
elif true_love <= 50:
    print("You like each other quite well.")
else:
    print("You love each other so much!!")
    




