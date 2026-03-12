size=input("what size of pizza do you want (L/M/S)?")
Bill=0

if size=="L" or size=="l":
    Bill +=100
    print("Small size of pizza is 100 BDT.")
elif size=="M" or size=="m":
    Bill +=150
    print("Small size of pizza is 150 BDT.")
else:
    Bill +=200
    print("Small size of pizza is 200 BDT.")

add_pepperonis=input("how many pepperonis do you want (Y/N)?")
if add_pepperonis=="Y" or add_pepperonis=="y":
    if size=="s" or size=="S":
        Bill +=20
        print("Small size of pizza is 20 BDT.")
    else:
        Bill +=25
        print(" Large or Medium size of pizza is 25 BDT.")

extra_cheese=input("Any extra cheese do you want?")
if extra_cheese=="Y" or extra_cheese=="y":
    Bill +=50

print("Your final bill is", Bill)
