from src.modules.color import Color
from yaspin import yaspin
from src.modules.printer import Printer
import json
import os

class Wizard:
    config_path = ""
    USER = ""
    config = {}

    def __init__(self, config_path):
        self.config_path = os.path.expanduser(config_path)

    def setup(self):
        self.USER = input(Color.BOLD + "Enter your default user: " + Color.END)

    def confirm(self):
        print("\n")
        # Add other confirmations here
        print("USER -> " + Color.GREEN + self.USER + Color.END)
        #
        input("\n" + Color.BOLD + "Press enter to create file..." + Color.END)
        self.config = {
            'USER': self.USER,
        }

    def write_config(self):
        with yaspin(text="Creating config...", color="yellow") as spinner:
            try:
                if not os.path.exists(os.path.dirname(self.config_path)):
                    os.makedirs(os.path.dirname(self.config_path))
                f = open(self.config_path, 'w')  
                f.write(json.dumps(self.config))
                f.close()
                spinner.ok("✅ ")
            except Exception as e:
                spinner.fail("❌ ")
                Printer.error(e)

    def read_config(self):
        try:
            f = open(self.config_path, 'r')
            self.config = json.loads(f.read())
            f.close()
        except Exception as e:
                Printer.error(e)

    def get_config(self):
        return self.config