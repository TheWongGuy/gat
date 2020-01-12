import sys, os
from src.modules.color import Color

GAT_CONFIG = '~/.gat/config'
config = {}

# Preform initial check of ~/.gatconfig file
def config_check(config: str):
    from src.modules.wizard import Wizard
    if not os.path.isfile(os.path.expanduser(GAT_CONFIG)):
        print("Looks like " + Color.GREEN + Color.BOLD + GAT_CONFIG +  Color.END  + " doesn't exist.")
        response = input(Color.BOLD + "Would you like us to help you set it up? (Y/N): " + Color.END)
        if(response.upper() != 'Y'):
            print('Goodbye!')
            sys.exit(0)
        wizard = Wizard(GAT_CONFIG)
        wizard.setup()
        wizard.confirm()
        wizard.write_config()
    else:
        wizard = Wizard(GAT_CONFIG)
        wizard.read_config()
    config = wizard.get_config()
    
config_check(GAT_CONFIG)