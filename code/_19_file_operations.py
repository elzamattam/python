# Open the file in read mode
file = open('E:\\GitHub\\python\\README.md','r')
print(file) # Only prints the metadata of 'file' object
print(file.readline()) # Prints the first line
print(file.readline()) # Prints the second line
# Prints all the contents in 'file', line by line
for line in file:
    print(line)


# Open the file in write mode - this overwrites the existing content
file = open('E:\\GitHub\\python\\README.md','w')
file.write('abc')


# Open the file in append mode - this just appends to the existing content
file = open('E:\\GitHub\\python\\README.md','a')
file.write('\npython')
file.write('\nPython learning.\nThis repository contains files related to created during the programming sessions.This is very useful for beginners.')


# Very important: Always close the opened file after using
file.close()



file_read = open('E:\\GitHub\\python\\README.md','r')
file_write = open('E:\\GitHub\\python\\README1.md','w')
try:
    content = file_read.read() # Reads the whole content
    file_write.write(content)
finally:    
    # This finally makes sure that the file references are closed no matter what (after normal execution or exception)
    file_read.close()
    file_write.close()