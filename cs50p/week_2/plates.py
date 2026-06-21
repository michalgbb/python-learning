def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    count = False
    
    if len(s) >= 2 and len(s) <= 6 and s[0:2].isalpha() and s.isalnum():   
        
        for letter in s:
            # Sprawdzamy zero i jezeli wystepuje zmieniamy przelącznik
            if letter == "0" and count == False:
                count = True
                return False
            # Pojawienie się liczby i włączenie przełącznika
            elif letter.isdigit():
                count = True
            # Pojawienie się litery włączonym przełączniku (liczbie)
            elif letter.isalpha() and count == True:
                return False         
        
        return True       
   
    return False

#     def is_valid(s):

#     if 2 <= len(s) <= 6 and s[0:2].isalpha() and s[2:6].isalnum() and s[2] != "0":
# # For 6 letters        
#         if  len(s) == 6 and (s[2].isdigit() or s[3].isdigit() or s[4].isdigit()) and s[5].isalpha():
#             return False
#         elif  len(s) == 6 and (s[2].isdigit() or s[3].isdigit()) and s[4].isalpha():
#             return False
#         elif  len(s) == 6 and s[2].isdigit() and s[3].isalpha():
#             return False
# # For 5 letters
#         elif len(s) == 5 and (s[2].isdigit() or s[3].isdigit()) and s[4].isalpha():
#             return False
        
#         elif len(s) == 5 and s[2].isdigit() and s[3].isalpha() and s[4].isdigit():
#             return False
# # For 4 letters
#         elif len(s) == 4 and s[2].isdigit() and s[3].isalpha():
#             return False
#         else:
#             return True           
#     else:
#         return False


main()

