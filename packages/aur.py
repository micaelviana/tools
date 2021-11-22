import os

packages = ['brave-bin','caffeine-ng','google-chrome','visual-studio-code-bin']

for item in packages:
    command = "yay -S "+item+" --needed"
    os.system(command)
