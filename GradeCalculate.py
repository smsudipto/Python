mark=int(input("enter mark:"))
if 100>=mark>=80 :
    print("your grades  is:A+")
elif mark>=101 :
    print("This result is invalid.")
elif 70<=mark<=79:
    print("your grades  is:A")
elif 60<=mark<=69:
    print("your grades  is:A-")
elif 59>=mark>=50:
    print("your grades  is:B")
elif 49>=mark>=40:
    print("your grades  is:C")
elif 33<=mark<=39:
    print("your grades  is:D")
elif mark<0:
    print("your grades  is invalid.")
else:
    print("your grades  is:F")