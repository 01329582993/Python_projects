text = input("Enter some text: ")

for char in text:
    if char == ' ':
        print("...", end ="")
    else:
        print(char, end= "")
