def chatbot():
    print("Welcome to the chatbot!")
while True:
        user_input = input("You: ")
        user_input = user_input.lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hello How can I assist you today?")
        elif "how are you" in user_input:
            print("Bot: I'm doing well, thanks for asking!")
        elif "what is your name" in user_input:
            print("Bot: My name is Chintu, nice to meet you!")
        elif "what is rectangle" in user_input:
            print("Bot:A rectangle is a geometric shape characterized by having four sides and four right angles. Its opposite sides are equal in length, and adjacent sides are perpendicular to each other")
        elif "what is circle" in user_input :
            print("Bot: The term 'circle' in short form refers to a shape consisting of all points in a plane that are at a given distance from a given point, known as the center!.")
        elif "quit" in user_input or "exit" in user_input:
            print("Bot: Goodbye It was nice chatting with you.")
            break
        else:
            print("Bot: Sorry, I didn't understand that. Please try again.")
if __name__ == "__main__":                                                                        
    chatbot()
