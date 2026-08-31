import inflect

def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            
            name = input("Name: ")
            names.append(name)
            # for n in names:
            #     print(n) 
            

        except EOFError: 
            print()
            print(f"Adieu, adieu, to {p.join(names)}")
            break



main()