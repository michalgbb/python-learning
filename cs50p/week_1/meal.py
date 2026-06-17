def main():
    time = input("What is it? ")
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("")

#Convert time to float time string to float time
def convert(a):
    h, m = a.split(":", 1)
    m = int(m)
    h = int(h)
    float_time = f"{h+(m/60)}"
    return float(float_time)

if __name__ == "__main__":
    main()