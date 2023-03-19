import config
import model


class MenuDisplay:
    @staticmethod
    def display(option):
        print(f"{config.SEPARATOR}\nTODO LIST\n{config.SEPARATOR}"
              f"\nThe following commands are available: ")
        for key, value in option.items():
            print(f"{key}. {value}")


class DisplayItems:
    @staticmethod
    def display():
        counter = 0
        items = model.Model.get_items()

        if len(items) == 0:
            print(f"{config.SEPARATOR}\nTodo list is empty!")
        else:
            print(f"{config.SEPARATOR}\nTODO LIST")
            print(f"{config.SEPARATOR}\n#. Title - Description")
            for item in items:
                counter += 1
                print(f"{counter}. {item[1]} - {item[2]}")


class DisplayAddItem:
    @staticmethod
    def display():
        title = model.Model.add_item()
        if title:
            print(f'New todo "{title}" has been added!')


class DisplayModifyItem:
    @staticmethod
    def display():
        title = model.Model.modify_item()
        if title:
            print(f"Todo list has been updated!")


class DisplayDeleteItem:
    @staticmethod
    def display():
        title = model.Model.delete_item()
        if title:
            print(f'Todo "{title}" has been deleted!')
