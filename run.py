import sys, os

if __name__ == "__main__":
  try:os.system("git pull")
  except:pass
  try:os.mkdir("OK")
  except:pass
  try:os.mkdir("CP")
  except:pass
  __import__("Brute").menu()

