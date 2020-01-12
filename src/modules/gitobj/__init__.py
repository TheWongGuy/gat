import os, sys, subprocess, shutil
from src.modules.printer import Printer
from src.modules.color import Color
from yaspin import yaspin
GIT_SSH_PREFIX = 'git@github.com'

class GitObj:
    REPO_STRING = ""
    config = {}
    repo = ""
    def __init__(self, repo, config):
        self.config = config
        self.repo = repo
        self.REPO_STRING = GIT_SSH_PREFIX + ":" + config["USER"] + "/" + repo + ".git"

    def clone(self):
        clone = "git clone " + self.REPO_STRING
        # CD into project directory
        user_directory ='~/projects/' + self.config["USER"]
        project_directory = user_directory + "/" + self.repo
        with yaspin(text="Creating directory...", color="yellow") as spinner:
            try:
                if not os.path.exists(os.path.expanduser(project_directory)):
                    os.makedirs(os.path.expanduser(project_directory))
                else:
                    spinner.stop()
                    Printer.error("Looks like this project already exists...")
                    restart = input("Would you like to clone anyway? (Y/N): ")
                    spinner.start()
                    if(restart.upper() == 'Y'):
                        shutil.rmtree(os.path.expanduser(project_directory))
                        os.makedirs(os.path.expanduser(project_directory))
                    else:
                        raise Exception("Project already exists.")
                spinner.ok("✅ ")
            except Exception as e:
                spinner.fail("❌ ")
                Printer.error(e)
                sys.exit(1)
        os.chdir(os.path.expanduser(user_directory))
        with yaspin(text="Cloning repository ...", color="yellow").white.bold.shark as spinner:
            try:
                subprocess.check_output(clone, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                spinner.ok("✅ ")
                Printer.success(str("Cloned project to: " + project_directory))
                Printer.important(str(" -> Changed your directory to: " + project_directory + " <-"))
                return project_directory
            except subprocess.CalledProcessError as e:
                spinner.fail("❌ ")
                Printer.error(str(e.output))
                sys.exit(1)

                