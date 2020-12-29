# String Manipulation

str = 'X-DSPAM-Confidence: 0.8475 '

# Find and extract portion of the string after colon
# colpos = str.find(':')
# print(colpos)
# 
# substr = str[colpos+1:]
# print(substr)
# 
# 
# numstr = substr.strip()
# print(numstr)
# 
# print(float(numstr))

print(float(str[str.find(':')+1:].strip()))