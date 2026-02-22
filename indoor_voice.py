def make_lower(a):
    if any(char.isupper() for char in a):
        print("Capital letter found, converting to lowercase")
        return a.lower()
    else:
        print("You are good to go, no capitals found!")
        return a

text = input("Enter your inputs: ")
result = make_lower(text)
print("Final Version after review:", result)  
