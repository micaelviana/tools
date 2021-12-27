import os

packages = ['brave-bin','caffeine-ng','google-chrome','mintstick']

for item in packages:
    command = "yay -S "+item+" --needed"
    os.system(command)
