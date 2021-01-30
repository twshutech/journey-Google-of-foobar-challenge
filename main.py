__name__ = "__main__"
def main():
    import usage
    msg = usage.messages()
    global() msg
    status = 0
    print msg.HELP
    command(status)

challenges = (
    "Braille translation",
    "Numbers Station Coded msg",
    "Elevator Maintenance",
    "Prepare the Bunnies' Escape",
    "Bomb baby",
    "Fuel Injection Perfection"
    )

def mkpy():
    f = open("solution.py", "w+")
    f.write(msg.INITSOLU)

def command(status):
    from os import path
    cmd = raw_input()
    if cmd == 'request':
        if path.exists("solution.py") == True:
            print msg.REQUEST_ERR
            return command(status)
        readme = './'+challenges[status]+'/README.md'
        r = open(readme, 'r')
        print 'r', r.read()

        mkpy()
    elif  cmd == 'help':
        print msg.HELP
        command(status)
    elif cmd == 'verify':
        import Verify
        Verify
    else:
        return

if __name__ == "__main__":
    main()