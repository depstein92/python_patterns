'''

Decorator pattern allows a user to add new functionality to an existing object without altering its structure. 
This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.

!- This pattern creates a decorator class which wraps the original class and provides additional 
   functionality keeping class methods signature intact

Decorator Design Pattern != Python decorator/function wrapper

Main reasons to use a decorator pattern:
- I want to change the behavior of a class, without changing
the class itself
'''

class WindowInterface:
    def build(self): pass


class AbstractWindowDecorator(WindowInterface):
    """
    Maintain a reference to a Window object and define an interface
    that conforms to Window's interface.
    """

    def __init__(self, window):
        self._window = window

    def build(self): pass


class Window(WindowInterface):
    def build(self):
        print("Building window")


class BorderDecorator(AbstractWindowDecorator):
    def add_border(self):
        print("Adding border")

    def build(self):
        self.add_border()
        self._window.build()


class VerticalSBDecorator(AbstractWindowDecorator):
    def add_vertical_scroll_bar(self):
        print("Adding vertical scroll bar")

    def build(self):
        self.add_vertical_scroll_bar()
        self._window.build()


class HorizontalSBDecorator(AbstractWindowDecorator):
    def add_horizontal_scroll_bar(self):
        print("Adding horizontal scroll bar")

    def build(self):
        self.add_horizontal_scroll_bar()
        self._window.build()
        
#=========Enact Decorator Pattern==============

w = Window()
w.build()

wb = BorderDecorator(w) # changes behavior of w 
wb.build()

wbv = VerticalSBDecorator(wb) # changes behavior of w
wb.build()
        