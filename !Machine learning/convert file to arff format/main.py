
import csv
from time import sleep


class convert(object):
    content = []
    name = ''

    def __init__(self):
        self.csvInput()
        self.arffOutput()
        print ('\nFinished.')

    def csvInput(self):

        user = input('Enter the CSV file name: ')

        if user.endswith('.csv') == True:
            self.name = user.replace('.csv', '')

        print 'Opening CSV file.'
        try:
            with open(user, 'rb') as csvfile:
                lines = csv.reader(csvfile, delimiter=',')
                for row in lines:
                    self.content.append(row)
            csvfile.close()
            sleep(2)

        except IOError:
            sleep(2)
            print
            'File not found.\n'
            self.csvInput()


    def arffOutput(self):
        print 'Converting to ARFF file.\n'
        title = str(self.name) + '.arff'
        new_file = open(title, 'w')


        new_file.write('@relation ' + str(self.name) + '\n\n')

        for i in range(len(self.content[0]) - 1):
            attribute_type = input('Is the type of ' + str(self.content[0][i]) + ' numeric or nominal? ')
            new_file.write('@attribute ' + str(self.content[0][i]) + ' ' + str(attribute_type) + '\n')

        last = len(self.content[0])
        class_items = []
        for i in range(len(self.content)):
            name = self.content[i][last - 1]
            if name not in class_items:
                class_items.append(self.content[i][last - 1])
            else:
                pass
        del class_items[0]

        string = '{' + ','.join(sorted(class_items)) + '}'
        new_file.write('@attribute ' + str(self.content[0][last - 1]) + ' ' + str(string) + '\n')

        new_file.write('\n@data\n')

        del self.content[0]
        for row in self.content:
            new_file.write(','.join(row) + '\n')

        new_file.close()
        sleep(2)


run = convert()