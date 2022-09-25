"""A Reverse-Polish Calculator implemented in Python and Tkinter

Variable Naming convention:
    calc     - the parent calculator
    window   - the window to a frame
    b[word]  - A button
    o[word]  - An output box
    l[word]  - A list
    sb[word] - A scrollbar

Keybinds:
0-9          - type numbers 0-9
+            - add
-            - subtract
*            - multiply
/            - divide
^            - raise to the power
%            - modulo
Shift-minus  - Toggle the input being negative
Enter        - submit
Backspace    - Delete last item in stack
Ctrl-C       - Clear the input field
Ctrl-Shift-C - Clear the stack

Display:
+--Main window----------------------+
|+---Stack-----+ +--Entry/Output---+|
||+-----------+| |           123321||
||| Cls | Del || +-----------------+|
||+-----------+| +-----------------+|
||element 1  |^| |+-------++------+||
||   .    2  | | || 7 8 9 || +  - |||
||   .    3  | | || 4 5 6 || *  / |||
||   .    4  | | || 1 2 3 || %  ^ |||
||           | | || C 0 ↵ ||(-)   |||
||           |v| |+-------++------+||
|+-------------+ +-----------------+|
+-----------------------------------+
"""

from tkinter import *
from rpcalc import Calculator

MAX_LINE_LEN = 80

class NumberButtons(Frame):
    """The Buttons to input the numbers"""
    def __init__(self, calculator, window):
        super().__init__(window) # Make a frame
        self.__calc = calculator # The parent calculator object
        self.__window = window # The window the frame is in

        #The numbers 0-9
        self.__b0 = Button(self, text='0', command=lambda:self.__calc.enter_number('0'))
        self.__b1 = Button(self, text='1', command=lambda:self.__calc.enter_number('1'))
        self.__b2 = Button(self, text='2', command=lambda:self.__calc.enter_number('2'))
        self.__b3 = Button(self, text='3', command=lambda:self.__calc.enter_number('3'))
        self.__b4 = Button(self, text='4', command=lambda:self.__calc.enter_number('4'))
        self.__b5 = Button(self, text='5', command=lambda:self.__calc.enter_number('5'))
        self.__b6 = Button(self, text='6', command=lambda:self.__calc.enter_number('6'))
        self.__b7 = Button(self, text='7', command=lambda:self.__calc.enter_number('7'))
        self.__b8 = Button(self, text='8', command=lambda:self.__calc.enter_number('8'))
        self.__b9 = Button(self, text='9', command=lambda:self.__calc.enter_number('9'))

        # Clear input button
        self.__bC = Button(self, text='C', command=lambda:self.__calc.clear_input())

        # Enter button
        self.__bE = Button(self, text='↵', command=lambda:self.__calc.execute(''))

        # Grid them
        self.__b0.grid(column=1,row=3)
        self.__b1.grid(column=0,row=2)
        self.__b2.grid(column=1,row=2)
        self.__b3.grid(column=2,row=2)
        self.__b4.grid(column=0,row=1)
        self.__b5.grid(column=1,row=1)
        self.__b6.grid(column=2,row=1)
        self.__b7.grid(column=0,row=0)
        self.__b8.grid(column=1,row=0)
        self.__b9.grid(column=2,row=0)

        self.__bC.grid(column=0,row=3)
        self.__bE.grid(column=2,row=3)


class OperatorButtons(Frame):
    """The buttons to execute operators"""
    def __init__(self, calculator, window):
        super().__init__(window) # Make a frame
        self.__calc = calculator # The parent calculator object
        self.__window = window # The window the frame is in

        # The operator buttons
        self.__badd = Button(self, text=' + ', command=lambda:self.__calc.execute('+'))
        self.__bsub = Button(self, text=' - ', command=lambda:self.__calc.execute('-'))
        self.__bmul = Button(self, text=' * ', command=lambda:self.__calc.execute('*'))
        self.__bdiv = Button(self, text=' / ', command=lambda:self.__calc.execute('/'))
        self.__bmod = Button(self, text=' % ', command=lambda:self.__calc.execute('%'))
        self.__bexp = Button(self, text=' ^ ', command=lambda:self.__calc.execute('^'))
        self.__bmin = Button(self, text='(-)', command=lambda:self.__calc.toggle_number_negative())

        self.__badd.grid(column=0, row=0)
        self.__bsub.grid(column=1, row=0)
        self.__bmul.grid(column=0, row=1)
        self.__bdiv.grid(column=1, row=1)
        self.__bmod.grid(column=0, row=2)
        self.__bexp.grid(column=1, row=2)
        self.__bmin.grid(column=0, row=3)


