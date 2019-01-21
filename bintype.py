import sys


class bbyte():
    def __init__(self, innumber, *letter):
        self.nums = [0,0,0,0,0,0,0,0]
        try:
            self.mynum = innumber
        except:
            self.mynum = ord(letter)
        number = innumber
        if number < 256:
            if number >= 128:
                self.nums[0] = 1
                number = number - 128
            if number >= 64:
                self.nums[1] = 1
                number = number - 64
            if number >= 32:
                self.nums[2] = 1
                number = number - 32
            if number >= 16:
                self.nums[3] = 1
                number = number - 16
            if number >= 8:
                self.nums[4] = 1
                number = number - 8
            if number >= 4:
                self.nums[5] = 1
                number = number - 4
            if number >= 2:
                self.nums[6] = 1
                number = number - 2
            if number == 1:
                self.nums[7] = 1
                number = number - 1
        else:
           print("Value is bigger than 256")

    def toletter(self):
        return chr(self.mynum)

    



empty_bytes = bbyte(97, None)

for i in range(0,8):

    sys.stdout.write(str(empty_bytes.nums[i]))

print()
print(empty_bytes.toletter())

mybytes = [0] * 255
for i in range(0,255):
    mybytes[i] = bbyte(i)

mybytes[1]
for i in range(0,255):
    print(mybytes[i].toletter())

class bbtyeARR():
    def __init__(self, sentence):
        lengthofsentence =  len(sentence)
        self.types = [] * lengthofsentence




