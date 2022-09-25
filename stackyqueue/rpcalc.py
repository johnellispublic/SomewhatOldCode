"""Command line Reverse-Polish Calculator

Commands:
    integer  - push an integer to the stack
    '+-*/^%' - apply the respective operator to the top 2 elements
    p        - print the top of the stack
    f        - print the whole stack
    q        - quits the command line
"""

from stack import Stack

def is_int(string):
    """Check if the string is an integer"""
    try:
        int(string)
        return True
    except ValueError:
        return False

class Calculator:
    """A reverse polish calculator"""
    def __init__(self, capacity=1024):
        self._stack = Stack(1024) # The stack of numbers
        self._error_happened = False # If an error has happened

    def __push(self, number):
        """Push a number to the stack"""
        try:
           self._stack.push(number)
        # If the stack is too full, handle it
        except IndexError:
            self._error_happened = True
            self.print('Stack Full')

    def __add(self):
        """Performs addition"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)

        # Pop 2 elements and push their sum
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(int(n1+n2))

    def __sub(self):
        """Performs subtraction"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)
        # Pop 2 elements and push their difference
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(int(n1-n2))

    def __mul(self):
        """Performs multiplilcation"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)
        # Pop 2 elements and push their product
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(int(n1*n2))

    def __div(self):
        """Performs division"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)

        # Check if division by zero
        elif self._stack.peek() == 0:
            self.print('Division By Zero')
            self._error_happened = True
        # Pop 2 elements and push their division
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(n1//n2)

    def __mod(self):
        """Performs modulo"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)

        # Check if modulo by zero
        elif self._stack.peek() == 0:
            self.print('Modulo By Zero')
            self._error_happened = True
        # Pop 2 elements and push their mod
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(int(n1%n2))

    def __exp(self):
        """Performs exponentiation"""
        # Check if the stack is empty or has only 1 element
        err_msg = self.__is_stack_too_empty()
        # Print the error message
        if err_msg:
            self.print(err_msg)

        # Pop 2 elements and push the first to the second
        else:
            n2 = self._stack.pop()
            n1 = self._stack.pop()
            self.__push(int(n1**n2))

    def print(self,value=None):
        """Prints the top of the stack or the variable in value"""

        if value is not None:
            print(value)
        # Ignore if the stack is empty
        elif self._stack.is_empty():
            pass
        else:
            print(self._stack.peek())

    def execute(self, command):
        """Executes a command"""
        # Reset if an error had happened
        self._error_happened = False

        # Checks if the command is a number and if it is, it pushes it to the stack
        if is_int(command):
            number = int(command)
            self.__push(number)

        # Performs the respective operation given the command
        elif command == '+':
            self.__add()
        elif command == '-':
            self.__sub()
        elif command == '*':
            self.__mul()
        elif command == '/':
            self.__div()
        elif command == '%':
            self.__mod()
        elif command == '^':
            self.__exp()
        elif command == 'p':
            self.print()
        elif command == 'f':
            self.print(' '.join([str(i) for i in self._stack]))
        else:
            # Otherwise raise an error
            self.print(f"Invalid command {command}")

    def __is_stack_too_empty(self):
        """Checks if the stack has 1 or 0 numbers in it"""
        # If it has none, give the respective error message
        if self._stack.is_empty():
            self._error_happened = True
            return 'Stack Empty'

        # If it has 1, give the respective rror message
        elif len(self._stack) == 1:
            self._error_happened = True
            return 'Stack Contains only 1 element'

        # Otherwise, return an empty string
        else:
            return ""

    def command_line(self):
        """Run the calculator on the command line"""
        while True:
            # Get the users input
            line = input("> ")
            # Seperate the commands
            for command in line.split():

                # quit if q is the command
                if command == 'q':
                    return

                # otherwise, execute it
                else:
                    self.execute(command)

if __name__ == '__main__':
    calc = Calculator()
    calc.command_line()
