def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, KeyError, IndexError) as e:
            print(e)
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Please provide both a name and a phone number.")
    name, phone = args
    contacts[name] = phone
    print(f"Contact added.")

@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise ValueError("Please provide both a name and a phone number.")
    name, phone = args
    if name not in contacts:
        raise KeyError(f"Name '{name}' not found in contacts.")
    contacts[name] = phone
    print(f"Contact updated.")

@input_error
def show_phone(args, contacts):
    if len(args) < 1:
        raise IndexError("Please provide a name.")
    name = args[0]
    if name not in contacts:
        raise KeyError(f"Name '{name}' not found in contacts.")
    print(f"{contacts[name]}")

def show_all(contacts):
    if contacts:
        print("Contacts list:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("Contact list is empty.")

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            add_contact(args, contacts)
        elif command == "change":
            change_contact(args, contacts)
        elif command == "phone":
            show_phone(args, contacts)
        elif command == "all":
            show_all(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
