CHOICES = ["Add", "Subtract", "Multiply","Integer Division","Quit"] #The operations to choose from
POSSIBLE_USER_CHOICES = ['A','S','M','D','Q'] #The values the user can chose

def display_choices(CHOICES,POSSIBLE_USER_CHOICES):
    print()
    for choice in range(len(CHOICES)):
        print(f"{POSSIBLE_USER_CHOICES[choice]}) {CHOICES[choice]}")

def is_invalid(choice,POSSIBLE_USER_CHOICES=[],is_str=False):
    try:
        if not is_str:
            choice = float(choice)
    except ValueError:
        return f"{choice} is an invalid number."

    else:
        if len(POSSIBLE_USER_CHOICES) == 0:
            return ""

        elif choice in POSSIBLE_USER_CHOICES:
            return ""
        elif not is_str and 1 <= choice <= len(POSSIBLE_USER_CHOICES):
            return ""

        elif is_str:
            return f"{choice} is not in {POSSIBLE_USER_CHOICES}"
        else:
            return f"{choice} is not between 1 and {len(CHOICES)}"


def get_valid_choice(CHOICES):
    while True:
        choice = input("Enter number: ")
        choice = choice.upper()

        error = is_invalid(choice,POSSIBLE_USER_CHOICES,True)
        if error:
            print(error)
        else:
            return choice


def get_operand(n):

    while True:
        op = input(f"{n}) Enter number: ")

        error = is_invalid(op)

        if error:
            print(error)
        else:
            op = float(op)
            return op


def get_two_operands():
    return get_operand(1), get_operand(2)

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def do_integer_division(a,b):
    return a//b

def display_result(result):
    print(result)

def main():
    while True:
        display_choices(CHOICES,POSSIBLE_USER_CHOICES)
        choice = get_valid_choice(CHOICES)
        a,b = get_two_operands()

        if choice == 'A':
            result = add(a,b)
        elif choice == 'S':
            result = subtract(a,b)
        elif choice == 'M':
            result = multiply(a,b)
        elif choice == 'D':
            result = do_integer_division(a,b)
        elif choice == 'Q':
            return

        display_result(result)


main()
