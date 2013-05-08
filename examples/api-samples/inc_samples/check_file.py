import os
import time

def check_file(arg1, arg2):
    result = ""
    #counter to not wait forever
    counter = 0
    name = ""
    currentDir = os.path.dirname(os.path.realpath(__file__))
    downloadFolder = currentDir + '/../downloads'
    while True:
        time.sleep(5)
        files = os.listdir(downloadFolder)
        if len(files) > 0:
            name = files[0]
        if name == '':
            counter = counter + 1
        else:
            result = name
            break
        if counter >= 10:
            result = "File was not found. Looks like something went wrong."
            break
    return result