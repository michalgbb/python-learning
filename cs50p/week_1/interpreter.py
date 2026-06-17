
cal = input("Expression: ").strip()
x , y, z = cal.split(" ", 2)
x = int(x)
z = int(z)

if y == "*":
    result = x * z
elif y == "/":
    result = x / z  
elif y == "+":
    result = x + z
elif y == "-":
    result = x - z       

print(f"{float(result)}")    

