def main():
    name = input("What your name? ")
    hello(name)

def hello(to = "world"):
    print("Hello", to)

main()