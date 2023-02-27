import sys, os

if __name__ == "__main__":
  try:
      os.system("git pull")
  try:
      os.mkdir("OK")
  try:
      os.mkdir("CP")
      __import__("rembo").menu()
  except Exception as e:
    exit(str(e))
