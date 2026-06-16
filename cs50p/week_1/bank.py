msg = input("Greeting: ")

match msg.strip():
    case "Hello" | "Hello, Newman":
        print("$0")
    case "How you doing?":
        print("$20")
    case "What's happening?" | "What's up?":
        print("$100")