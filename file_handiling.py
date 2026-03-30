
File = open('03-24-26/name.txt', 'r')
read = File.read()
print(read)
File.close()
with open ("03-24-26/name.txt","r") as r:
    content=r.read()
    print(content)


import os

# Ensure the directory exists to avoid a FileNotFoundError
os.makedirs("03-24-26", exist_ok=True)

with open("03-24-26/name.txt", "w") as r:
    # Adding the initial lines
    r.write("His name is Dina. And he is 22 years old. I live in Dhanmondi.\n\n")
    r.write("His name is Dina. And he is 22 years old. I live in Dhanmondi.\n\n")
    
    # Using triple quotes for the multi-line introduction
    introduction = """Hello! My name is Sudipto Mandol. I am a Software Engineering major 
currently pursuing my B.Sc. in Computer Science and Engineering at 
Bangladesh University of Business and Technology.

I am a passionate Full-Stack Web Developer with expertise in Python, Django, and React. 
I enjoy building functional, user-centered applications, such as my 'Save & Sell' project, 
which focuses on reducing food waste through technology. Beyond web development, 
I have a strong interest in Machine Learning and Game Development, particularly 
using the Unity engine.

I am currently focused on sharpening my technical skills and practicing my spoken 
English to prepare for a career in the global software industry."""
    
    r.write(introduction)
    r.write(introduction)

print("File '03-24-26/name.txt' has been created successfully!")

import os

file_name = 'name.txt'

if os.path.exists(file_name):
    print("File exists. Opening now...")
    with open(file_name, 'r') as f:
        print(f.read())
else:
    print(f"Error: {file_name} namer kono file pawa jayni!")