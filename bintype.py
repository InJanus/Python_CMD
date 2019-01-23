import sys


class bbyte():
    def __init__(self, number, **letter):
        self.nums = [0,0,0,0,0,0,0,0]
        if 'letter' in letter:
            innum = ord(str(letter)[12])
            self.mynum = number
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
            # print(str(mybins[i]) + '  | i: ' + str(i))

    def newNum(self, number):
        innum = number
        self.mynum = number
        for i in range(0,8):
            if innum >= pow(2, 7-i):
                self.nums[i] = 1
                innum = innum - pow(2, 7-i)

    def tostring(self):
        outputstr = ''
        for i in range(0,8):
            outputstr = outputstr + str(self.nums[i])
        return outputstr

        

def encode(sentence):
    # add spaces so it can easily scramble the bits

    while len(sentence)%8 != 0:
        sentence = sentence + ' '
    outputbin = [None] * len(sentence)
    tempbin = [None] * len(sentence)

    for i in range(0,len(sentence)):
        outputbin[i] = bbyte(0, letter = sentence[i])

    # total_num = range(0,8*len(outputbin))
    jump = int(len(outputbin)/8)
    # print('jump: ' + str(jump))

    for repeat in range(0,jump):
        for i in range(0+(repeat*8),8+(repeat*8)):
            tempstr = ''
            for j in range(0+(repeat*8),8+(repeat*8)):
                tempstr = tempstr + str(outputbin[j].nums[i%8])
            tempbin[i] = bbyte(0)
            tempbin[i].newNumbin(tempstr)
    return tempbin

def fileendcode(filename):
    print()



    
def writeToFile(inbbyte, filename):
    f = open(filename, 'wb')
    for i in range(0, len(inbbyte)):
        f.write(inbbyte[i].tohex())
    f.close()




temp = encode('Hello! this is a coded message that takes some software to decode')
writeToFile(temp, 'test.file')










# test = bbyte(1)
# print(test.printNum())
# test.newNumbin('11001011')
# print(test.printNum())

# ==============================================

# empty_bytes = bbyte(2)
# testbytes = [None] * 256
# print(empty_bytes.tohex())

# print(len(testbytes))
# f = open('test.file', 'wb')
# for i in range(0,256):
#     testbytes[i] = bbyte(i)
#     print(testbytes[i].tohex())
#     f.write(testbytes[i].tohex())
# f.close()


# ==============================================
# for i in range(0,8):

#     sys.stdout.write(str(empty_bytes.nums[i]))

# print()
# print(empty_bytes.toletter())

# mybytes = [0] * 255
# for i in range(0,255):
#     mybytes[i] = bbyte(i)

# mybytes[1]
# for i in range(0,255):
#     print(mybytes[i].toletter())

# class bbtyeARR():
#     def __init__(self, sentence):
#         lengthofsentence =  len(sentence)
#         self.types = [] * lengthofsentence




