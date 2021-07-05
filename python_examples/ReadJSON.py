# https://www.geeksforgeeks.org/os-module-python-examples
# https://www.geeksforgeeks.org/read-json-file-using-python/

import math

'''
os module -> provides functionality for intercating with the Operating System
os & os.path modules -> include many functions to interact with the file system

'''

import os, json


def current_path():
    print(' get current working directory ', os.getcwd())



def changeCWD(cwd='/Users/karanalang/Documents'):
    current_path()
    os.chdir(cwd)
    current_path()


def createDirectory():
    home = '/Users/karanalang/Documents'
    new = 'os_test'

    path = os.path.join(home, new)

    print(" removing os_test directory ")
    os.rmdir(path)
    print(" creating os_test directory ")

    os.mkdir(path, 0o777)
    print(" path, list dirs in path -> ", path, os.listdir(path))
    # os.rmdir(path)
    os.listdir(path)


def write_read_open():
    fd = open('new.txt', 'w')
    fd.write(' Hello ')
    fd.close()
    fd1 = open('new.txt', 'r')
    text = fd1.read()
    print(" text -> ", text)
    os.rename('new.txt', 'renamed.txt')
    r = open('renamed.txt','w')
    r.write(" in renamed ")
    r.close()
    r = open('renamed.txt','r')
    print(" reading renamed -> ", r.read())
    r.close()
    # os.remove('renamed.txt')
    print(" os.path.exists -> ", os.path.exists('renamed.txt'), os.path.exists('new.txt'))
    print(" file size in bytes -> ", os.path.getsize('renamed.txt'))


def splitFile():
    path = '/Users/karanalang/Documents/0.EmployeeSystems/0.Prism-LOE/Extracts/BalanceDetails/'
    # path = '/Users/karanalang/Documents/0.EmployeeSystems/0.Prism-LOE/Extracts/MaheshEmpID/test'
    os.chdir(path)

    cnt = 0
    fdr = open('TAP_Balance_Details_Prism_2018.csv','r')
    # fdr = open('TAP_Balance_Details_Prism_20210610_2137.csv', 'r')
    # TAP_Balance_Details_Prism_20210610_2137.csv
    # fdw = open('TAP_Balance_Details_Prism_USA_1.csv','w')
    lines = fdr.readlines()
    print(type(lines), len(lines))
    maxCntInFile = 10**6-1
    numfiles = math.ceil(len(lines)/maxCntInFile)

    # print(math.ceil(10/3), 10//3, 8//3, math.ceil(8/3))


    print(" numfiles -> ", numfiles)
    curr = 1
    for i in range(numfiles):
        dest = "TAP_Balance_Details_Prism_2018_"+str(i)+".csv"
        fdw = open(dest, 'w')
        fdw.write(lines[0])
        for j in range(curr, curr+maxCntInFile):
            # print(lines[j], " - j - ", j)
            if j >= len(lines):
                break
            fdw.write(lines[j])
        fdw.close()
        print(" size of file -> ", os.path.getsize(dest))
        curr+=maxCntInFile

    # for l in lines:
    #     fdw.write(l)
    #     cnt+=1
    #     if cnt == 999999:
    #         break
    #
    # print(" size of file -> ", os.path.getsize('TAP_Balance_Details_Prism_USA_1.csv'))


def write_read_popen():
    current_path()
    fd = "GFG.txt"
    fd2 = os.popen(fd, 'w')
    fd2.write(' hello using os.popen ')
    # fd1 = open('new1.txt', 'r')
    # text = fd1.read()
    # print(" read text after popen -> ", text)

def read_linebyline():
    print(os.getcwd())
    fd = open('conan.txt', 'r')
    alllines = fd.readlines()
    for line in alllines:
        print(" lineby line -> ", line)



def readJsonFile(path):
    os.chdir(path)
    emp = open("emp.json", 'r')
    data = json.load(emp)
    print(data)
    names, email, job = [], [], []
    for d in data["emp_details"]:
        # print(d)
        names.append(d['emp_name'])
        email.append(d['email'])
        job.append(d['job'])
    print(" names -> ", names)
    print(" emails -> ", email)
    print(" job -> ", job)

def readJson(jsonStr):

    content = json.loads(jsonStr)
    print(" content ", content)
    for emp in content["emp_details"]:
        print(" names -> ", emp["name"])
        print(" languages -> ", emp["languages"])





print(" os.name ", os.name)

# changeCWD()
# createDirectory()
# write_read_open()
# write_read_popen()
# read_linebyline()
# readJsonFile("/Users/karanalang/Documents/Technology/Python_json_os/")

# jsonStr = '{"emp_details": [ {"name": "Bob", "languages": ["English", " French"]}, {"name": "Joe", "languages": ["Spanish", "German"]} ]}'
# readJson(jsonStr)
splitFile()



# home1 = '/Users/karanalang/Documents/Users/karanalang/Documents/os_test/os_test1'
# new1 = 'os_test2'
#
# path1 = os.path.join(home1, new1)

# print(" path1 -> ", path1)
# # os.makedirs(path1)
#
# print(" listdirs ")
# list_dirs = os.listdir('/Users/karanalang/Documents/')
#
# print(list_dirs)


