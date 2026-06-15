type = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
type = type.replace("-", " ").title().strip()


if type == "Forty Two" or type == "42":
    print("Yes")  
else:
    print("No")
    
