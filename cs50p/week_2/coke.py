def main():

    amount_due = 50
    print(f"Amount due: {amount_due}")

    while amount_due > 0:
        insert_coin = check_coin(input("Insert Coin: "))
        amount_due = amount_due - int(insert_coin)
        if amount_due > 0:
            print(f"Amount Due: {amount_due}")
        else:
            print(f"Change Owed: {amount_due * -1}")         

#tutaj trafia string dlatego porównuejsz do str
def check_coin(coins):
  
        #if coins in [5, 10, 25]:
        if coins == "5" or coins == "10" or coins == "25":
            return coins
        else:
            return 0 
        


# while True:
#         n = int(input("What's n? "))
#         if n > 0:
#             return n


main()