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

class messages:
  INITSOLU = "__name__ = 'solution'\ndef solution():\n    from usage import messages\n    return messages.PASSED+messages.HINT\nif __name__ == '__main__':\n    solution()"
  REQUEST_ERR =  bcolors.FAIL+"Please submit the solution before requiring."+bcolors.ENDC
  HELP = bcolors.ENDC+"\nUse the following shell commands:\n"+bcolors.WARNING+"cd"+bcolors.ENDC+"	change directory [dir_name]\n"+bcolors.WARNING+"cat"+bcolors.ENDC+"	print file [file_name]\n"+bcolors.WARNING+"ls"+bcolors.ENDC+"	list directory contents [dir_name]\n"+bcolors.WARNING+"request"+bcolors.ENDC+"	request new challenge\n"+bcolors.WARNING+"verify"+bcolors.ENDC+"	runs tests on solution file [file_name]\n"
  HINT = bcolors.ENDC+"For a list of commands type "+bcolors.WARNING+'help'+bcolors.ENDC+". To get started with your first challenge type "+bcolors.WARNING+'request'+bcolors.ENDC+"."
  MISSING = bcolors.FAIL+"Type 'request' to start challenge"+bcolors.ENDC
  PASSED = bcolors.OKGREEN+"The function has passed all the tests."+bcolors.ENDC