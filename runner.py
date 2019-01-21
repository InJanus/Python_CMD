import datetime
import subprocess
import os
import sys
import re
import time


def splitInput(myinput):
    words = []
    tempword = ''
    myinput =  myinput + ' '
    for i in range(0,len(myinput)):
        if myinput[i] != ' ':
            tempword = tempword + myinput[i]
        else:
            words.append(tempword)
            tempword = ''
    return words

def command(commandCtl):
    currentPath = os.getcwd()
    if commandCtl[0] + commandCtl[1] == 'changedir':
        if commandCtl[2] == 'back':
            previousDicrectory = re.search('([A-Z]?:?[\\\\/]?.*[\\\\/]).*', currentPath)
            os.chdir(previousDicrectory.group(1))
        else:
            os.chdir(commandCtl[2])
    if commandCtl[0] + commandCtl[1] == 'clearscreen':
        os.system('cls')
    if commandCtl[0] + commandCtl[1] == 'showcwd':
        print()
        os.system('dir')
        print()
    if commandCtl[0] + commandCtl[1] == 'newfile':
        myfilename = input('Enter file name: ')
        try:
            f = open(myfilename,'x')
        except FileExistsError:
            print('That file already exists you doughnut.')
    if commandCtl[0] + commandCtl[1] == 'editfile':
        try:
            editfilename = commandCtl[2]
        except IndexError:
            editfilename = input('Enter file name: ')
        try:
            f = open(editfilename, 'w')
            print()
            print('File : ' + editfilename)
            print('To stop writing to a file type stopgog')
            print('WRITING FROM THIS FILE WILL DELETE ALL PREVIOUS WORK')
            while True:
                stoptext = input(' > ')
                if stoptext == 'stopgog':
                    break
                else:
                    f.write(stoptext + '\n')

        except FileExistsError:
            print('That file doesn\'t exist you egg')
    if commandCtl[0] + commandCtl[1] == 'viewfile':
        try:
            viewfilename = commandCtl[2]
        except IndexError:
            viewfilename = input('Enter file name: ')
            
        try:
            f = open(viewfilename, 'r')
            ledata = os.path.getatime(currentPath + '\\' + viewfilename)
            print('File : ' + viewfilename)
            print('Last edit made : ' + time.ctime(ledata) + '\n')
            for line in f:
                sys.stdout.write(line)
            print()
        except FileNotFoundError:
            print('You going to give me a file to read or...?')
    if commandCtl[0] + commandCtl[1] == 'binfile':
        print()


print('BC SYSTEM CMD - INGANUS SOFTWARE')
timestart = datetime.datetime.now()
print(str(timestart) + '\n')

myinput = ''
myquit = False
while not myquit:
    path = os.getcwd()
    myinput = input('==|' + str(path) + '>')
    
    commands = splitInput(myinput)
    if myinput == 'quit':
        myquit = True
    elif commands[0] == 'cmd':
        cmdcommand = ''
        for i in range(1,len(commands)):
            cmdcommand = cmdcommand + commands[i]
        os.system(cmdcommand)
    elif myinput == '':
        print('\n')
    else:
        command(commands)







