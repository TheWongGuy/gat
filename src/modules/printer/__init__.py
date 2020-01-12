from src.modules.color import Color

class Printer():
    @staticmethod
    def error(msg):
        print(Color.RED + Color.BOLD)
        print(msg)
        print(Color.END)

    @staticmethod
    def success(msg):
        print(Color.GREEN + Color.BOLD) 
        print(msg)
        print(Color.END)

    @staticmethod
    def important(msg):
        print(Color.BLUE + Color.BOLD) 
        print(msg)
        print(Color.END)
