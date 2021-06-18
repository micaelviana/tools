import os

packages = ['google-chrome']

for item in packages:
    command = "yay -S "+item+" --needed"
    os.system(command)
