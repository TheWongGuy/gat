import sys, os, subprocess, webbrowser
from iterfzf import iterfzf
from src.modules.printer import Printer
from src.modules.color import Color
from fuzzyfinder import fuzzyfinder

GAT_CONFIG = '~/.gat/config'
GAT_FOLDER = '~/.gat'
config = {}

# Preform initial check of ~/.gat/config file
def config_check():
    global config
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

def populate_defaults():
    global config

    if(config.get("PROJECTS") is None):
        config["PROJECTS"] = "~/projects"

    
def handle_params(params):
    if(len(params) == 0):
        # TODO : Display help
        print("GAT; Adam Wong")
        sys.exit(0)
    
    # Process initial command
    if(params[0] == "clone"):
        # Clone Command
        if(len(params) < 2):
            Printer.error("Expected a repository parameter.")
            sys.exit(1)
        
        # TODO: Different formats of repository
        # For now doing default, no user specified
        repo = params[1]
        from src.modules.gitobj import GitObj
        gitobj = GitObj(repo, config)
        project_path = gitobj.clone()
        os.system("echo \'" + os.path.expanduser(project_path) + "\'" + " > " + GAT_FOLDER + "/gattemporary")
        sys.exit(0)
    elif(params[0] == "cd"):
        if(len(params) < 2):
            Printer.error("Expected a project name to find.")
            sys.exit(1)
        project = params[1]
        project_path = os.path.expanduser(config["PROJECTS"]) + "/" + config["USER"] + "/" + project
        if not os.path.exists(project_path):
            projects = [dir for dir in os.listdir(os.path.dirname(project_path)) if os.path.isdir(os.path.join(os.path.dirname(project_path), dir))]
            filtered = list(fuzzyfinder(project, projects))
            if(len(filtered) == 0):
                Printer.error("No project matches.")
                sys.exit(1)
            elif(len(filtered) == 1):
                project_path = os.path.expanduser(config["PROJECTS"]) + "/" + config["USER"] + "/" + filtered[0]
            else:
                project = iterfzf(filtered)
                project_path = os.path.expanduser(config["PROJECTS"]) + "/" + config["USER"] + "/" + project

        os.system("echo \'" + project_path + "\'" + " > " + GAT_FOLDER + "/gattemporary")
        sys.exit(0)
    elif(params[0] == "open"):
        called_from = os.environ.get("CURDIR")
        if(len(params) == 1):
            gitrepo = called_from + '/.git'
            if not os.path.exists(gitrepo):
                Printer.error("Current directory is not a git repository.")
                sys.exit(1)
            remoteurl = subprocess.check_output('git config --get remote.origin.url', shell=True, cwd=called_from, universal_newlines=True)
            remoteurl = remoteurl.replace(':', '/')
            remoteurl = remoteurl.replace('git@', '')
            remoteurl = 'http://www.' + remoteurl 
            webbrowser.open(remoteurl, new=0, autoraise=True)

            




            

config_check()
# Remove temporary
if os.path.exists(os.path.expanduser(GAT_FOLDER) + '/gattemporary'):
    os.system("rm " + GAT_FOLDER + "/gattemporary")
populate_defaults()
handle_params(sys.argv[1:])