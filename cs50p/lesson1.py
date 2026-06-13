# Zapytaj uzytkownika o imie
name = input("Jak masz na imie? ") 

#usun psute znaki i powieksz litery imienia i nazwiska
name = name.strip().title()

#Przywitaj uzytkownika
print(f"Witaj, {name}")
