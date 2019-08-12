import re


def linestodict(listtoparse,keylist, uniquekeylist):
    for f in uniquekeylist:
        if f in listtoparse:
            indexlist = [index for index, value in enumerate(listtoparse) if value == f]
            for i in reversed(indexlist):
                listtoparse.insert(i, '**')

        listtoparse.insert(len(listtoparse), '**')
    dct = {}

    for i in keylist:
        adelement = listtoparse[listtoparse.index(i) + 1:listtoparse.index('**', 1)]
        if i not in dct:
            dct['%s' % i] = adelement
        else:
            dct[i] = dct[i] + adelement
        del listtoparse[listtoparse.index(i):listtoparse.index('**', 1)+1]
    return dct


def rmvsubstring(inputlist, substring):
    for e in inputlist:
        if substring in e:
            inputlist.remove(e)


def instancecount(inputlist, outputdict):
    for i in inputlist:
        outputdict[i] = inputlist.count(i)


def listsearch(pattern,inputlist,outputlist):
    for i in inputlist:
        match = re.findall(pattern, i)
        if match:
            outputlist.append(match[0])

