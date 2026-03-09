print("🤖 ChatBot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("🤖 ChatBot: Hi there! How can I help you?")
    
    elif "how are you" in user_input:
        print("🤖 ChatBot: I'm just a program, but I'm doing great!")

    elif "your name" in user_input:
        print("🤖 ChatBot: I am a simple Python chatbot.")

    elif "help" in user_input:
        print("🤖 ChatBot: I can respond to greetings and simple questions.")

    elif user_input == "bye":
        print("🤖 ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that.")