try:
    a=int(input("Inter your first value:"))
    b=int(input("Inter your second value:"))
    c=a/b
    print("result is:",c)

    if a>b:
        print("a ia gatter than b.")
    else:
        print("g is gater than c.")

except ZeroDivisionError:
    print(" value is not division by zero.")
except SyntaxError:
    print("Code is not written correctly.")
except ValueError:
    print("The type is correct but the value is wrong.")
except NameError:
    print("This veriable is not exist.")
except Exception as e:
    print("other exception is occured .")