
import re
 
def isValid(s):
     
    # 1) Begins with 0 or 91
    # 2) Then contains 7 or 8 or 9.
    # 3) Then contains 9 digits
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    if (Pattern.match(s)) and len(s) == 12: 
        print(True)
        return True
    else:
        print(False)
        return False

number = 7304298382
isValid(str(910000000000+number))

 