# We have to open a file before reading or writing.
# f = open( "file _ name", "mode")

# r : read mode
# w : write mode

# data = f.read( )
# f.close( )

# 'r' open for reading (default)
# 'w' open for writing, truncating the file first
# 'x' create a new file and open it for writing
# 'a' open for writing, appending to the end of the file if it exists
# 'b' binary mode
# 't' text mode (default)
# '+' open a disk file for updating (reading and writing)

#  to combine two mode , f=open("file name","rt")

f=open("demo.txt","r")
data=f.read()

print(data)
print(type(data))
print(len(data))

# after reading f.read() -> it read entire file and pointer go at end of file so unabl to read line
line1=f.readline()
print(line1)

line2=f.readline()
print(line2)

f.close()