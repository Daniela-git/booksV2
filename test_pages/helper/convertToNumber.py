import re
def convertToNumber(value):
  # $ 209.20
  regx = r"\D"
  try:
    return int(re.sub(regx,"",value))
  except:
    return 0