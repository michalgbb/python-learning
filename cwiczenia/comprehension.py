def save_counts(slownik):
    print("Wynik końcowy słownika:", slownik)

def main():

#  # comprehesion 

    counts = {}
    words = ["pies", "kot", "Pies", "ptak", "kot", "pies"]
    #nowa lista z malymi literami
    lowercase_words = [word.lower() for word in words] 
    for word in lowercase_words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    save_counts(counts)


# #comprehesion dictionary

#     words = ["pies", "kot", "Pies", "ptak", "kot", "pies"]
#     #nowa lista z malymi literami
#     lowercase_words = [word.lower() for word in words] 
    
#     counts = {word: lowercase_words.count(word) for word in lowercase_words}

#     save_counts(counts)



main()    