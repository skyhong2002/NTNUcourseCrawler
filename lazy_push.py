import os

cmds = ["git add .", 'git commit -m \"ONEISAN\"', "git push"]
[os.system(cmd) for cmd in cmds]