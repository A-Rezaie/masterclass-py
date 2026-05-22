def main():
    """
    This program checks whether a given string is a palindrome.

    It ignores uppercase/lowercase differences and spaces.
    The user can check multiple strings until they choose to stop.
    """
  
    running = True
    
    while running:
        user_input = input("Enter your sample(string): ").strip().lower()
        normalized_input = user_input.replace(" ", "")
    
        if normalized_input == "":
            print("Input cannot be empty.")
            continue
    
        inverse_user_input = normalized_input[::-1]
    
        if normalized_input == inverse_user_input:
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
        
        while True:
            user_response = input("Do you want to check another string? (yes/no): ").strip().lower()
    
            if user_response in ["yes", "y"]:
                break
            elif user_response in ["no", "n"]:
                running = False
                break
            else:
                print("Invalid response. Please enter yes/y or no/n.")


if __name__ == "__main__":
    main()
