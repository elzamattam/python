# file = open('E:\GitHub\python\README.md','r')
# print(file)
# print(file.readline())
# print(file.readline())
# for line in file:
#     print(line)
# python
# Python learning.
# This repository contains files related to created during the programming sessions.This is very useful for beginners.

# file = open('E:\GitHub\python\README.md','w')
# file.write('abc')

# file = open('E:\GitHub\python\README.md','a')
# file.write('\npython')
# file.write('\nPython learning.\nThis repository contains files related to created during the programming sessions.This is very useful for beginners.')

try:
    file_read = open('E:\GitHub\python\README.md','r')
    file_write = open('E:\GitHub\python\README1.md','w')

    content = file_read.read()
    file_write.write(content)
finally:    
    file_read.close()
    file_write.close()