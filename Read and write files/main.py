fw = open('sample.txt', 'w') # open and create and w is to write to it
fw.write('writing some stuff in my text file\n')
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r') # open and r for read
text = fr.read() # read file and store in text string
print(text)
fr.close()

