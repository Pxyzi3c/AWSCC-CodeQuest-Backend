import input_types

shopping_list = []

ACTIONS = {
    1: ("Add item to the shopping list", "ADD_ITEM"),
    2: ("View shopping list", "VIEW"),
    3: ("Remove item from the shopping list", "REMOVE"),
    4: ("Quit", "QUIT"),
}

def to_bool(answer):
    if answer.lower() == 'y':
        return True
    elif answer.lower() == 'n':
        return False
    else:
        return answer.lower()

def validate_input(input_type, user_input):
    if input_type == input_types.SELECTED_OPTION:
        try:
            user_input = int(user_input)
            ACTIONS[user_input]
            return user_input;
        except ValueError:
            print("Invalid value!")
            return None
        except KeyError:
            print("Selected option is not on the list!")
    elif input_type == input_types.BOOLEAN_OPTION:
        if isinstance(user_input, bool):
            return user_input
        else:
            return print("Answer must be 'y' or 'n'!")
    elif input_type == input_types.REMOVE_ITEM or input_type == input_types.ADD_ITEM:
        return user_input in shopping_list
        
def add_item(item):
    validated_input = validate_input(input_types.ADD_ITEM, item)
    if not validated_input:
        shopping_list.append(item)
        print(f"{item} has been added to your shopping list.")
    else:
        print(f"{item} is already on the list.")

def view():
    print("Your shopping list:")
    for item in shopping_list:
        print(item)

def remove_item(item):
    validated_input = validate_input(input_types.REMOVE_ITEM, item)
    if validated_input:
        shopping_list.remove(item)
        print(f"{item} has been removed to your shopping list.")
    else:
        print("Item is not on the list! Please try again.")

def quit_program():
    print("Goodbye!")
    exit()

def evaluate(user_input):
    OPTION_VALS = {}
    for key, value in ACTIONS.items():
        instruction, label = value
        OPTION_VALS[label] = key

    if user_input == OPTION_VALS["ADD_ITEM"]:
        add_item(input("Enter the item you want to add: "))
    elif user_input == OPTION_VALS["VIEW"]:
        view()
    elif user_input == OPTION_VALS["REMOVE"]:
        remove_item(input("Enter the item you want to remove: "))
    elif user_input == OPTION_VALS["QUIT"]:
        quit_program()

def start():
    print("OPTIONS:")

    for key, value in ACTIONS.items():
        instruction, label = value
        print(f"{key}. {instruction}")

    while True:
        selected_option = validate_input(input_types.SELECTED_OPTION, input("Enter the number of your choice: "))

        evaluate(selected_option)
        
        if not validate_input(input_types.BOOLEAN_OPTION, to_bool(input("Continue [y/n]? "))):
            break

start()