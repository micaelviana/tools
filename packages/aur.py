import os

packages = ['brave-bin','caffeine-ng','google-chrome','mintstick']
temp = ['fnm-bin']

for item in temp:
    command = "yay -S "+item+" --needed"
    os.system(command)
