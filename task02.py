inp = 'KOE'
out = 'MQG'
transtab = str.maketrans(inp, out)

s = input('Enter the string: \n')
res = s.translate(transtab)
print(res)