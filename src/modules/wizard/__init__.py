from src.modules.color import Color
from yaspin import yaspin
import json
import os

class Wizard:
    config_path = ""
    USER = ""

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

    def write_config(self):
        config = {
            'USER': self.USER,
        }
        with yaspin(text="Creating config...", color="yellow") as spinner:
            try:
                if not os.path.exists(self.config_path):
                    os.makedirs(os.path.dirname(self.config_path))
                f = open(self.config_path, 'w')  
                f.write(json.dumps(config))
                f.close()
                spinner.ok("✅ ")
            except Exception as e:
                spinner.fail("❌ ")
                print(Color.RED + Color.BOLD)
                print(e)
                print(Color.END)