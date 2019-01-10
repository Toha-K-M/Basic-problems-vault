from urllib import request
import re

url_names = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.names'
url_data = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'

def download_datasets(data_url):
    flag = 0
    b = []
    name = input("Enter dataset name: ")
    print(name)
    response_names = request.urlopen(url_names)
    response = request.urlopen(url_data)
    set_names = response_names.read()
    set_names = str(set_names)
    set_data = response.read()
    set_data = str(set_data,'utf-8')
    lines_names = set_names.split("\\n")
    lines = set_data.split("\\n")
    dest_url=r'dataset.arff'
    fx = open(dest_url, "w")
    for line in lines_names:
        fx.write("%" + line + "\n")
    fx.write("\n@RELATION " + name + "\n\n")
    ########### finding attribute name from Attribute Information: section
    for line in lines_names:
        if 'Attribute Information:' in line:
            flag = 1
            continue
        if 'Missing Attribute Values: ' in line:
            break
        if flag == 1:
            if (re.findall(r'[0-9].(.*?)in',line)):
                x = re.findall(r'[0-9].(.*?)in',line)[0]#[0] to print as string as it is getting stored in list
                fx.write("@ATTRIBUTE " + x.replace(" ","") + " NUMERIC" + "\n")
                print(x.replace(" ",""))# replacing white space
           # above 3 line will find between [0-9]. to in to get the attribute name except the class attribute
        if 'class:' in line: ######### started to write class
            flag = 2
            continue
        if flag == 2:
            y = line.replace("--","")
            print(y.replace(" ",""))
            b.append(y.replace(" ",""))
    fx.write("@ATTRIBUTE class {")
    for i in range(0,len(b)-1):# -1 is for a white space that occurs after -- in class:
        fx.write(b[i])
        if i is not 2:
            fx.write(',')
    fx.write("}\n")
    fx.write("\n@DATA\n")
    for line in lines:
        fx.write(line + "\n")
    fx.close()

download_datasets(url_data)