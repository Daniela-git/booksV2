import re
def convertToNumber(value):
  # $ 209.20
  regx = r"\D"
  return int(re.sub(regx,"",value))