class OutField(LabelFrame):
    """The output box (also displays numbers while they are not yet entered)"""
    def __init__(self, window):
        super().__init__(window) # Initiate the frame

        # Create the output box
        self.__obox = Label(self, text='Press Any Key', anchor=E, justify=LEFT, relief=RIDGE)

        # Pack it as it needs to expand
        self.__obox.pack(fill=X,expand=True)

    def set_text(self, text):
        """Sets the text of the box to `text`"""

        text = str(text) # Allows splicing
        if len(text) > MAX_LINE_LEN:
            # Split the text into lines `MAX_LINE_LEN` long
            text = [text[i:i+MAX_LINE_LEN] for i in range(0, len(text),MAX_LINE_LEN)]

            # Join the lines with newlines
            text = '\n'.join(text)

        # Set the text in the output box to text
        self.__obox['text'] = text


class StackDisplay(Frame):
    """Displays the contents of the stack used in the rp calculator"""
    def __init__(self, calculator, window):
        super().__init__(window) # Make a frame
        self.__calc = calculator # The parent calculator object
        self.__window = window # The window the frame is in

        self.__lstack = Listbox(self) # The list of items in the stack
        self.__sbstack = Scrollbar(self) # The scrollbar for that list

        # The buttons used in the stack
        # Clear:  Clears the stack
        # Delete: Removes the item at the top of the stack
        self.__stack_display_buttons = Frame(self)
        self.__bclear_stack = Button(self.__stack_display_buttons, text='Clear', command=lambda:self.__calc.clear_stack())
        self.__bdelete_prev = Button(self.__stack_display_buttons, text='Delete', command=lambda:self.__calc.del_top())

        # Configure the scrollbar
        self.__lstack.config(yscrollcommand=self.__sbstack.set)
        self.__sbstack.config(command=self.__lstack.yview)

        # Pack items so filling can be done
        self.__bclear_stack.pack(side=LEFT)
        self.__bdelete_prev.pack(side=RIGHT)
        self.__stack_display_buttons.pack(side=TOP)
        self.__sbstack.pack(side=RIGHT, fill=Y)
        self.__lstack.pack(side=LEFT, fill=BOTH)

    def set_data(self, data):
        self.__lstack.delete(0,END)
        for i in range(len(data)):
            self.__lstack.insert(i, data[i])


