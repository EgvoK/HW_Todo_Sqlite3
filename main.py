from controller import Controller


class Main:
    @staticmethod
    def start():
        controller = Controller()
        controller.menu()


if __name__ == "__main__":
    app = Main()
    app.start()
