# ChatbotAI

This program is a simple chatbot implemented in Python. The chatbot responds to user inputs based on predefined patterns and generates appropriate responses.
The program begins by importing the random and re modules. The random module is used to randomly select a response when a pattern does not match, and the re module is used for pattern matching.
Next, two lists are defined: user_inputs and bot_responses. These lists contain a series of predefined patterns and their corresponding responses. 
The generate_response function takes a user input as a parameter. It loops through each pattern in the user_inputs list and checks if it matches the user input using the re.search method. If it finds a match, it returns the corresponding response from the bot_responses list. If no match is found, it randomly selects a response from a default list.
The program then enters a while loop which continues indefinitely until the user enters a "bye", "goodbye", or "exit" message. Inside the loop, the program prompts the user for input using the input function.
If the user input matches any of the "bye", "goodbye", or "exit" patterns using the re.search method, the program prints "Bot: Goodbye!" and exits the loop.
If the user input does not match any of the exit patterns, the program calls the generate_response function with the user input as an argument. 
The generated response is then printed preceded by "Bot:".
