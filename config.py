import sys
import os

#grant permission
os.system("chmod +x scripts/*.sh")

flags = {
  "-g": "git.sh",
}

if __name__ == "__main__":
    #the program assumes that the python filename is the first argument, so I cant start at the beggining
    for i in range(1,len(sys.argv)):
        flag=sys.argv[i]
        if flag in flags:
            argument=flags[flag]
            command="bash scripts/"+argument
            os.system(command)

