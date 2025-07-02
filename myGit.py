#### Created by David N Preiss


### TABLE OF CONTENTS
"""
intro
imports
"""

### INTRO
"""
This code is for managing git operations
"""

### Import statements
if True:
    import shutil
    import os
    import subprocess
    # System call
    os.system("")

    # Class of different styles
    class style():
        BLACK = '\033[30m'
        RED = '\033[31m'
        GREEN = '\033[32m'
        YELLOW = '\033[33m'
        BLUE = '\033[34m'
        MAGENTA = '\033[35m'
        CYAN = '\033[36m'
        WHITE = '\033[37m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'
    try:
        import GitPython
    except ImportError as e:
        print(style.RED + f"!--ERROR:{e}\nGitPython is not installed. Installing..." + style.RESET)
        subprocess.check_call(["pip", "install", "GitPython"])
        print("Installation complete. You can now run the script.")