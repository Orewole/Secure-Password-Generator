import random
import string

def build_character_pool(include_symbols):
    """
    Constructs the list of available characters based on configuration.
    Matches SDLC Phase 2: Component Design.
    """
    # always include letters and numbers
    pool = string.ascii_letters + string.digits
    
    if include_symbols:
        pool += string.punctuation
        
    return pool

def generate_secure_token(length, include_symbols):
    """
    The core logic engine that samples the pool.
    Matches SDLC Phase 2: Component Design.
    """
    character_set = build_character_pool(include_symbols)
    
    # Create a list of random choices and join them into a string
    token = ''.join(random.choice(character_set) for _ in range(length))
    return token

def runtime_interface():
    """
    The user interaction loop.
    Matches SDLC Phase 2: Component Design.
    """
    print("--- PyGen-Secure: Credential Generator ---")
    
    while True:
        try:
            # Input Handling
            len_input = input("\n[?] Enter desired password length (e.g., 12): ")
            length = int(len_input)
            
            if length <= 0:
                print("Error: Length must be greater than 0.")
                continue

            # Complexity Toggle
            sym_input = input("[?] Include special symbols? (y/n): ").lower()
            use_symbols = True if sym_input == 'y' else False

            # Generation
            password = generate_secure_token(length, use_symbols)
            
            # Output
            print(f"\n[RESULT] Your secure password is:  {password}")
            
            # Exit Check
            again = input("\nGenerate another? (y/n): ").lower()
            if again != 'y':
                print("Session terminated. Stay secure.")
                break

        except ValueError:
            # Matches SDLC Phase 3: Error Handling
            print("(!) Error: Please enter a valid number for length.")

if __name__ == "__main__":
    runtime_interface()
