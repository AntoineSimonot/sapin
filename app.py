import sys


from flask import Flask

app = Flask(__name__)
@app.route('/sapin')
def noParam():
    return '<p>Please enter a param in the url </p>'

@app.route('/sapin/<int:sizeOfSapin>')
def createSapin(sizeOfSapin):
    sapin = [
        '*',
        '***',
        '*****',
        '*******',
    ]
    start = 3

    branchToRepeat = sapin[2]
    repeatLine:int = 4
    latestBlock:list = []
    latestBranch = ''

    activate = 0
    blockCount = 0
    for block in range(sizeOfSapin-1):
        blockCount += 1
        repeatLine += 1
        latestBranch = branchToRepeat
        activate +=1
        latestBlock.append(branchToRepeat)
        for j in range(repeatLine -1):
            latestBranch = createBranch(len(latestBranch) + 2)
            latestBlock.append(latestBranch)
        for m in latestBlock:
            sapin.append(m)
        if block < 3:
            if(activate == 3):
                activate = 0
                start += 1
                branchToRepeat = latestBlock[start]
            else:
                branchToRepeat = latestBlock[start]
        else:
            if(block == 4) :
                activate = 1
                start += 1
                branchToRepeat = latestBlock[start]
            if(activate == 3):
                activate = 1
                start += 1
                branchToRepeat = latestBlock[start]
            else:
                branchToRepeat = latestBlock[start]
        pop_all(latestBlock)
    if sizeOfSapin <= 0 :
        return 'Nothing'
    if sizeOfSapin >= 30 :
        return "<p>n can't be higher or equal to 30</p>"
    else:
        sapin = renderSapin(sapin, sizeOfSapin)
        return '<pre>' + sapin + '</pre>'
        

def pop_all(l):
    r, l[:] = l[:], []
    return r


def createBranch(branchAmmout: int):
    branch = ''
    for i in range(branchAmmout):
        branch += '*'
    return branch


def renderSapin(sapin, pipe):
    fir = sapin # array of Fir
# -----------------------------------------------------------
    lastBranchOfFir = sapin[-1]
    roundOfLastValueOfLeaves = len(lastBranchOfFir)//2
    allValues = ""
    pipeValues = ""
    for i, value in enumerate(fir):
        fir[i] = (' ' * (roundOfLastValueOfLeaves -len(value)//2  )) + value
    for value in fir:
        if value == fir[-1]:
            allValues = allValues + value
        else:
            allValues = allValues + value + '\n'
    for i in range(pipe):
        if pipe % 2 != 0: 
            pipeValues = pipeValues + (' ' * (roundOfLastValueOfLeaves -pipe//2  )) + ('|' * pipe) + '\n'
        else: 
            pipe += 1
            pipeValues = pipeValues + (' ' * (roundOfLastValueOfLeaves -pipe//2  )) + ('|' * pipe) + '\n'
    return allValues + "\n" + pipeValues
    
# -----------------------------------------------------------





