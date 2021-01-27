class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

help_msg = bcolors.ENDC+"\nUse the following shell commands:\n"+bcolors.WARNING+"cd"+bcolors.ENDC+"	change directory [dir_name]\n"+bcolors.WARNING+"cat"+bcolors.ENDC+"	print file [file_name]\n"+bcolors.WARNING+"ls"+bcolors.ENDC+"	list directory contents [dir_name]\n"+bcolors.WARNING+"request"+bcolors.ENDC+"	request new challenge\n"+bcolors.WARNING+"verify"+bcolors.ENDC+"	runs tests on solution file [file_name]\n"
hint = "For a list of commands type "+bcolors.WARNING+'help'+bcolors.ENDC+". To get started with your first challenge type "+bcolors.WARNING+'request'+bcolors.ENDC+"."
challenges = (
    "Braille translation",
    "Numbers Station Coded Messages",
    "Elevator Maintenance",
    "Prepare the Bunnies' Escape",
    "Bomb baby",
    "Fuel Injection Perfection"
    )


def command(status):
    cmd = raw_input()
    if cmd == 'request':
        file = './'+challenges[status]+'/README.md'
        r = open(file, 'r')
        print 'file',r.read()


def main():
    status = 0
    print help_msg
    command(status)

if __name__ == "__main__":
    main()