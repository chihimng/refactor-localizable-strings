import sys
import os

basePath = sys.argv[1]
baseFile = sys.argv[2]
excludeFiles = ['Localizable.strings', baseFile]
targets = []

def keyValuesFrom(path):
    output = {}
    with open(path) as f:
        lines = f.read().splitlines()
        for line in lines:
            if line == '' or (line.startswith('/*') and line.endswith('*/')) or line.startswith('//'):
                continue
            key = line[:-1].split(' = ')[0][1:-1]
            value = line[:-1].split(' = ')[1][1:-1]
            output[key] = value
        return output

dictionary = keyValuesFrom(os.path.join(basePath, baseFile))
print(dictionary)

for myFile in os.listdir(basePath):
    if myFile.endswith('.strings') and not myFile in excludeFiles:
        targets.append(os.path.join(basePath, myFile))

for target in targets:
    with open(target) as fi:
        output = []
        lines = fi.read().splitlines()
        for line in lines:
            if line == '' or (line.startswith('/*') and line.endswith('*/')) or line.startswith('//'):
                output.append(line)
                continue
            key = line[:-1].split(' = ')[0][1:-1]
            if key in dictionary.keys():
                output.append('"'+key+'"'+' = '+'"'+dictionary[key]+'";')
            else:
                output.append(line)
        print(output)
        os.rename(target,target+'.orig')
        with open(target, 'w') as fo:
            for line in output:
                fo.write(line+'\n')
