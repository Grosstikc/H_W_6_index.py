def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            return f"Error: {e}"

    return wrapper


@input_error
def handle_hello():
    return "How can I help you?"


@input_error
def handle_add(contact_info, contacts):
    name, phone = contact_info.split()
    contacts[name] = phone
    return f"Contact {name} added successfully."


@input_error
def handle_change(contact_info, contacts):
    name, phone = contact_info.split()
    contacts[name] = phone
    return f"Phone number for {name} changed successfully."


@input_error
def handle_phone(contact_name, contacts):
    return contacts[contact_name]


@input_error
def handle_show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def main():
    contacts = {}
    while True:
        user_input = input("Enter a command: ").lower()

        if user_input == "good bye" or user_input == "close" or user_input == "exit":
            print("Good bye!")
            break

        if user_input == "hello":
            print(handle_hello())
        elif user_input.startswith("add"):
            print(handle_add(user_input[4:], contacts))
        elif user_input.startswith("change"):
            print(handle_change(user_input[7:], contacts))
        elif user_input.startswith("phone"):
            print(handle_phone(user_input[6:], contacts))
        elif user_input == "show all":
            print(handle_show_all(contacts))
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
