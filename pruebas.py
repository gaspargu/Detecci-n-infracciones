a = [['a','b'],['c','d']]

def writer(file_name, data):
    with open(file_name, 'w') as f:
        for i in range(len(a)):
            line = ''
            for j in range(len(a[i])):
                line += a[i][j]+','
            line = line[:-1]
            line += '\n'
            f.write(line)


writer('bla.txt',a)

