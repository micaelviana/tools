import os

packages = ['brave-bin','google-chrome','visual-studio-code-bin']

for item in packages:
    command = "yay -S "+item+" --needed"
    os.system(command)
