#fw = open('./file_lab/file_lab.txt', 'w') #new directory is slightly more complicated
fw = open('./file_lab.txt', 'w')

fw.write("Hello World!\n")
fw.write("Hello World!\n")
fw.write("Hello World!\n")
fw.close()

"""
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	open for exclusive creation, failing if the file already exists
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)
'U'	universal newlines mode (deprecated)
"""
# fr = open('./file_lab.txt', 'r')
# buff = fr.read()
# print(buff)
# fr.close()


# fr = open('./file_lab.txt', 'r')
# buff = fr.readline()
# print(buff[:-1])
# buff = fr.readline()
# print(buff[:-1])
# buff = fr.readline()
# print(buff[:-1])
# buff = fr.readline()
# print(buff[:-1])
# fr.close

with open('./file_lab.txt') as fr:  #with statement: syntactic sugar for try/finally block. cleans stuff up
    for l in fr:    #file object is line iterable
        print(l[:-1])    #[:-1] means list[0.. second last]

