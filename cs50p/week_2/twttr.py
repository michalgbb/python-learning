

words = input("Input: ")
name = ""

for word in words:
    if word.lower() in ["a", "e", "i", "o", "u"]:
        name += ""
    else:
        name += word
    
print(name, end="")

# #2 not in

# name2 = ""

# for word in words:
#     if word.lower() not in ["a", "e", "i", "o", "u"]:
#         name2 += word 

# print(name2)

# #3 list

# name3 = []

# for word in words:
#     if word.lower() not in ["a", "e", "i", "o", "u"]:
#         name3.append(word) 

# print("".join(name3))

# #4 list (co? skąd? warunek? - inne skladnia przy else)

# name4 = [word for word in words if word.lower() not in ["a", "e", "i", "o", "u"]]

# print("".join(name4))

# #5 list przyklad 

# name5 = ["" if word.lower() in ["a", "e", "i", "o", "u"] else word for word in words]

# print("".join(name5))
