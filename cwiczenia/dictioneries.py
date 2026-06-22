spacecraft = {"name": "Moon", "distance": "384 400"}

print(spacecraft)
#wyswietla konkrtena wartosc
print(spacecraft["name"])
#dodaje kolejny klucz + wartość
spacecraft["color"] = "white"
#wyświetla cały słownik - dict
print(spacecraft)
print(spacecraft.keys())
print(spacecraft.values())


# for name in spacecraft:
#     print(name)


for n in spacecraft.keys():
    print(f"{n} key<--->value {spacecraft[n]}")


for n in spacecraft:
    print(n)    