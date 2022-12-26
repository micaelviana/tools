import sys
import os

#grant permission
os.system("chmod +x scripts/*.sh")

flags = {
    "-g": "git.sh",
    "-d": "directories.sh",
    "-t": "tmux.sh"
}

if __name__ == "__main__":
    #the program assumes that the python filename is the first argument, so I cant start at the beggining
    if(len(sys.argv)>1):
        for i in range(1,len(sys.argv)):
            flag=sys.argv[i]
            if flag in flags:
                argument=flags[flag]
                command="bash scripts/"+argument
                os.system(command)
    else:
        print("Available options:")
        print("python config.py -g will run git.sh")
        print("python config.py -d will run directories.sh")
        print("python config.py -t will run tmux.sh")
        print()
        print("More than one can be used. Eg:")
        print("python config.py -d -g")

