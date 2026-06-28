# ==========================================
# Rule-Based AI Chatbot
# ==========================================

from colorama import Fore, Style, init # type: ignore

# Initialize Colorama
init(autoreset=True)

# Function to print chatbot responses
def chatbot(message):
    print(Fore.BLUE + "Chatbot: " + Style.RESET_ALL + message)

# Welcome Message
print(Fore.CYAN + "=" * 55)
print(Fore.CYAN + "         🤖 WELCOME TO AI CHATBOT 🤖")
print(Fore.CYAN + "=" * 55)

print("\nHello! I am a Rule-Based AI Chatbot.")
print("You can ask me simple questions.")
print("Type 'help' to see available commands.")
print("Type 'bye' or 'exit' to end the chat.\n")

# Chat Loop
while True:

    # User Input
    user = input(Fore.GREEN + "You: " + Style.RESET_ALL).lower().strip()

    # Greetings
    if user == "hello" or user == "hi":
        chatbot("Hello! Nice to meet you! How can I help you today?")
        

    elif user == "good morning":
        chatbot("Good Morning! Have a wonderful day.")

    elif user == "good afternoon":
        chatbot("Good Afternoon!")

    elif user == "good evening":
        chatbot("Good Evening!")

    # General Questions
    elif user == "how are you":
        chatbot("I am doing great!")
        chatbot("Thank you for asking.")

    elif user == "what is your name":
        chatbot("My name is Rule-Based AI Chatbot.")

    elif user == "who made you":
        chatbot("I was created using Python programming.")

    elif user == "where do you live":
        chatbot("I live inside your computer.")

    elif user == "who are you":
        chatbot("I am your Rule-Based AI assistant.")

    elif user == "what can you do":
        chatbot("I can answer simple predefined questions using if-else statements.")

    # Programming
    elif user == "python":
        chatbot("Python is an easy and powerful programming language.")

    elif user == "java":
        chatbot("Java is an object-oriented programming language.")

    elif user == "c++":
        chatbot("C++ is widely used for software and game development.")

    elif user == "ai":
        chatbot("AI stands for Artificial Intelligence. AI is the development of computer systems \n capable of performing tasks that typically require human intelligence.")

    elif user == "machine learning":
        chatbot("Machine Learning enables computers to learn from data.")

    elif user == "chatbot":
        chatbot("A chatbot is software that communicates with users.")

    # Conversation
    elif user == "thanks" or user == "thank you":
        chatbot("You're welcome!")

    elif user == "yes":
        chatbot("Great!")

    elif user == "no":
        chatbot("Okay, no problem.")

    elif user == "time":
        chatbot("Sorry, I cannot tell the current time.")

    elif user == "date":
        chatbot("Sorry, I cannot tell today's date.")

    # Help Menu
    elif user == "help":
        chatbot("You can ask the following questions:")
        print("""
1. hello
2. hi
3. good morning
4. good afternoon
5. good evening
6. how are you
7. what is your name
8. who made you
9. where do you live
10. who are you
11. what can you do
12. python
13. java
14. c++
15. ai
16. machine learning
17. chatbot
18. time
19. date
20. thanks
21. bye
22. exit
""")

    # Exit
    elif user == "bye":
        chatbot("Goodbye! Have a wonderful day.")
        break

    elif user == "exit":
        chatbot("Chat ended successfully.")
        break

    # Unknown Input
    else:
        chatbot("Sorry, I don't understand that.")
        chatbot("Type 'help' to see available commands.")