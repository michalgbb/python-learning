def main():

    level = getnumber()

    if level <= 1:
            print("E")
    elif 1 < level < 99:
        print(f"{level}%")
    elif level >= 99:
        print("F")


def getnumber():
    while True:

        try:
            fuel = input("Fraction : ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)

            if x > y:
                 continue
            elif x < 0 :
                 continue
            else:
                return round(x / y * 100)
            
        except (ValueError, ZeroDivisionError):
            pass
        
    

    
    



main()