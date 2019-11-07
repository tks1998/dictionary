
fo = open("data2.txt","r")

line = fo.readline()
print("Read Line: %s" % (line))

# Again set the pointer to the beginning
line = fo.readline()
fo.readline(18)
print("Read Line: %s" % (line))

# Close opend file
fo.close()