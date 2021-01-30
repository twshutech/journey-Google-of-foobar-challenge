__name__ = "__main__"

def verify():
  from usage import messages
  from os import path
  if path.exists("solution.py") == True:
    import solution
  else:
    print messages.MISSING

  return True

if __name__ == "__main__":
  verify()