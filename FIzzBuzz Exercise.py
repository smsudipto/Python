for i in range (1,21):
    if i%3==0 and i%5==0:
        print(f"{i} is a FizzBuzz number.")
    elif i%3==0:
        print(f"{i} is a Fizz number.")
    elif i%5==0:
        print(f"{i} is a Buzz number.")
    else:
        print(f"{i} is a only a number.")