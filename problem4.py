text = input("Enter something: ")

file = open("notes.txt", "a")  
file.write(text + "\n")
file.close()

print("Data added successfully!")