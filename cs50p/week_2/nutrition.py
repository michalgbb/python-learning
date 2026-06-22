def main():

    fruits = { 
        "Apple": "130", 
        "Avocado": "50",
        "Banana": "110",
        "Cantaloupe": "50",
        "Grapefruit": "60",
        "Grapes": "90",
        "Honeydew Melon": "50",
        "Kiwifruit": "90",
        "Lemon": "15",
        "Lime": "20",
        "Nectarin": "60",
        "Orange": "80",
        "Peach": "60",
        "Pear": "100",
        "Pinneapple": "50",
        "Plums": "70",
        "Strawberries": "50",
        "Sweet Cherries": "100",
        "Tangerine": "50",
        "Watermelon": "80"
    }



    name = input("Item : ").lower()
   

    for fruit in fruits:
        if fruit.lower() == name:
            print(f"Calories: {fruits[fruit]}")
            break 
        
    
  
    #         if name in fruits:
    #             name = fruits[name]
    #             print(f"Calories: {fruits[name]}")
    #         else:
    #             return ""
        



    # if name == fruits[name]:
    #     print(name)

    # else:
    #     return ""
   


main() 