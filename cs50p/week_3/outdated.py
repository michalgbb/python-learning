def main():

    print("mm/dd/yyyy or Month Day, Year")
    get_date()

def get_date():

    month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    while True:

        x = input("Date: ")

        try:
            if "/" in x:
                m, d, y = x.split("/")
                m, d, y = int(m), int(d), int(y)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    break
                
                
            elif "," in x:
                m, d, y = x.split(" ")
                d = d.replace(",", "")
                if m in month:
                    m = month.index(m) + 1
                    m, d, y = int(m), int(d), int(y)
                    if 1 <= m <= 12 and 1 <= d <= 31: 
                        break
        
        except ValueError:
            pass


    print(f"{y}-{m:02}-{d:02}")            

main()