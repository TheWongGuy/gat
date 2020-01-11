import sys, os
from src.modules.color import Color

GAT_CONFIG = '~/.gat/config'

# Preform initial check of ~/.gatconfig file
def config_check(config: str):
    if not (os.path.isfile(GAT_CONFIG)):
        print("Looks like " + Color.GREEN + Color.BOLD + GAT_CONFIG +  Color.END  + " doesn't exist.")
        response = input(Color.BOLD + "Would you like us to help you set it up? (Y/N): " + Color.END)
        if(response.upper() != 'Y'):
            print('Goodbye!')
            sys.exit(0)
        from src.modules.wizard import Wizard
        wizard = Wizard(GAT_CONFIG)
        wizard.setup()
        wizard.confirm()
        wizard.write_config()

config_check(GAT_CONFIG)