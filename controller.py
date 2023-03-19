import enum

import config
import view
from model import Model


class EnumMenu(enum.Enum):
    ShowTodoList = '1'
    AddItem = '2'
    ModifyItem = '3'
    DeleteItem = '4'
    Exit = '0'


def get_option():
    option = input("\nEnter the option number: ")
    return option


class Controller:
    def __init__(self):
        self.model = Model()
        self.options = config.OPTIONS

    def show_menu(self):
        view.MenuDisplay.display(self.options)

    def menu(self):
        self.show_menu()

        while True:
            option = get_option()
            match option:
                case EnumMenu.ShowTodoList.value:
                    view.DisplayItems.display()
                    self.show_menu()

                case EnumMenu.AddItem.value:
                    view.DisplayAddItem.display()
                    self.show_menu()

                case EnumMenu.ModifyItem.value:
                    view.DisplayModifyItem.display()
                    self.show_menu()

                case EnumMenu.DeleteItem.value:
                    view.DisplayDeleteItem.display()
                    self.show_menu()

                case EnumMenu.Exit.value:
                    print(f"{config.SEPARATOR}\nExit...")
                    break

                case _:
                    print(f"{config.SEPARATOR}\nIncorrect option! Try again!")
