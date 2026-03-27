#1.

score=0
def game_score(car_score):
    global score
    score= score + 10
game_score()
print(score)

#2.

score=0
def add_point():
    global score
    score=score + 10
    print(f"Point Added! Curren Score {score}")
def penalty():
    global score
    score=score - 5
    print(f"Penalty! Curren Score {score}")
add_point()
add_point()
penalty()

#3.
is_logged_in=False
def login():
    global is_logged_in
    is_logged_in=True
    print("User login Successful!!")
def check_status():
    if is_logged_in:
        print("Welcome back!!You can access the dashboard.")
    else:
        print("Please login first.")
check_status()
login()
check_status()