class TkinerCalculator(Calculator):
    """The Reverse-Polish Calculator object (tkinter variant)"""
    def __init__(self):
        self.__window = Tk() # Create a new window

        self.__number_to_enter = '' # The number about to be entered
        self.__started_typing = False # Whether the user has started typing

        self.__create_buttons() # Create the buttons

        # Allows the user to use the keyboard instead of the buttons
        self.__window.bind('<Key>', self.__handle_keyboard_input)

        # Create the calculator
        super().__init__()

    def __create_buttons(self):
        self.__button_frame = Frame(self.__window) # The frame for all the buttons

        # The numbers 0-9 and clear input/enter
        self.__number_buttons = NumberButtons(self, self.__button_frame)

        # The operators
        self.__operator_buttons = OperatorButtons(self, self.__button_frame)

        # The output display / display for numbers while they are being entered
        self.__display = OutField(self.__window)

        # The display for the stack
        self.__stack_display = StackDisplay(self,self.__window)

        # Grid the buttons such that they are next to each other
        self.__number_buttons.grid(column=0,row=0)
        self.__operator_buttons.grid(column=1,row=0)

        # Pack Everything in the main window so that fill can be used
        self.__stack_display.pack(side=LEFT, fill=BOTH)
        self.__display.pack(side=TOP, fill=X)
        self.__button_frame.pack(side=TOP)


    def __handle_keyboard_input(self, event):
        """Handles when the user presses a key

        Keybinds:
        0-9          - type numbers 0-9
        +            - add
        -            - subtract
        *            - multiply
        /            - divide
        ^            - raise to the power
        %            - modulo
        Shift-minus  - Toggle the input being negative
        Enter        - submit
        Backspace    - Delete last item in stack
        Ctrl-C       - Clear the input field
        Ctrl-Shift-C - Clear the stack
        """
        # Handles the case where event.char is empty (such as a mouse button press)
        if event.char == '':
            return

        # If the c key is pressed while the control key (0b100) is pressed
        if event.keysym == 'c' and event.state & 4:
            self.clear_input()

        # If shift+c (capital C) is pressed while the control key is
        elif event.keysym == 'C' and event.state & 4:
            self.clear_stack()
        # If a number key (main keyboard or numpad) is pressed
        elif event.char.isnumeric() and event.char.isascii():
            self.enter_number(event.char)
        # If an operator key is pressed
        elif event.char in '+-*/^%':
            self.execute(event.char)

        # If an enter key is pressed (carriage return or newline)
        elif event.char in '\r\n':
            self.execute('')

        # If the backspace key is pressed
        elif event.char in '\b':
            self.del_top()

        # If shift-Minus is pressed
        elif event.char in '_':
            self.toggle_number_negative()


    def enter_number(self, num):
        """Append a digit to the input field"""
        self.__number_to_enter += num
        self.__started_typing = True # set it so the user has started typing
        self.print() # Output the new number

    def toggle_number_negative(self):
        """Make the number negative"""

        # Multiply it by -1
        self.__number_to_enter = int(self.__number_to_enter)
        self.__number_to_enter *= -1
        self.__number_to_enter = str(self.__number_to_enter)
        self.print()

    def clear_input(self):
        """Clear the input field"""
        self.__number_to_enter = '' # Reset the number to enter
        self.__started_typing = True # Set it so the user has started typing
        self.print() # Update the display

    def execute(self, command):
        """Execute a command"""
        if self.__number_to_enter:
            # If the has entered a number, add it to the stack and clear the input
            super().execute(self.__number_to_enter)
            self.clear_input()

        # Execute the command and reset `__started_typing`
        self.__started_typing = False
        super().execute(command)

        # If an error has not happened update the display
        #   This is because the error handling already outputs the message
        #   to the display. If the display was updated now, it would overwrite
        #   the message.
        if not self._error_happened:
            self.print()

        # Update the stack
        self.__stack_display.set_data(list(self._stack))

    def print(self, text=None):
        """Print a message or update the display"""
        # If a pre-determined message is sent, set the output to that message
        if text is not None:
            self.__display.set_text(text)

        # If the user has started typing, display the number
        elif self.__started_typing:
            self.__display.set_text(self.__number_to_enter)

        # Otherwise, give the item at the top of the stack
        else:
            if not self._stack.is_empty():
                self.__display.set_text(self._stack.peek())
            else:
                self.__display.set_text('')

    def clear_stack(self):
        """Clears the stack"""

        # Pop until an empty stack.
        while not self._stack.is_empty():
            self._stack.pop()

        # Update the display
        self.print()

        # Update the stack display (it will be empty so an empty list is used)
        self.__stack_display.set_data([])

    def del_top(self):
        """Remove the item from the top of the stack"""

        # Do nothing if the stack is empty
        if not self._stack.is_empty():
            self._stack.pop()

        # Update the display and the stack display
        self.print()
        self.__stack_display.set_data(list(self._stack))

    def run(self):
        """Run the tkinter widget"""
        self.__window.mainloop()

if __name__ == '__main__':
    calc = TkinerCalculator()
    calc.run()
