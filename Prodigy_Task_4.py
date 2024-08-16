import os

def get_filename():
    """Prompts the user for a filename and ensures it's valid."""
    while True:
        filename = input("Enter the filename for logging (e.g., log.txt): ").strip()
        if filename:
            return filename
        print("Filename cannot be empty. Please try again.")

def log_user_input(filename):
    """
    Logs user input to a specified file.

    Parameters:
        filename (str): The name of the file where input will be logged.
    """
    if os.path.exists(filename):
        append_mode = input(f"File '{filename}' already exists. Append to it? (y/n): ").strip().lower()
        if append_mode not in ['y', 'yes']:
            print("Exiting without logging.")
            return
    
    print("Starting input logger. Type 'exit' to end.")
    try:
        with open(filename, 'a') as file:
            while True:
                user_input = input("Enter text: ")
                if user_input.lower() == 'exit':
                    break
                file.write(user_input + '\n')
                print("Input logged.")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    """
    Main function to run the input logger.
    """
    filename = get_filename()
    log_user_input(filename)
    print(f"Logging complete. Data saved to {filename}.")

if __name__ == "__main__":
    main()
