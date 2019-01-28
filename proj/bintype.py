import sys
import re
# from decimal import *


class bbyte():
    def __init__(self, number, **letter):
        self.nums = [0,0,0,0,0,0,0,0]
        if 'letter' in letter:
            myletter = re.search('.*?\'.*?\'.*?\'(.*?)\'', str(letter)).group(1)
            innum = 0
            if len(myletter) == 4:
                innum = int(innum)
            elif len(myletter) == 2:
                innum = int(innum)
            else:
                innum = ord(myletter)
            self.mynum = innum
        else:
            innum = number
            self.mynum = number
        
        if innum < 256:
            for i in range(0,8):
                if innum >= pow(2, 7-i):
                    self.nums[i] = 1
                    innum = innum - pow(2, 7-i)
        else:
           print('Error: Value is bigger than 255')
    def toletter(self):
        return chr(self.mynum)

    def tohex(self):
        return self.mynum.to_bytes(1,'big')


    def newNumbin(self, bintype):
        # this is to update a number to binary format
        self.mynum = 0
        for i in range(0, 8):
            self.nums[i] = int(bintype[i])
            if self.nums[i]:
                self.mynum = self.mynum + pow(2, (7-i))
            # print(str(self.nums[i]) + '  | i: ' + str(i))

    def newNum(self, number):
        innum = number
        self.mynum = number
        for i in range(0,8):
            if innum >= pow(2, 7-i):
                self.nums[i] = 1
                innum = innum - pow(2, 7-i)
            else:
                self.nums[i] = 0

    def tostring(self):
        outputstr = ''
        for i in range(0,8):
            outputstr = outputstr + str(self.nums[i])
        return outputstr

    def tonum(self):
        return self.mynum

def encode(sentence, progress):
    # add spaces so it can easily scramble the bits

    while len(sentence)%8 != 0:
        sentence = sentence + ' '
    outputbin = [None] * len(sentence)
    tempbin = [None] * len(sentence)


    if progress:
        counterstep = 100/(len(sentence)*8)

    for i in range(0,len(sentence)):
        outputbin[i] = bbyte(0, letter = sentence[i])
    jump = int(len(outputbin)/8)
    counter = 0

    for repeat in range(0,jump):
        for i in range(0+(repeat*8),8+(repeat*8)):
            tempstr = ''
            for j in range(0+(repeat*8),8+(repeat*8)):
                tempstr = tempstr + str(outputbin[j].nums[i%8])
                if progress:
                    counter = counter + counterstep
                    sys.stdout.write("\r%d%% ==> Encoding Progress" % counter)
                    sys.stdout.flush()

            tempbin[i] = bbyte(0)
            tempbin[i].newNumbin(tempstr)
    return tempbin



def decode(sentence, progress):
    tempbin = [None] * len(sentence)
    for i in range(0,len(sentence)):
        tempbin[i] = bbyte(ord(sentence[i]))

    if progress:
        counterstep = 100/(len(sentence)*8)

    outputbin = [bbyte(0)] * len(tempbin)
    jump = int(len(outputbin)/8)
    tempstring = ''
    counter = 0
    for repeat in range(0,jump):
        for i in range(0+(8*repeat),8+(8*repeat)):
            tempstring = ''
            for j in range(0+(8*repeat),8+(8*repeat)):
                tempstring = tempstring + str(tempbin[j].nums[i%8])
                if progress:
                    counter = counter + counterstep
                    sys.stdout.write("\r%d%% ==> Decoding Progress" % counter)
                    sys.stdout.flush()

            outputbin[i] = bbyte(0)
            outputbin[i].newNumbin(tempstring)
            # print('i : ' + str(i+(8*repeat)) +'   repeat: '+ str(repeat) +  '      ' + str(outputbin[i].toletter()))
    counter = 100
    sys.stdout.write("\r%d%% ==> Decoding Progress" % counter)
    sys.stdout.flush()
    return outputbin
            
    

def fileencode(filename):
    print()



    
def writeToFile(inbbyte, filename, progress):
    if progress:
        counterstep = 100/(len(inbbyte))
        # print(counterstep)

    counter = 0
    f = open(filename, 'wb')
    for i in range(0, len(inbbyte)):
        if progress:
                    counter = counter + counterstep
                    sys.stdout.write("\r%d%% ==> Writting File Progress" % counter)
                    sys.stdout.flush()

        f.write(inbbyte[i].tohex())
    f.close()

def getFromFile(filename, progress):
    
    
    f = open(filename, 'rb')
    tempbyte = f.read()
    f.close()
    returnbyte = [None] * len(tempbyte)
    if progress:
        counterstep = 100/(len(tempbyte))

    counter = 0
    for i in range(0, len(tempbyte)):
        if progress:
                counter = counter + counterstep
                sys.stdout.write("\r%d%% ==> Reading File Progress" % counter)
                sys.stdout.flush()
        returnbyte[i] = bbyte(tempbyte[i])
    return returnbyte

def getFromFileStr(filename):
    f = open(filename, 'r')
    tempbyte = f.read()
    f.close()
    return tempbyte


def view(inbbyte):
    print()
    for i in range(1, len(inbbyte)+1):
        print(inbbyte[i-1].tostring(), end = ' ')
        if i%8 == 0:
            print()

    print()

def viewChr(inbbyte):
    tempstr = ''
    
    for i in range(1, len(inbbyte)+1):
        tempstr = tempstr + inbbyte[i-1].toletter()

    return tempstr

def viewChr_v2(inbbyte):
    for i in range(1, len(inbbyte)+1):
        print(inbbyte[i-1].toletter(),end = '')


# f = open('pi.txt', 'r')
# encodestring = f.read()
# print('to Encode: ' + encodestring)
# temp = encode(encodestring,True)
# viewChr_v2(temp)
# print('\nBefore: ' + viewChr_v2(temp))
# temp = [bbyte(255)]*8
# writeToFile(temp, 'test.file',True)

# temp2 = getFromFile('test.file',True)
# temp2 = decode(viewChr(temp2), True)
# print('\nAfter: ' + viewChr_v2(temp2))
# viewChr_v2(temp2)
# f.close()



