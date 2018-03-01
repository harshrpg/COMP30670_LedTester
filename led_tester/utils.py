import sys
sys.path.append('.')
import requests


def parseFile(filePath):

    ## Checking whether filepath starts with 'http' for it to be a network address
    if filePath.startswith("http:"):
        filePath = toFile(requests.get(filePath))
    with open(filePath) as fin:
        L = int(fin.readline())
        cmd=[]
        for i in fin.readlines():
            cmd.append(i.strip())
    return L, cmd

def toFile(response):
    with open('input.txt','w') as fout:
        fout.writelines(response.text)
    fout.close()
    return 'input.txt'

