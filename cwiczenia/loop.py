i = 0

while i < 3:
    print("Meow")
    i = i + 1

for i in [0, 1, 2]:
    print("Meow")

# #lenght

students = ["Ron", "Hermione", "Harry"]
for i in range(len(students)):
    print(i + 1, students[i])

def main():

    meaw(get_number())
    
def get_number():
    while True:
        n = input("What is the number? : ")
        n = int(n)
        if n > 0:
            return n
        
def meaw(n):
    for _ in range(n):
        print("Meaw")

main()    
