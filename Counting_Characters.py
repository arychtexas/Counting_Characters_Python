#Counting_Characters 

# Prompt the user for input
user_input = input("Enter your text: ")

# Check if the input is empty
if not user_input:
    print("You entered nothing. Please try again.")
else:
    # Calculate the total number of characters
    character_count = len(user_input)

# Display the result
print(f"The character count is {character_count}.")
