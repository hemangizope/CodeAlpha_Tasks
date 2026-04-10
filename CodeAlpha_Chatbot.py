def chatbot():
    print("--- Welcome to the Rule-Bot! (Type 'bye' to exit) ---")
    
    while True:
        # 1. Get input from the user and normalize it (lowercase)
        user_input = input("You: ").lower().strip()

        # 2. Define the logic (Rules)
        if user_input == "hello" or user_input == "hi":
            print("Chatbot: Hi!")
        
        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break  # Exit the loop to end the program
        
        else:
            print("Chatbot: I'm sorry, I don't understand that yet.")

# 3. Call the function to start
chatbot()