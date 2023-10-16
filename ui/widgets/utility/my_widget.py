from PyQt5.QtWidgets import QWidget


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.class_list = {}

    # Add class to the class list
    def set_class(self, my_class_string: str):
        for my_class in my_class_string.split():
            self.class_list[my_class] = True
        self.reset_style()

    # Toggle class state
    def toggle_class(self, my_class, new_value=None, with_reset=True):
        if my_class in self.class_list.keys():
            if new_value is None:
                self.class_list[my_class] = not self.class_list[my_class]
            else:
                self.class_list[my_class] = new_value
        else:
            self.class_list[my_class] = True
        if with_reset:
            self.reset_style()

    # Remove class from the class list
    def remove_class(self, my_class):
        if my_class in self.class_list.keys():
            self.class_list.pop(my_class)
            self.reset_style()

    #
    def remove_all_classes(self):
        self.class_list.clear()
        self.reset_style()

    # Set "class" property
    def reset_style(self):
        separator = " "
        my_classes = separator.join([my_class for my_class, is_toggled in self.class_list.items() if is_toggled])
        self.setProperty("class", my_classes)
        self.setStyleSheet("")


